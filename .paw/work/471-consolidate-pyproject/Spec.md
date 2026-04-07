# Feature Specification: Consolidate Package Metadata into pyproject.toml

**Branch**: feature/471-consolidate-pyproject  |  **Created**: 2026-04-07  |  **Status**: Draft
**Input Brief**: Eliminate metadata duplication between setup.py and pyproject.toml by making pyproject.toml the single source of truth (PEP 621)

## Overview

The Adyen Python API Library currently maintains package metadata in two places: `setup.py` and `pyproject.toml`. This duplication has already caused a real bug — the `pydantic>=2.0` dependency was added to `pyproject.toml` but missed in `setup.py` (fixed in PR #468), meaning users installing via certain code paths could get a broken install without pydantic.

This specification defines the consolidation of all package metadata into `pyproject.toml` as the single authoritative source, following PEP 621 — the Python standard for declaring project metadata in `pyproject.toml`. The existing `setup.py` will be reduced to a minimal shim that delegates entirely to setuptools, which reads metadata from `pyproject.toml`. Supporting files (CI workflows, Makefile) will be updated to reflect the new single source of truth.

The primary beneficiaries are library maintainers, who will no longer need to keep two files in sync when adding dependencies, updating metadata, or bumping versions. Contributors benefit from a clear canonical location for package configuration. End users benefit from consistent dependency resolution regardless of their installation method.

## Objectives

- Eliminate metadata duplication that caused the pydantic dependency bug (Rationale: prevents an entire class of sync-related bugs)
- Establish pyproject.toml as the single source of truth for all package metadata (Rationale: aligns with PEP 621 and modern Python packaging standards)
- Ensure the development setup command (`make install`) installs dependencies from the same source as production builds (Rationale: catches dependency mismatches early)
- Keep CI/CD workflows accurate by removing stale references to setup.py as a metadata source (Rationale: prevents misleading cache keys and no-op version bumps)

## User Scenarios & Testing

### User Story P1 – Maintainer adds a new dependency

Narrative: A maintainer needs to add a new runtime dependency to the library. They add it to `pyproject.toml` under `dependencies` and are confident this single change is sufficient for all install paths — pip install, editable install, tox, and CI builds.

Independent Test: Add a dependency to `pyproject.toml` `dependencies`, run `pip install .`, and verify the dependency is installed.

Acceptance Scenarios:
1. Given `pyproject.toml` lists `pydantic>=2.0` in `dependencies`, When a user runs `pip install .`, Then pydantic is installed as a dependency
2. Given `pyproject.toml` lists a new dependency, When setup.py is not updated, Then the dependency is still correctly installed (because setup.py is a shim)
3. Given a maintainer edits only `pyproject.toml`, When `python -m build` runs, Then the built wheel includes the correct dependency metadata

### User Story P2 – Developer sets up local environment

Narrative: A developer clones the repository and runs `make install` to set up their local development environment. All test, dev, and runtime dependencies are installed from pyproject.toml extras, and the project is available in editable mode.

Independent Test: Run `make install` in a fresh virtualenv and verify the project is importable and test dependencies are available.

Acceptance Scenarios:
1. Given a clean virtualenv, When the developer runs `make install`, Then the Adyen package is installed in editable mode with test and dev dependencies
2. Given `make install` has been run, When the developer runs `make tests`, Then tests execute successfully with all required dependencies present

### User Story P3 – Release automation bumps version

Narrative: The release automation action triggers a version bump. It updates version strings in `pyproject.toml` and `Adyen/settings.py` without attempting to modify `setup.py` (which no longer contains a version).

Independent Test: Simulate a version bump by replacing the version string in `pyproject.toml` and `Adyen/settings.py`, build the package, and verify the new version appears in the built distribution metadata.

Acceptance Scenarios:
1. Given the release workflow runs, When it processes `version-files`, Then it updates `pyproject.toml` and `Adyen/settings.py` only (setup.py is not in the list)
2. Given setup.py is not listed in `version-files`, When the release action runs, Then setup.py is not processed at all

### Edge Cases

- **Legacy pip install**: Users with older pip versions that invoke `python setup.py install` — the minimal shim delegates to setuptools which reads pyproject.toml. This path requires setuptools ≥ 61.0.0 to be already installed in the user's environment (note: `build-system.requires` only applies via PEP 517 frontends like `pip install`, not direct `python setup.py` invocation). The risk is low — setuptools 61.0.0 was released in March 2022 and is widely available.
- **Editable install**: `pip install -e .` works with the shim + pyproject.toml metadata via PEP 660 (setuptools ≥ 64) or legacy mode (shim present)
- **tox environments**: tox.ini installs deps directly (not via extras) — unaffected by this change, continues to work as-is
- **setup.py with no version**: The release action's perl substitution is a no-op on a file with no version string — no error, no change

## Requirements

### Functional Requirements

- FR-001: pyproject.toml `[project]` table is the sole source of package metadata (name, version, description, dependencies, classifiers, etc.) (Stories: P1, P3)
- FR-002: setup.py contains only `from setuptools import setup; setup()` with no metadata arguments (Stories: P1, P2)
- FR-003: pyproject.toml includes `[tool.setuptools.packages.find]` configuration for package discovery (Stories: P1)
- FR-004: pyproject.toml includes `[project.urls]` with Homepage, Repository, and Issues links (Stories: P1)
- FR-005: `build-system.requires` specifies `setuptools>=61.0.0` (minimum for PEP 621 support) (Stories: P1, P2)
- FR-006: `make install` installs the project in editable mode using pyproject.toml extras (Stories: P2)
- FR-007: Release workflow `version-files` no longer includes setup.py (Stories: P3)
- FR-008: CI lint workflow cache key uses pyproject.toml hash instead of setup.py hash (Stories: P2)

### Cross-Cutting / Non-Functional

- All existing tests pass without modification after the consolidation
- Package builds (`python -m build`) produce equivalent core metadata (name, version, dependencies, classifiers) to the current release. The `long_description` (full README) and `project-urls` fields are intentionally improved.
- No breaking change for users who `pip install Adyen` from PyPI

## Success Criteria

- SC-001: `pip install .` in a clean environment installs `pydantic>=2.0` as a dependency (FR-001)
- SC-002: `pip install -e ".[requests,test,dev]"` succeeds and all extras are available (FR-001, FR-003, FR-006)
- SC-003: `python -m build --sdist --wheel` succeeds and the built metadata shows correct name, version, dependencies, and URLs (FR-001, FR-003, FR-004, FR-005)
- SC-004: `make install && make tests` succeeds with all tests passing (FR-006)
- SC-005: setup.py contains exactly two lines: an import and a setup() call with no arguments (FR-002)
- SC-006: `grep -c 'version' setup.py` returns 0 — no version string in setup.py (FR-002, FR-007)

## Assumptions

- The `release-automation-action` perl-based version substitution gracefully handles files where no match is found (confirmed: perl `s///` with no match is a no-op)
- The `adyen-sdk-automation` code generator does not generate or modify `setup.py` (confirmed by SpecResearch — templates only generate service files)
- Keeping `wheel` in `build-system.requires` alongside setuptools (harmless, improves compatibility)
- The `coveralls` package previously installed by `make install` is not required for local development (it was a CI-only tool); dropping it from `make install` is acceptable
- Excluding `pycurl` from `make install` is acceptable — it requires system-level libcurl, often fails on developer machines without it, and is adequately tested via tox's pycurl variant

## Scope

In Scope:
- Simplify setup.py to minimal shim
- Add `[tool.setuptools.packages.find]` to pyproject.toml
- Add `[project.urls]` to pyproject.toml
- Bump `build-system.requires` to `setuptools>=61.0.0`
- Update Makefile `install` target to use pyproject.toml extras
- Update `release.yml` to remove setup.py from version-files
- Update `lint.yml` cache key from setup.py to pyproject.toml

Out of Scope:
- Removing setup.py entirely (kept as shim for backward compatibility)
- Modifying `VERSION` file
- Modifying `setup.cfg`
- Modifying `Adyen/settings.py`
- Updating `tox.ini` to use pyproject.toml extras (future improvement)
- Adding `coveralls` to pyproject.toml extras

## Dependencies

- setuptools ≥ 61.0.0 (for PEP 621 `[project]` table support) — released March 2022, widely available
- Adyen release-automation-action v1.4.0 (must handle version-files update)

## Risks & Mitigations

- **Release automation breaks with updated version-files**: The perl substitution is a simple find-and-replace that operates on the file list. Removing setup.py from the list is a safe reduction. Mitigation: The VERSION file (source of truth for the action) and Adyen/settings.py remain in the list unchanged.
- **Code generation overwrites setup.py**: Confirmed by research that adyen-sdk-automation does NOT touch setup.py or pyproject.toml. Mitigation: None needed; risk is eliminated.
- **Legacy build tools fail**: Some very old tools may not support pyproject.toml. Mitigation: The minimal setup.py shim ensures backward compatibility with any tool that invokes `python setup.py install`.

## References

- Issue: https://github.com/Adyen/adyen-python-api-library/issues/471
- PR #468: Fixed pydantic dependency in pyproject.toml (the bug that motivated this issue)
- PEP 621: https://peps.python.org/pep-0621/
- Python Packaging Authority migration guide: https://packaging.python.org/en/latest/guides/modernize-setup-py-project/
- Research: .paw/work/471-consolidate-pyproject/SpecResearch.md
- Work Shaping: .paw/work/471-consolidate-pyproject/WorkShaping.md
