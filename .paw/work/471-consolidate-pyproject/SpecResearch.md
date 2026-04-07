# Spec Research: Consolidate Pyproject Metadata

## 1. Python Packaging Standards

### PEP 621 — `[project]` Table Fields

PEP 621 standardises project metadata in `pyproject.toml`. The only **required** field is `name`. Key available fields:

| Field | Type | Notes |
|---|---|---|
| `name` | string | **Required** |
| `version` | string | Static, or declared `dynamic` |
| `description` | string | One-line summary |
| `readme` | string / table | Path to README; setuptools auto-sets `long_description` and `long_description_content_type` |
| `requires-python` | string | e.g. `">=3.8"` |
| `license` | SPDX / table | e.g. `{text = "MIT"}` or SPDX expression |
| `authors` | list of tables | `[{name = "...", email = "..."}]` |
| `maintainers` | list of tables | Same structure |
| `keywords` | list of strings | |
| `classifiers` | list of strings | Trove classifiers |
| `urls` | table | `[project.urls]` section |
| `dependencies` | list of strings | PEP 508 format |
| `optional-dependencies` | table of lists | `[project.optional-dependencies]` |
| `dynamic` | list of strings | Fields resolved at build time |

### setuptools ≥ 61.0.0 Behaviour

- **First version** of setuptools to read PEP 621 `[project]` metadata from `pyproject.toml`.
- When both `setup.py` and `pyproject.toml` define metadata, **`pyproject.toml` takes precedence** for fields defined in `[project]`. Any remaining setup.py kwargs are merged in.
- With a **minimal shim** (`from setuptools import setup; setup()`), setuptools will read all metadata from `pyproject.toml`. The shim adds no conflicting metadata.

### `[tool.setuptools.packages.find]` Syntax

```toml
[tool.setuptools.packages.find]
include = ["Adyen*"]          # glob patterns (NOT regex)
exclude = ["test*", "tests*"] # glob patterns
```

- `where` (default `["."]`): directories to search.
- `include`: if set, **only** packages matching these globs are included.
- `exclude`: packages matching these globs are excluded from the result.
- `namespaces` (default `true`): set `false` to require `__init__.py`.

### `readme` Field Behaviour

When `readme = "README.md"` is in `[project]`:
- setuptools sets `long_description` from the file content.
- `long_description_content_type` is auto-detected from the file extension (`.md` → `text/markdown`).
- This **replaces** the current `setup.py` hardcoded string `"A Python client library for accessing Adyen APIs"` with the full README content — **an improvement**.

### Minimal `setup.py` Shim Compatibility

- **pip ≥ 21.3 + setuptools ≥ 64**: PEP 660 editable installs (`pip install -e .`) work **without any setup.py**.
- **Older pip**: a `setup.py` shim (`from setuptools import setup; setup()`) is needed for `pip install -e .`.
- The shim pattern is **explicitly recommended** by the [Python Packaging Authority migration guide](https://packaging.python.org/en/latest/guides/modernize-setup-py-project/).
- Keeping the shim ensures compatibility with legacy environments, CI/CD tools, and the `adyen-sdk-automation` build system.

### Edge Case: Editable Installs

With `setuptools>=61.0` specified in `build-system.requires`:
- `pip install -e .` works with `pyproject.toml`-only metadata + a minimal shim.
- The `[tool.setuptools.packages.find]` section ensures correct package discovery during editable installs.
- The `lint.yml` workflow already uses `pip install -e ".[dev]"` — this will continue to work.

---

## 2. Current Codebase State

### `setup.py` — Current State

```python
from setuptools import find_packages, setup

setup(
    name="Adyen",
    packages=find_packages(include=["Adyen*"], exclude=["tests", "tests.*"]),
    version="15.0.0",
    maintainer="Adyen",
    maintainer_email="support@adyen.com",
    description="Adyen Python Api",
    long_description="A Python client library for accessing Adyen APIs",
    author="Adyen",
    author_email="support@adyen.com",
    url="https://github.com/Adyen/adyen-python-api-library",
    keywords=["payments", "adyen", "fintech"],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "requests": ["requests>=2.25.0"],
        "pycurl": ["pycurl>=7.43.0"],
        "test": ["pytest>=7.0.0", "pytest-cov>=4.0.0", "mock>=4.0.0", "requests>=2.25.0"],
        "dev": ["ruff>=0.4.4", "pre-commit>=3.0.0"],
    },
    classifiers=[...],
)
```

**Key observations:**
- `install_requires=[]` — **empty**. Missing `pydantic>=2.0` which IS in `pyproject.toml`. This is the bug described in issue #471 (fixed in PR #468 for `pyproject.toml` only).
- `long_description` is a static string, not README content.
- `url` is defined but no `project_urls` dict (which maps to `[project.urls]`).
- `find_packages(include=["Adyen*"], exclude=["tests", "tests.*"])` — note exclude uses `"tests"` and `"tests.*"` but the actual test directory is named `test` (singular).

**What gets removed:** Everything except `from setuptools import setup; setup()`.

### `pyproject.toml` — Current State

```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "Adyen"
version = "15.0.0"
description = "Adyen Python Api"
readme = "README.md"
requires-python = ">=3.8"
authors = [{name = "Adyen", email = "support@adyen.com"}]
maintainers = [{name = "Adyen", email = "support@adyen.com"}]
keywords = ["payments", "adyen", "fintech"]
dependencies = ["pydantic>=2.0"]
classifiers = [...]

[project.optional-dependencies]
requests = ["requests>=2.25.0"]
pycurl = ["pycurl>=7.43.0"]
test = ["pytest>=7.0.0", "pytest-cov>=4.0.0", "mock>=4.0.0", "requests>=2.25.0"]
dev = ["ruff>=0.4.4", "pre-commit>=3.0.0"]

[tool.ruff]
...

[tool.coverage.run]
source = ["Adyen/"]
```

**What's already there:** Most metadata is already present and correct.

**What needs adding/changing:**
1. `build-system.requires` → bump from `"setuptools>=45"` to `"setuptools>=61.0.0"`
2. Add `[tool.setuptools.packages.find]` section
3. Add `[project.urls]` section
4. Optionally remove `"wheel"` from `build-system.requires` (modern pip/setuptools include it automatically, but keeping it is harmless)

### `setup.cfg` — Current State (Out of Scope)

```ini
[bdist_wheel]

[metadata]
description_file = README.md

[egg_info]
tag_build =
tag_date = 0
tag_svn_revision = 0

[coverage:run]
source =
    Adyen/
```

**Awareness notes:**
- The `[metadata] description_file` is a legacy setuptools-specific field. With `readme = "README.md"` in `pyproject.toml`, this becomes redundant but harmless.
- The `[coverage:run]` section duplicates `[tool.coverage.run]` in `pyproject.toml`. Out of scope but noted.
- Not modifying this file per the work shaping decision.

### `Makefile` — Current Install Target

```makefile
install:
	@pip install requests pycurl mock coveralls ruff
```

**Issues:**
- Hardcodes individual package names instead of using the project's dependency groups.
- Doesn't install the project itself.
- Doesn't use `pyproject.toml`-defined extras.
- Includes `coveralls` which isn't in any extras group.

**Proposed replacement:**
```makefile
install:
	@pip install -e ".[requests,test,dev]"
```

This:
- Installs the project in editable mode
- Pulls in `requests`, `test`, and `dev` extras from `pyproject.toml`
- Does NOT include `pycurl` (requires system-level `libcurl` — handled by tox separately)
- Does NOT include `coveralls` (not in any extras; consider adding to `test` extras or keeping separate)

### `Adyen/settings.py` — Runtime Version (Out of Scope)

```python
LIB_NAME = "adyen-python-api-library"
LIB_VERSION = "15.0.0"
```

Used by `Adyen/client.py` for:
- HTTP headers: `adyen-library-name` and `adyen-library-version`
- User-Agent suffix
- These are **runtime values** sent to Adyen APIs, not packaging metadata.
- The release-automation-action bumps this file via the perl regex substitution.
- Out of scope per work shaping decision.

### `VERSION` File — Current Content (Out of Scope)

```
15.0.0
```

- The release-automation-action reads this via `cat VERSION` to get the current version.
- Used as the source of truth for the release automation.
- Out of scope per work shaping decision.

### `.github/workflows/release.yml`

```yaml
- name: Bump
  run: |
    perl -i -pe 's/${{steps.current-version.outputs.current-version}}/${{steps.release.outputs.next-version}}/' VERSION ${{ inputs.version-files }}
```

With `version-files: setup.py pyproject.toml Adyen/settings.py`:
- The perl command does a **literal string substitution** of the old version with the new version across all listed files.
- For `setup.py`, it currently matches `version="15.0.0"` on line 6.
- **After our change**, `setup.py` will be `from setuptools import setup\nsetup()` — **no version string present**. The perl command will simply not match anything in `setup.py`, which is harmless (perl `s///` with no match is a no-op).
- However, keeping `setup.py` in `version-files` is misleading. It should be **removed** from `version-files`.

**⚠️ REQUIRED CHANGE:** `version-files` line must be updated to remove `setup.py`:
```yaml
version-files: pyproject.toml Adyen/settings.py
```

### `.github/workflows/pypipublish.yml`

```yaml
- name: Install pypa/build
  run: python -m pip install build --user
- name: Build a binary wheel and a source tarball
  run: python -m build --sdist --wheel --outdir dist/ .
```

- Uses `python -m build` which reads `pyproject.toml` for metadata.
- **No changes needed.** This workflow already works with `pyproject.toml` as the metadata source.

### `.github/workflows/python-ci.yml`

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install tox
    sudo apt-get update
    sudo apt install libcurl4-openssl-dev
- name: Test with tox
  run: tox
```

- Installs `tox` and runs tests. Does not reference `setup.py` directly.
- **No changes needed.**

### `.github/workflows/lint.yml`

```yaml
key: ${{ runner.os }}-pip-${{ hashFiles('**/setup.py') }}
```

- Uses `hashFiles('**/setup.py')` for pip cache key.
- **⚠️ SHOULD UPDATE** to `hashFiles('**/pyproject.toml')` since `pyproject.toml` is now the source of truth for dependencies. After our change, `setup.py` will never change (it's a static shim), making it useless as a cache key.

Also in `lint.yml`:
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -e ".[dev]"
```

- Already uses `pip install -e ".[dev]"` — this works perfectly with pyproject.toml extras. **No changes needed** for this part.

### `tox.ini`

```ini
[testenv]
deps =
    mock
    requests: requests
    pycurl: pycurl
commands =
    make tests
```

- Does **not** use extras from pyproject.toml — installs deps directly.
- **No changes proposed** in this issue. Could be a future improvement to use `pip install .[test,requests]` etc.

---

## 3. Risk Analysis

### 3.1 Release Automation — `version-files` with Minimal setup.py

**Mechanism:** The `Adyen/release-automation-action@v1.4.0` (pinned to SHA `3e5694d...`):
1. Reads current version from `cat VERSION`
2. Computes next version from PR labels
3. Runs: `perl -i -pe 's/OLD_VERSION/NEW_VERSION/' VERSION ${{ inputs.version-files }}`
4. Creates a PR with the bumped files

**Risk assessment:**
- If `setup.py` contains only `from setuptools import setup\nsetup()`, the perl regex `s/15.0.0/16.0.0/` will find **no match** — this is a **no-op**, not an error. Perl `s///` with no match simply leaves the file unchanged.
- **Impact: NONE functionally**, but the file will be needlessly processed.
- **Recommendation:** Remove `setup.py` from `version-files` in `release.yml` to keep the workflow clean and avoid confusion.
- **Updated line:** `version-files: pyproject.toml Adyen/settings.py`

### 3.2 SDK Automation (Code Generation)

**Finding:** The `adyen-sdk-automation` repo's `python/build.gradle.kts` does **NOT** generate or modify `setup.py`. It only:
- Generates service files into `repo/Adyen/services/<serviceName>/`
- Copies `__init__.py` files for services
- Uses mustache templates for API classes only

The local `Makefile` generator section (lines 20-101) also only generates into `Adyen/services/` — no `setup.py` involvement.

**Templates directory** (`templates/`): Contains only API mustache templates (`api-single.mustache`, `api-small.mustache`, etc.) and `config.yaml`. **No setup.py template exists.**

**Risk: NONE.** The code generation process is completely independent of packaging metadata.

### 3.3 Files Referencing setup.py

| File | Reference | Impact |
|---|---|---|
| `.github/workflows/release.yml:38` | `version-files: setup.py pyproject.toml Adyen/settings.py` | Must remove `setup.py` |
| `.github/workflows/lint.yml:30` | `hashFiles('**/setup.py')` | Should update to `hashFiles('**/pyproject.toml')` |
| `setup.py` itself | `from setuptools import find_packages, setup` | Simplify to `from setuptools import setup; setup()` |

No other files import from or reference `setup.py`.

### 3.4 Dependency Discrepancy

**Current state:**
- `pyproject.toml` has `dependencies = ["pydantic>=2.0"]`
- `setup.py` has `install_requires=[]` (empty!)

**After consolidation:** `pyproject.toml` is authoritative. The empty `install_requires` in the shim `setup.py` is harmless because modern setuptools reads `dependencies` from `[project]` and does **not merge** `install_requires` from `setup()` when `[project].dependencies` is defined.

**Risk: NONE after consolidation.** Actually resolves the discrepancy.

### 3.5 Package Discovery

**Current `setup.py`:** `find_packages(include=["Adyen*"], exclude=["tests", "tests.*"])`
- Note: The exclude pattern says `"tests"` (plural) but the actual directory is `test` (singular). The exclude pattern was **never matching** the real test directory anyway.
- The `include=["Adyen*"]` pattern is the effective filter.

**Proposed `pyproject.toml`:**
```toml
[tool.setuptools.packages.find]
include = ["Adyen*"]
exclude = ["test*"]
```

The `test` directory has a `__init__.py`, making it a discoverable package. But `include = ["Adyen*"]` alone is sufficient to exclude it, since `test` doesn't match `Adyen*`. Adding `exclude = ["test*"]` is a belt-and-suspenders approach.

### 3.6 Version Synchronisation Across Files

After this change, version appears in these files (all still bumped by the release action):
- `VERSION` — source of truth for release action (`cat VERSION`)
- `pyproject.toml` — `version = "15.0.0"` in `[project]`
- `Adyen/settings.py` — `LIB_VERSION = "15.0.0"` for runtime headers

The `setup.py` shim will **no longer contain a version string**, which is correct because `pyproject.toml` is the authoritative source.

---

## 4. Ecosystem Patterns

### Other Adyen Libraries

A GitHub code search for `pyproject.toml` + `[tool.setuptools.packages.find]` or `[project.urls]` across the Adyen org returned **no results**. This Python library appears to be the **first Adyen SDK** to adopt PEP 621 consolidation.

The `release-automation-action` is used across multiple Adyen repos but its `version-files` input is always a space-separated list of files — the action is agnostic to file format and uses simple string replacement.

### Industry Standard

The pattern of `pyproject.toml` as single source of truth with a minimal `setup.py` shim is **widely adopted** in the Python ecosystem:
- The Python Packaging Authority has an [official migration guide](https://packaging.python.org/en/latest/guides/modernize-setup-py-project/)
- Major projects (Django, Flask, requests, etc.) have migrated or are migrating
- `setuptools>=61.0` has been available since March 2022 — well-established

---

## 5. Key Findings & Recommendations

### Critical Actions (Must Do)

1. **Simplify `setup.py`** to `from setuptools import setup; setup()` — removes all duplicate metadata.

2. **Add `[tool.setuptools.packages.find]`** to `pyproject.toml`:
   ```toml
   [tool.setuptools.packages.find]
   include = ["Adyen*"]
   exclude = ["test*"]
   ```

3. **Bump `build-system.requires`** from `"setuptools>=45"` to `"setuptools>=61.0.0"`.

4. **Add `[project.urls]`**:
   ```toml
   [project.urls]
   Homepage = "https://github.com/Adyen/adyen-python-api-library"
   Repository = "https://github.com/Adyen/adyen-python-api-library"
   Issues = "https://github.com/Adyen/adyen-python-api-library/issues"
   ```

5. **Update `Makefile` install target**:
   ```makefile
   install:
   	@pip install -e ".[requests,test,dev]"
   ```

6. **Update `release.yml`** — remove `setup.py` from `version-files`:
   ```yaml
   version-files: pyproject.toml Adyen/settings.py
   ```

7. **Update `lint.yml`** — change cache key from `hashFiles('**/setup.py')` to `hashFiles('**/pyproject.toml')`.

### Findings That Align with Work Shaping

- All shaping decisions are sound and feasible.
- The minimal shim approach is the recommended Python packaging migration pattern.
- No contradictions found with any shaping decision.

### Additional Findings (Not Contradictions, but Worth Noting)

1. **`setup.cfg` redundancy:** The `[metadata] description_file = README.md` and `[coverage:run]` sections duplicate what's in `pyproject.toml`. Out of scope per shaping, but worth a follow-up issue.

2. **`install_requires` bug was real:** `setup.py` had `install_requires=[]` while `pyproject.toml` had `dependencies = ["pydantic>=2.0"]`. The consolidation fully resolves this class of bug.

3. **Existing `setup.py` exclude pattern was wrong:** `exclude=["tests", "tests.*"]` never matched the `test/` directory. The new `pyproject.toml` config with `include = ["Adyen*"]` is more correct.

4. **`coveralls` in old Makefile:** The current `Makefile` installs `coveralls` but it's not in any extras group. The new install target drops it. If coverage upload is needed, it should be added to `test` extras in a follow-up.

5. **`wheel` in build-system.requires:** `"wheel"` can optionally be removed from `build-system.requires` since modern pip (≥21.0) includes it. However, keeping it is harmless and improves compatibility. **Recommendation: keep it.**

6. **tox.ini doesn't use extras:** The `tox.ini` installs deps manually rather than via `pip install .[test]`. This is out of scope but could be a future improvement.
