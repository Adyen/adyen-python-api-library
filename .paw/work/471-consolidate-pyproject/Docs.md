# Technical Documentation: Consolidate Package Metadata into pyproject.toml

**Date**: 2025-07-21 | **Issue**: [#471](https://github.com/Adyen/adyen-python-api-library/issues/471) | **Branch**: feature/471-consolidate-pyproject

## Summary

This change eliminates metadata duplication between `setup.py` and `pyproject.toml` by making `pyproject.toml` the single source of truth for all package metadata, following PEP 621. The existing `setup.py` is reduced to a minimal 2-line shim that delegates entirely to setuptools.

## Motivation

Package metadata was duplicated across two files, which caused a real bug: `pydantic>=2.0` was listed in `pyproject.toml` dependencies but missing from `setup.py`'s `install_requires` (fixed in PR #468). This consolidation prevents that entire class of sync-related bugs.

## Changes Made

### 1. `setup.py` → Minimal Shim

**Before**: 45-line file with full metadata (name, version, description, author, classifiers, extras, etc.)
**After**: 2-line shim — `from setuptools import setup` / `setup()`

The shim exists for backward compatibility with legacy build tools that invoke `python setup.py install` directly. Modern pip reads metadata from `pyproject.toml` via PEP 517.

### 2. `pyproject.toml` — Three Additions

| Section | Purpose |
|---------|---------|
| `[project.urls]` | Homepage, Repository, Issues links (previously only in setup.py `url` field) |
| `[tool.setuptools.packages.find]` | Package discovery with `include = ["Adyen*"]` (replaces setup.py `find_packages()`) |
| `build-system.requires` bump | `setuptools>=45` → `setuptools>=61.0.0` (minimum for PEP 621 support) |

### 3. `Makefile` — Install Target

**Before**: `pip install requests pycurl mock coveralls ruff` (hardcoded individual packages)
**After**: `pip install -e ".[requests,test,dev]"` (editable install using pyproject.toml extras)

Pycurl is intentionally excluded (requires system libcurl; tested via tox). Coveralls is dropped (CI-only, not in any extras group).

### 4. CI Workflows

| File | Change |
|------|--------|
| `release.yml` | Removed `setup.py` from `version-files` (shim has no version to bump) |
| `lint.yml` | Cache key changed from `hashFiles('**/setup.py')` to `hashFiles('**/pyproject.toml')` |

## Version Synchronization

After this change, version appears in three files (down from four):

| File | Field | Bumped By |
|------|-------|-----------|
| `VERSION` | Plain text | Release automation (source of truth) |
| `pyproject.toml` | `version = "X.Y.Z"` | Release automation (perl `s///`) |
| `Adyen/settings.py` | `LIB_VERSION = "X.Y.Z"` | Release automation (perl `s///`) |

`setup.py` no longer contains a version string. The release automation's perl substitution is a no-op on files with no match.

## Verification

| Command | Expected Result |
|---------|-----------------|
| `make install && make tests` | Editable install + all 162 tests pass |
| `make lint` | All checks passed |
| `pip install .` | Installs with pydantic>=2.0 as dependency |
| `python -m build --sdist --wheel` | Builds with correct metadata |
| `grep -c 'version' setup.py` | Returns 0 |

## Out of Scope

- `VERSION` file — unchanged, remains release automation source of truth
- `setup.cfg` — unchanged, legacy config (redundant but harmless)
- `Adyen/settings.py` — unchanged, provides runtime version for API headers
- `tox.ini` — unchanged, installs deps directly (future improvement candidate)
