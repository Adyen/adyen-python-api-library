# Consolidate Package Metadata into pyproject.toml — Implementation Plan

## Overview

Eliminate metadata duplication between `setup.py` and `pyproject.toml` by making `pyproject.toml` the single source of truth (PEP 621). Replace `setup.py` with a minimal shim, add missing sections to `pyproject.toml`, update the Makefile install target, and fix CI workflow references to `setup.py`.

## Current State Analysis

Package metadata is fully duplicated between `setup.py` (45 lines) and `pyproject.toml` (81 lines). The duplication already caused a real bug: `install_requires=[]` in `setup.py` while `pyproject.toml` correctly has `dependencies = ["pydantic>=2.0"]` (PR #468).

`pyproject.toml` is nearly complete — it only lacks `[tool.setuptools.packages.find]` and `[project.urls]` sections. The `build-system.requires` needs a bump from `setuptools>=45` to `setuptools>=61.0.0` for PEP 621 support.

Two CI workflows reference `setup.py`: `release.yml:38` (version-files) and `lint.yml:30` (cache key hash). The `Makefile:2` install target hardcodes individual packages instead of using pyproject.toml extras.

No tests verify packaging metadata — all existing tests cover API runtime behavior.

## Desired End State

- `pyproject.toml` is the sole, authoritative source of all package metadata
- `setup.py` is a 2-line shim: `from setuptools import setup` / `setup()`
- `make install` uses pyproject.toml extras for development setup
- CI workflows reference `pyproject.toml` instead of `setup.py` where applicable
- All existing tests continue to pass without modification
- `pip install .`, `pip install -e ".[requests,test,dev]"`, and `python -m build` all work correctly

**Verification approach**: `make install && make tests` in a clean virtualenv; `make lint`; manual inspection of file contents.

## What We're NOT Doing

- Removing `setup.py` entirely (kept as shim for backward compatibility)
- Modifying `VERSION` file
- Modifying `setup.cfg`
- Modifying `Adyen/settings.py`
- Updating `tox.ini` to use pyproject.toml extras
- Adding `coveralls` to any extras group
- Removing `wheel` from `build-system.requires`

## Phase Status

- [x] **Phase 1: Metadata Consolidation** — Consolidate all metadata into pyproject.toml and update all dependent files
- [x] **Phase 2: Documentation** — Create Docs.md technical reference

## Phase Candidates

<!-- No candidates — this is a well-scoped, atomic change set -->

---

## Phase 1: Metadata Consolidation

All five file changes are tightly coupled and must be applied atomically — the pyproject.toml additions and setup.py simplification are interdependent. Covers FR-001 through FR-008.

### Changes Required:

- **`setup.py`** (lines 1-45): Replace entire file with minimal shim:
  ```python
  from setuptools import setup
  setup()
  ```
  This removes all duplicate metadata (name, version, description, author, dependencies, classifiers, etc.). The shim delegates entirely to setuptools which reads `[project]` from `pyproject.toml`. (FR-002)

- **`pyproject.toml`**:
  - **Line 2**: Bump `requires = ["setuptools>=45", "wheel"]` → `requires = ["setuptools>=61.0.0", "wheel"]` (FR-005)
  - **After line 32** (after classifiers closing bracket): Add `[project.urls]` section with Homepage, Repository, Issues (FR-004)
  - **After `[project.optional-dependencies]` section** (after line 46): Add `[tool.setuptools.packages.find]` section with `include = ["Adyen*"]` (FR-003)
  
  The `[project.urls]` placement follows PEP 621 convention — URLs go after the main `[project]` table. The `[tool.setuptools.packages.find]` section goes before `[tool.ruff]` since it's a setuptools concern.

- **`Makefile`** (line 2): Change install target from `@pip install requests pycurl mock coveralls ruff` to `@pip install -e ".[requests,test,dev]"` (FR-006)
  
  This installs the project in editable mode with requests, test, and dev extras from pyproject.toml. Intentionally excludes pycurl (requires system libcurl, handled by tox) and drops coveralls (not in any extras; CI-only).

- **`.github/workflows/release.yml`** (line 38): Change `version-files: setup.py pyproject.toml Adyen/settings.py` → `version-files: pyproject.toml Adyen/settings.py` (FR-007)
  
  The shim setup.py has no version string, so keeping it in the list is misleading (though harmless — perl `s///` is a no-op on no match).

- **`.github/workflows/lint.yml`** (line 30): Change `hashFiles('**/setup.py')` → `hashFiles('**/pyproject.toml')` (FR-008)
  
  After consolidation, `setup.py` is a static 2-line shim that never changes — useless as a cache invalidation key.

- **Tests**: No test changes needed. All 24 test files test API runtime behavior via mocked HTTP responses. The import paths (`import Adyen`, `from Adyen import settings`) are unaffected.

### Success Criteria:

#### Automated Verification:
- [ ] `pip install .` in clean env installs pydantic: `pip install . && python -c "import pydantic"` (SC-001)
- [ ] Editable install with extras: `pip install -e ".[requests,test,dev]"` succeeds and extras available (SC-002)
- [ ] Package build + metadata: `python -m build --sdist --wheel` succeeds; inspect built metadata for correct name, version, dependencies, URLs (SC-003)
- [ ] Full dev workflow: `make install && make tests` succeeds with all tests passing (SC-004)
- [ ] Lint passes: `make lint`

#### Manual Verification:
- [ ] `setup.py` contains exactly 2 lines (import + setup call), no metadata arguments (SC-005)
- [ ] `grep -c 'version' setup.py` returns 0 — no version string in setup.py (SC-006)
- [ ] `pyproject.toml` has `[project.urls]`, `[tool.setuptools.packages.find]`, and `setuptools>=61.0.0` (FR-003, FR-004, FR-005)
- [ ] `release.yml` version-files does not include `setup.py` (FR-007)
- [ ] `lint.yml` cache key uses `hashFiles('**/pyproject.toml')` (FR-008)

---

## Phase 2: Documentation

> Depends on: Phase 1

### Changes Required:

- **`.paw/work/471-consolidate-pyproject/Docs.md`**: Technical reference documenting the consolidation — what changed, why, verification approach, and impact on maintainer workflows. Load `paw-docs-guidance` for template.

- **No project documentation updates**: This is an internal packaging improvement. The README already describes the library correctly. No user-facing APIs change. No CHANGELOG entry needed (internal chore, not a feature/fix users interact with).

### Success Criteria:
- [ ] Docs.md accurately captures the as-built state
- [ ] Content is consistent with actual implementation

---

## References

- Issue: https://github.com/Adyen/adyen-python-api-library/issues/471
- Spec: `.paw/work/471-consolidate-pyproject/Spec.md`
- Research: `.paw/work/471-consolidate-pyproject/SpecResearch.md`, `.paw/work/471-consolidate-pyproject/CodeResearch.md`
