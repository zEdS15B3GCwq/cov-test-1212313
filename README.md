# cov-test-1212313

[![Push and PR tests status](https://github.com/zEdS15B3GCwq/cov-test-1212313/actions/workflows/ci.yml/badge.svg)](https://github.com/zEdS15B3GCwq/cov-test-1212313/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/zEdS15B3GCwq/cov-test-1212313/main.svg)](https://results.pre-commit.ci/latest/github/zEdS15B3GCwq/cov-test-1212313/main)
[![coverage status](https://img.shields.io/endpoint?url=https://zEdS15B3GCwq.github.io/cov-test-1212313/badges/coverage.json)](https://zEdS15B3GCwq.github.io/cov-test-1212313/htmlcov/)
[![docs location](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://zEdS15B3GCwq.github.io/cov-test-1212313/)
[![python support](https://img.shields.io/badge/Python-3.12%20%7C%203.13%20%7C%203.14-blue?logo=python)](https://www.python.org/)
[![CodeQL](https://github.com/zEdS15B3GCwq/cov-test-1212313/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/zEdS15B3GCwq/cov-test-1212313/actions/workflows/github-code-scanning/codeql)

Testing GitHub workflow & codecov badge generation.

## Overview

This is a test project to learn how to set up CI workflow with coverage report,
documentation and test passing badges, and publishing results on Github Pages,
using pre-commit.ci and other CI tools, publishing to (test)PyPI etc.

The rest is AI slop.

This is a simple Python package that provides basic mathematical operations.
Currently, it includes an `add2()` function that adds 2 to any given number.

## Installation

```bash
pip install -e .
```

For development dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

```python
from testmodule import add2

result = add2(5)
print(result)  # Output: 7
```

## Development

This project uses:

- **pytest** for testing
- **ruff** for linting
- **sphinx** for documentation
- **nox** for task automation

### Running Tests

```bash
# Run tests with coverage for all Python versions
nox -s tests

# Or directly with pytest
pytest --cov=testmodule
```

### Linting

```bash
# Run ruff linting
nox -s lint

# Or directly with ruff
ruff check .
```

### Building Documentation

```bash
# Build documentation
nox -s docs

# Documentation will be in docs/_build/html/
```

## License

This project is licensed under the MIT License - see the LICENSE file for
details.
