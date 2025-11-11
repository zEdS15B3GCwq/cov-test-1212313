"""Nox sessions for linting, testing, and documentation."""

import nox

# Define Python versions to test against
PYTHON_ALL_VERSIONS = ["3.12", "3.13", "3.14"]
PYTHON_MAIN_VERSION = "3.14"
PYTHON_OTHER_VERSIONS = list(set(PYTHON_ALL_VERSIONS) - set(PYTHON_MAIN_VERSION))

# Default sessions to run when no session is specified
nox.options.sessions = [
    "lint",
    "tests",
    "fmt_check",
    "tests_with_coverage",
    "type_check",
]
nox.options.default_venv_backend = "uv|virtualenv"
nox.options.download_python = "never"


@nox.session(python=PYTHON_OTHER_VERSIONS)
def tests(session):
    """Run the test suite with pytest."""
    session.install("-e", ".")
    session.install("pytest")
    session.run(
        "pytest",
        "tests/",
    )


@nox.session(python=PYTHON_MAIN_VERSION)
def tests_with_coverage(session):
    """Run the test suite with pytest and coverage."""
    session.install("-e", ".")
    session.install("pytest", "pytest-cov")
    session.run(
        "pytest",
        "--cov=testmodule",
        "--cov-report=term-missing",
        "--cov-report=html",
        "--cov-report=xml",
        "tests/",
    )


@nox.session(python=PYTHON_MAIN_VERSION)
def lint(session):
    """Run ruff linter."""
    session.install("ruff")
    session.run("ruff", "check", ".")


@nox.session(python=PYTHON_MAIN_VERSION)
def fmt_check(session):
    """Check code formatting with ruff."""
    session.install("ruff")
    session.run("ruff", "format", "--check", ".")


@nox.session(python=PYTHON_MAIN_VERSION)
def fmt(session):
    """Format code with ruff."""
    session.install("ruff")
    session.run("ruff", "format", ".")


@nox.session(python=PYTHON_MAIN_VERSION)
def docs(session):
    """Build the documentation with Sphinx."""
    session.install("-e", ".")
    session.install("sphinx", "sphinx-rtd-theme", "myst-parser")
    session.run("sphinx-build", "-b", "html", "docs", "docs/_build/html")


@nox.session(python=PYTHON_MAIN_VERSION)
def docs_clean(session):
    """Clean the documentation build directory."""
    import shutil
    from pathlib import Path

    build_dir = Path("docs/_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)
        session.log("Cleaned documentation build directory")
    else:
        session.log("Documentation build directory does not exist")


@nox.session(python=PYTHON_MAIN_VERSION)
def type_check(session):
    """Run type checking with mypy."""
    session.install("-e", ".")
    session.install("mypy")
    session.run("mypy", "testmodule", "tests")
