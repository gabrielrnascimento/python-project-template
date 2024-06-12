# Python Project Template

Generic Python template for new projects.

## Technologies

- **Pylint**: A static code analyzer that helps enforce a coding standard and find programming errors, helping to maintain code quality.
- **Black**: An uncompromising code formatter that ensures code consistency by automatically formatting Python code to conform to the PEP 8 style guide.
- **MyPy**: A static type checker that checks the type annotations in your Python code, helping catch type-related errors early in the development process.
- **Pytest**: A powerful testing framework that makes it easy to write simple and scalable test cases, facilitating robust test coverage and quick feedback on code changes.
- **Pre-commit**: A framework for managing and maintaining multi-language pre-commit hooks, ensuring that code quality checks are performed automatically before every commit.
- **editorconfig**: A configuration file that helps maintain consistent coding styles across different editors and IDEs.

## Setup

1. `git clone` this repository.
2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install the pre-commit hooks:

    ```bash
    pre-commit install
    ```

## Scripts

- **Lint**: Run Pylint to check for code quality issues:

    ```bash
    pylint src/
    ```

- **Format**: Run Black to format the code according to the PEP 8 style guide:

    ```bash
    black src/
    ```

- **Type Check**: Run MyPy to check for type-related errors:

    ```bash
    mypy src/
    ```

- **Test**: Run Pytest to execute the test cases:

    ```bash
    pytest
    ```
