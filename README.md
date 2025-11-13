# cov-test-1212313

[![Tests](https://github.com/zEdS15B3GCwq/cov-test-1212313/actions/workflows/ci.yml/badge.svg)](https://github.com/zEdS15B3GCwq/cov-test-1212313/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/endpoint?url=https://zEdS15B3GCwq.github.io/cov-test-1212313/badges/coverage.json)](https://zEdS15B3GCwq.github.io/cov-test-1212313/htmlcov/)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://zEdS15B3GCwq.github.io/cov-test-1212313/)

Testing GitHub workflow & codecov badge generation.

## Overview

This is a test project to learn how to set up CI workflow with coverage report,
documentation and test passing badges, and publishing results on Github Pages.

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
