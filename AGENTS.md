## Overview

This is the Adyen Python API Library, providing Python developers with an easy way to interact with the Adyen API. The library is a wrapper around the Adyen API, generated from OpenAPI specifications.

## Code Generation

A significant portion of this library, particularly the API services, is automatically generated.

- **Engine**: We use [OpenAPI Generator](https://openapi-generator.tech/) with custom [Mustache](https://mustache.github.io/) templates to convert Adyen's OpenAPI specifications into Python code.
- **Templates**: The custom templates are located in the `/templates` directory. These templates are tailored to fit our custom HTTP client and service structure.
- **Automation**:
    - **Centralized**: The primary generation process is managed in a separate repository, [`adyen-sdk-automation`](https://github.com/Adyen/adyen-sdk-automation). Changes to the OpenAPI specs trigger a GitHub workflow in that repository, which generates the code and opens Pull Requests in this library.
    - **Local**: For development and testing, you must use the [`adyen-sdk-automation`](https://github.com/Adyen/adyen-sdk-automation) repository.

### Local Code Generation

To test new features or changes to the templates, you must run the generation process from a local clone of the `adyen-sdk-automation` repository.

1.  **Clone the automation repository**:
    ```bash
    git clone https://github.com/Adyen/adyen-sdk-automation.git
    ```

2.  **Link this library**: The automation project needs to target your local clone of `adyen-python-api-library`. From inside the `adyen-sdk-automation` directory, run the following commands. This will replace the `python/repo` directory with a symlink to your local project. For example, if you cloned both repositories in the same parent directory:
    ```bash
    rm -rf python/repo
    ln -s ../adyen-python-api-library python/repo
    ```

3.  **Run the generator**: You can now run the Gradle commands to generate code.
    - **To generate all services for the Python library**:
      ```bash
      ./gradlew :python:services
      ```
    - **To generate a single service (e.g., Checkout)**:
      ```bash
      ./gradlew :python:checkout
      ```
    - **To clean the repository before generating**:
      ```bash
      ./gradlew :python:cleanRepo :python:checkout
      ```

## Core Components

- **`Adyen.Adyen`**: The main facade class in `Adyen/__init__.py` that provides easy access to all API services.
- **`Adyen.client.AdyenClient`**: The central class for configuring the library (API key, environment, etc.) and making API calls.
- **`Adyen.httpclient.HTTPClient`**: The underlying client responsible for making HTTP requests to the Adyen API.
- **`Adyen/services/`**: This package contains the generated service classes (e.g., `AdyenCheckoutApi`, `AdyenManagementApi`) that expose methods for specific API endpoints. Unlike some other Adyen libraries, this one does not use generated models for requests and responses; standard Python dictionaries are used instead.

## Development Workflow

This project uses `make` and `tox` to streamline development tasks.

### Setup

To install the library and its development dependencies, run:
```bash
make install
```

### Running Tests

You can run the unit tests using two main methods:

1.  **Directly via `make`**: For a quick run of the test suite in your current environment.
    ```bash
    make tests
    ```
    This command executes the tests using Python's built-in `unittest` module.

2.  **Via `tox`**: For comprehensive testing across multiple Python versions, as is done in the CI pipeline.
    ```bash
    tox
    ```
    This command uses the `tox.ini` configuration to create isolated environments and run tests in each, ensuring compatibility. This is the method used in our GitHub Actions workflow.

## Release Process

The release process is automated via GitHub Actions. When a release is triggered:
1.  A script determines the next version number (major, minor, or patch).
2.  The `VERSION` file and other configuration files are updated.
3.  A pull request is created with the version bump.
4.  Once merged, a GitHub release is created, and the new version is published to PyPI.
