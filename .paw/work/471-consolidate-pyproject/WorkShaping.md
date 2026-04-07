# Work Shaping: Consolidate Package Metadata into pyproject.toml (PEP 621)

**Issue**: [#471](https://github.com/Adyen/adyen-python-api-library/issues/471)
**Origin**: Follow-up from PR #468 which fixed `pydantic>=2.0` missing from `setup.py`

## Problem Statement

Package metadata is duplicated across `setup.py` and `pyproject.toml`, leading to drift. The `pydantic>=2.0` dependency was added to `pyproject.toml` but missed in `setup.py` (PR #468). The root cause is having two sources of truth for the same information.

**Who benefits**: Maintainers (fewer places to update), contributors (clear canonical location), and users (consistent dependency resolution regardless of install method).

## Work Breakdown

### Core Work

1. **Add `[tool.setuptools.packages.find]` to `pyproject.toml`**
   - Include `Adyen*`, exclude `tests` and `tests.*`
   - This replaces the `find_packages()` call in `setup.py`

2. **Add `[project.urls]` to `pyproject.toml`**
   - Homepage, Repository, Issues links
   - Replaces the `url=` parameter lost from `setup.py`

3. **Bump `build-system.requires` to `setuptools>=61.0.0`**
   - Required for PEP 621 (`[project]` table) support
   - Released March 2022, well-established; pip build isolation installs it regardless

4. **Simplify `setup.py` to minimal shim**
   ```python
   from setuptools import setup
   setup()
   ```
   - All metadata now comes from `pyproject.toml`
   - Kept (not removed) because release automation (`release-automation-action`) targets it as a version file

5. **Update Makefile `install` target**
   - Change from hardcoded `pip install requests pycurl mock coveralls ruff`
   - To `pip install -e ".[test,dev,requests,pycurl]"` using pyproject.toml extras
   - Single source of truth for dependencies

### Out of Scope (Explicit Decisions)

- **`VERSION` file**: Left as-is. Not used by release automation, not hurting anything.
- **`setup.cfg`**: Left as-is. Contains some legacy config, but narrowing scope to the issue's intent.
- **`Adyen/settings.py`**: Must keep `LIB_VERSION` — used at runtime for API headers. Cannot be eliminated without changing how the client reads version.
- **Removing `setup.py` entirely**: Too disruptive to release automation config; minimal shim achieves the deduplication goal.

## Edge Cases & Expected Handling

| Scenario | Handling |
|----------|----------|
| `pip install .` (modern pip) | Reads `pyproject.toml` directly — works |
| `python setup.py install` (legacy) | Shim delegates to setuptools which reads `pyproject.toml` — works with `setuptools>=61` |
| `python setup.py sdist/bdist_wheel` (legacy) | Same delegation — works |
| Release automation bumps version | Action updates `setup.py pyproject.toml Adyen/settings.py` — `setup.py` shim has no version to bump, but action should handle this gracefully (it searches for version patterns) |
| `adyen-sdk-automation` regenerates code | May regenerate `setup.py` with full metadata — see Risk Assessment |

## Architecture Sketch

**Before** (metadata flow):
```
setup.py ──────────┐
                    ├──> pip install (picks one, inconsistency possible)
pyproject.toml ────┘
```

**After** (metadata flow):
```
pyproject.toml ──────> pip install (single source)
       │
setup.py (shim) ─────> delegates to pyproject.toml via setuptools
```

**Version still lives in 3 files** (release automation manages sync):
- `pyproject.toml` → packaging
- `Adyen/settings.py` → runtime API headers  
- `setup.py` → will have no version (shim only)

## Critical Analysis

**Value**: High. Prevents the exact class of bug that prompted PR #468. Low effort, high confidence.

**Build vs Modify**: Pure modification — no new tooling or infrastructure. Standard Python packaging modernization.

**Tradeoff**: Keeping `setup.py` as a shim is slightly redundant, but avoids touching release automation config (owned by Adyen, not us).

## Codebase Fit

- `pyproject.toml` already has a comprehensive `[project]` section — this work just makes it authoritative
- The library follows standard Python packaging conventions
- No custom build steps that would conflict with pure `pyproject.toml` metadata

## Risk Assessment

1. **Release automation compatibility**: The `release-automation-action` looks for version patterns in `setup.py`. With the shim having no `version=`, the action may fail or skip it. This needs testing, or the workflow's `version-files` should drop `setup.py`.
   - **Mitigation**: After changes, verify that `release-automation-action` handles a version-less `setup.py` gracefully, or update `release.yml` to remove `setup.py` from `version-files`.

2. **`adyen-sdk-automation` code generation**: If the automation repo regenerates `setup.py` with full metadata, it would undo this consolidation.
   - **Mitigation**: Document this in the PR. The automation templates may need a corresponding update in `adyen-sdk-automation`.

3. **Editable installs**: `pip install -e .` with `pyproject.toml` + setuptools works fine with `setuptools>=61`.

## Open Questions for Downstream Stages

1. Does `release-automation-action` handle a `setup.py` with no `version=` string? If not, should `setup.py` be removed from `version-files` in `release.yml`?
2. Does `adyen-sdk-automation` generate `setup.py`? If so, the template needs updating too.
3. Should `coveralls` be added to pyproject.toml extras since the Makefile currently installs it but it's not in any extras group?

## Session Notes

- **Scope kept tight**: User chose to leave `VERSION` file and `setup.cfg` alone
- **Makefile update included**: User wants `make install` to use pyproject.toml extras instead of hardcoded deps
- **Minimal shim over removal**: Avoids disrupting release automation owned by Adyen
- **`setuptools>=61.0.0`** confirmed as the version floor (matches issue proposal)
- **Project URLs to be added**: Homepage, Repository, Issues links in `[project.urls]`
