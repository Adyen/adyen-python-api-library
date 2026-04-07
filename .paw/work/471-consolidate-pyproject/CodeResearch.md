# Code Research: Consolidate pyproject.toml (PEP 621)

```yaml
date: 2025-07-21
git_commit: afa5b8b809c54d8e19fe63fe4fb183dea3f1ddc7
branch: feature/471-consolidate-pyproject
repository: /home/erdemtuna/workspace/personal/adyen-python-api-library
topic: Consolidate package metadata into pyproject.toml, eliminate setup.py duplication
tags: [pyproject.toml, PEP-621, setup.py, packaging, CI, release-automation]
status: complete
```

## Research Question

Where does package metadata currently live, what references exist to `setup.py` across the codebase, and what exact lines must change to make `pyproject.toml` the sole source of truth?

## Summary

Package metadata is **fully duplicated** between `setup.py` (45 lines) and `pyproject.toml` (81 lines). The `pyproject.toml` already contains a complete `[project]` table with all metadata, optional-dependencies, and tool configs. The only things **missing** from `pyproject.toml` are `[tool.setuptools.packages.find]` and `[project.urls]`. Only **two files** outside setup.py reference it: `release.yml:38` (version-files) and `lint.yml:30` (cache key). No tests verify packaging metadata. The `Makefile install` target uses raw `pip install` commands (not extras) — it needs updating per FR-006.

## Documentation System

| Item | Status |
|------|--------|
| `docs/` directory | **Does not exist** |
| Sphinx / mkdocs | **Not present** |
| `README.md` | Exists (18,814 bytes) — referenced by `pyproject.toml:9` as `readme = "README.md"` |
| `CONTRIBUTING.md` | Exists (887 bytes) |
| `CODE_OF_CONDUCT.md` | Exists (3,349 bytes) |
| `LICENSE.md` | Exists (1,062 bytes) — MIT License |

## Verification Commands

| Command | Purpose | Source |
|---------|---------|--------|
| `make tests` | Run unit tests via `python -m unittest discover -s test -p '*Test.py'` | Makefile:14 |
| `make lint` | Run ruff linter: `ruff check Adyen test` | Makefile:5 |
| `make install` | Install deps: `pip install requests pycurl mock coveralls ruff` | Makefile:2 |
| `tox` | Run full matrix (py38-py314, pycurl/requests/urllib, lint) | tox.ini:2 |
| `pip install -e ".[dev]"` | Install with dev extras (used in lint.yml:37) | .github/workflows/lint.yml:37 |
| `python -m build --sdist --wheel` | Build distributions (used in pypipublish.yml:33-38) | .github/workflows/pypipublish.yml:33-38 |
| `ruff check Adyen test` | Direct ruff invocation | Makefile:5, lint.yml:41 |
| `ruff format --check Adyen test` | Formatter check | lint.yml:45 |

## Detailed Findings

---

### 1. `setup.py` (45 lines) — IN SCOPE, MUST MODIFY

**Full content analysis:**

| Lines | Content | Notes |
|-------|---------|-------|
| 1 | `from setuptools import find_packages, setup` | Imports `find_packages` — not needed in shim |
| 3-45 | `setup(...)` with all kwargs | **All of this becomes the shim** |
| 4 | `name="Adyen"` | Duplicated at pyproject.toml:6 |
| 5 | `packages=find_packages(include=["Adyen*"], exclude=["tests", "tests.*"])` | Replaced by `[tool.setuptools.packages.find]` in pyproject.toml |
| 6 | `version="15.0.0"` | Duplicated at pyproject.toml:7, Adyen/settings.py:2, VERSION:1 |
| 7-8 | `maintainer`/`maintainer_email` | Duplicated at pyproject.toml:14-16 |
| 9-10 | `description`/`long_description` | Duplicated at pyproject.toml:8-9 (pyproject uses README.md) |
| 11-12 | `author`/`author_email` | Duplicated at pyproject.toml:11-13 |
| 13 | `url="https://github.com/Adyen/adyen-python-api-library"` | **NOT in pyproject.toml** — needs `[project.urls]` |
| 14 | `keywords=["payments", "adyen", "fintech"]` | Duplicated at pyproject.toml:17 |
| 15 | `python_requires=">=3.8"` | Duplicated at pyproject.toml:10 |
| 16 | `install_requires=[]` | **Empty!** pyproject.toml:18 has `["pydantic>=2.0"]` — this is the known discrepancy |
| 17-29 | `extras_require={...}` | Duplicated at pyproject.toml:34-46 |
| 31-44 | `classifiers=[...]` | Duplicated at pyproject.toml:19-32 |

**Target state:** Replace entire file with:
```python
from setuptools import setup
setup()
```

**Integration points:**
- `.github/workflows/release.yml:38` — `version-files: setup.py pyproject.toml Adyen/settings.py`
- `.github/workflows/lint.yml:30` — `hashFiles('**/setup.py')`
- No Python code imports from `setup.py`
- `adyen-sdk-automation` does **not** generate `setup.py` (confirmed in SpecResearch)

---

### 2. `pyproject.toml` (81 lines) — IN SCOPE, MUST MODIFY

**Current sections:**

| Lines | Section | Status |
|-------|---------|--------|
| 1-3 | `[build-system]` | Exists. `requires = ["setuptools>=45", "wheel"]`. **Must update** `setuptools>=45` → `setuptools>=61.0.0` per FR-005 |
| 5-32 | `[project]` | Complete metadata. Already has name, version, description, readme, requires-python, authors, maintainers, keywords, dependencies, classifiers |
| 34-46 | `[project.optional-dependencies]` | Complete. Has requests, pycurl, test, dev extras |
| 48-60 | `[tool.ruff]` | Exists. Out of scope |
| 62-75 | `[tool.ruff.lint]` | Exists. Out of scope |
| 77-78 | `[tool.ruff.lint.isort]` | Exists. Out of scope |
| 80-81 | `[tool.coverage.run]` | Exists. Out of scope |

**Missing sections (must add):**

1. **`[tool.setuptools.packages.find]`** — FR-003. Replaces `setup.py:5` `find_packages(include=["Adyen*"], exclude=["tests", "tests.*"])`. Should be:
   ```toml
   [tool.setuptools.packages.find]
   include = ["Adyen*"]
   ```

2. **`[project.urls]`** — FR-004. Replaces `setup.py:13` `url=...`. Should be:
   ```toml
   [project.urls]
   Homepage = "https://github.com/Adyen/adyen-python-api-library"
   Repository = "https://github.com/Adyen/adyen-python-api-library"
   Issues = "https://github.com/Adyen/adyen-python-api-library/issues"
   ```

**Must change:**
- Line 2: `requires = ["setuptools>=45", "wheel"]` → `requires = ["setuptools>=61.0.0", "wheel"]`

**Integration points:**
- `.github/workflows/release.yml:38` — listed in `version-files` (stays)
- `.github/workflows/lint.yml:30` — will become the new cache key hash source
- `.github/workflows/lint.yml:37` — `pip install -e ".[dev]"` reads extras from here
- `tox.ini` — tox installs the package, reads metadata from here
- `.github/workflows/pypipublish.yml:33-38` — `python -m build` reads from here

---

### 3. `Makefile` (103 lines) — IN SCOPE, MUST MODIFY

**Relevant targets:**

| Lines | Target | Current Command | Issue |
|-------|--------|-----------------|-------|
| 1-2 | `install` | `pip install requests pycurl mock coveralls ruff` | **FR-006**: Should use `pip install -e ".[test,dev,requests,pycurl]"` or equivalent extras-based install |
| 4-5 | `lint` | `ruff check Adyen test` | No change needed |
| 7-8 | `lint-fix` | `ruff check --fix Adyen test` | No change needed |
| 10-11 | `format` | `ruff format Adyen test` | No change needed |
| 13-14 | `tests` | `python -m unittest discover -s test -p '*Test.py'` | No change needed |
| 16-17 | `coverage` | `coverage run -m unittest discover...` | No change needed |
| 20-101 | Generator targets | OpenAPI code gen | Out of scope |

**Integration points:**
- `tox.ini:13` — `commands = make tests`
- `.github/workflows/lint.yml` — does **not** use `make install`; uses `pip install -e ".[dev]"` directly

---

### 4. `.github/workflows/release.yml` (43 lines) — IN SCOPE, MUST MODIFY

**Key line:**
- **Line 38**: `version-files: setup.py pyproject.toml Adyen/settings.py`

This is the `Adyen/release-automation-action@v1.4.0` parameter that lists files to apply version bumps via perl regex substitution. The action reads the current version from the `VERSION` file (or detects it), then runs `perl -i -pe"s/$old/$new/g"` on each listed file.

**FR-007 change:** Remove `setup.py` from this line → `version-files: pyproject.toml Adyen/settings.py`

**Context:** The shim `setup.py` will have no version string. While perl's `s///` is a no-op on no-match (harmless), keeping `setup.py` in the list is misleading.

---

### 5. `.github/workflows/lint.yml` (61 lines) — IN SCOPE, MUST MODIFY

**Key line:**
- **Line 30**: `key: ${{ runner.os }}-pip-${{ hashFiles('**/setup.py') }}`

**FR-008 change:** Update to `hashFiles('**/pyproject.toml')` since after consolidation, `setup.py` is a static 2-line shim that never changes — useless as a cache invalidation key.

**Other notable lines (no changes needed):**
- Line 37: `pip install -e ".[dev]"` — already uses pyproject.toml extras. No change.
- Line 41: `ruff check Adyen test` — no change.
- Line 45: `ruff format --check Adyen test` — no change.

---

### 6. `.github/workflows/python-ci.yml` (44 lines) — VERIFICATION ONLY

**No `setup.py` references found.** This workflow:
- Line 38: `pip install tox` — installs tox
- Line 43: `tox` — runs tox which invokes `make tests`

Confirmed clean. No changes needed.

---

### 7. `.github/workflows/pypipublish.yml` (49 lines) — VERIFICATION ONLY

**No `setup.py` references found.** This workflow:
- Line 29-30: `pip install build` — installs build tool
- Line 33-38: `python -m build --sdist --wheel --outdir dist/ .` — builds from pyproject.toml

Confirmed clean. No changes needed.

---

### 8. `tox.ini` (20 lines) — OUT OF SCOPE, VERIFIED

**Content analysis:**
- Line 2: `envlist = py{38,39,310,311,312,313,314}-{pycurl,requests,urllib},lint`
- Lines 8-11: `deps = mock; requests: requests; pycurl: pycurl` — installs deps per variant
- Line 13: `commands = make tests`
- Lines 15-20: lint env uses `ruff>=0.4.4`

**No references to `setup.py` or `pyproject.toml`.** Tox implicitly installs the package using the build backend, which reads pyproject.toml. No changes needed.

---

### 9. `setup.cfg` (14 lines) — OUT OF SCOPE, VERIFIED

**Content:**
- Line 1: `[bdist_wheel]` (empty section)
- Lines 3-4: `[metadata]` with `description_file = README.md`
- Lines 6-9: `[egg_info]` with tag settings
- Lines 11-14: `[coverage:run]` with `source = Adyen/` (duplicated in pyproject.toml:80-81)

**No version or metadata that conflicts.** The `description_file = README.md` is a legacy setuptools config, but with `pyproject.toml` having `readme = "README.md"`, this is redundant but harmless. Out of scope per spec.

---

### 10. `Adyen/settings.py` (2 lines) — OUT OF SCOPE, AWARENESS ONLY

```python
LIB_NAME = "adyen-python-api-library"  # line 1
LIB_VERSION = "15.0.0"                 # line 2
```

**Used by:**
- `Adyen/client.py:123` — `self.LIB_VERSION = settings.LIB_VERSION`
- `Adyen/client.py:124` — `self.USER_AGENT_SUFFIX = settings.LIB_NAME + "/"`
- `Adyen/client.py:387-388` — used in HTTP headers
- `Adyen/client.py:435` — passed to `lib_version`

**Stays in `release.yml` version-files.** No changes needed to this file.

---

### 11. `VERSION` (1 line) — OUT OF SCOPE, AWARENESS ONLY

Content: `15.0.0` (line 1, with trailing newline)

This is the canonical version source read by the release automation action. Not listed in `version-files` — the action reads it separately to determine the current version. Out of scope.

---

## Test Coverage

### Test Structure

The `test/` directory contains 24 test files, all named `*Test.py`. They test API service functionality via mocked HTTP responses (`test/mocks/` directory).

**No tests exist for:**
- Package metadata correctness
- Import structure / packaging
- Version consistency across files
- `setup.py` behavior

**Relevant test observations:**
- `test/BaseTest.py` — Base test class, imports `Adyen` package
- All tests use `import Adyen` and `from Adyen import settings` — these import paths are unaffected by the consolidation
- `test/methodNamesTests/checkoutTest.py` — generated test for method names

**Conclusion:** No existing tests will break from the consolidation. The changes are purely in build/packaging configuration files and CI workflows. The Python test suite tests runtime API behavior, not packaging metadata.

---

## Code References (Consolidated)

### Files that MUST change (in scope):

| File | Line(s) | What changes |
|------|---------|--------------|
| `setup.py` | 1-45 (entire file) | Replace with 2-line shim |
| `pyproject.toml` | 2 | `setuptools>=45` → `setuptools>=61.0.0` |
| `pyproject.toml` | after line 32 | Add `[project.urls]` section |
| `pyproject.toml` | after line 46 | Add `[tool.setuptools.packages.find]` section |
| `Makefile` | 2 | Change install to use pyproject.toml extras |
| `.github/workflows/release.yml` | 38 | Remove `setup.py` from `version-files` |
| `.github/workflows/lint.yml` | 30 | Change `hashFiles('**/setup.py')` → `hashFiles('**/pyproject.toml')` |

### Files verified clean (no changes needed):

| File | Reason |
|------|--------|
| `.github/workflows/python-ci.yml` | No setup.py references |
| `.github/workflows/pypipublish.yml` | No setup.py references |
| `tox.ini` | No setup.py references; implicitly reads pyproject.toml |
| `setup.cfg` | Legacy config, out of scope |
| `Adyen/settings.py` | Runtime version, out of scope |
| `VERSION` | Release automation source, out of scope |

### All `setup.py` references in non-PAW files:

| Location | Reference | Action |
|----------|-----------|--------|
| `setup.py` (itself) | Full metadata file | Replace with shim |
| `.github/workflows/release.yml:38` | `version-files: setup.py pyproject.toml Adyen/settings.py` | Remove `setup.py` |
| `.github/workflows/lint.yml:30` | `hashFiles('**/setup.py')` | Change to `hashFiles('**/pyproject.toml')` |

No other files in the repository reference `setup.py`.

---

## Architecture Documentation

### Metadata Flow (Current)

```
VERSION ─────────────────────> release-automation-action reads current version
setup.py ────────────────────> release-automation-action bumps version (line 6)
pyproject.toml ──────────────> release-automation-action bumps version (line 7)
Adyen/settings.py ───────────> release-automation-action bumps version (line 2)

pip install . ───> reads pyproject.toml [project] (modern path)
                   OR setup.py (legacy path, but pyproject.toml takes precedence when both exist)

python -m build ─> reads pyproject.toml [build-system], then [project]

tox ─────────────> installs package (reads pyproject.toml via build backend)
                   then runs `make tests`
```

### Metadata Flow (After Consolidation)

```
VERSION ─────────────────────> release-automation-action reads current version
pyproject.toml ──────────────> release-automation-action bumps version (line 7)
Adyen/settings.py ───────────> release-automation-action bumps version (line 2)

setup.py (shim) ─────────────> delegates to setuptools, which reads pyproject.toml
                               (exists only for backward compat with very old pip)

pip install . ───> reads pyproject.toml [project] (sole source)
python -m build ─> reads pyproject.toml (sole source)
tox ─────────────> same as before, pyproject.toml is authoritative
```

### Key Discrepancies Between Current setup.py and pyproject.toml

| Field | setup.py | pyproject.toml | Notes |
|-------|----------|----------------|-------|
| `install_requires` / `dependencies` | `[]` (empty) | `["pydantic>=2.0"]` | **BUG** — the discrepancy that motivated this work |
| `long_description` | Hardcoded string | `readme = "README.md"` | pyproject.toml uses full README — an improvement |
| `url` | `"https://github.com/Adyen/adyen-python-api-library"` | Not present | Must add `[project.urls]` |
| Package discovery | `find_packages(include=["Adyen*"], exclude=["tests", "tests.*"])` | Not present | Must add `[tool.setuptools.packages.find]` |

---

## Open Questions

1. **`setup.cfg` cleanup**: The `[coverage:run]` section in `setup.cfg:11-14` duplicates `[tool.coverage.run]` in `pyproject.toml:80-81`. This is harmless but redundant. Not in scope per spec, but flagged for awareness.

2. **`coveralls` in Makefile**: The current `make install` installs `coveralls` which is not in any pyproject.toml extras group. If `make install` switches to extras-based install, `coveralls` would need to be added to a group or installed separately. Note: `coveralls` is not used in any CI workflow or test command visible in the repo — it may be vestigial.

3. **`wheel` in build-system.requires**: The current `requires = ["setuptools>=45", "wheel"]` includes `wheel`. Modern setuptools (≥61) does not need `wheel` in build-system.requires (it's handled internally). However, the spec does not call for removing it, so it should stay.
