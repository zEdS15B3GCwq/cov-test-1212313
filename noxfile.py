"""Nox sessions for linting, testing, and documentation."""

import nox

# Define Python versions to test against
PYTHON_VERSIONS = ["3.12", "3.13", "3.14"]

# Default sessions to run when no session is specified
nox.options.sessions = ["lint", "tests", "fmt_check"]


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run the test suite with pytest and coverage."""
    session.install("-e", ".[dev]")
    session.run(
        "pytest",
        "--cov=testmodule",
        "--cov-report=term-missing",
        "--cov-report=html",
        "--cov-report=xml",
        "tests/",
    )


@nox.session(python="3.14")
def lint(session):
    """Run ruff linter."""
    session.install("ruff")
    session.run("ruff", "check", ".")


@nox.session(python="3.14")
def fmt_check(session):
    """Check code formatting with ruff."""
    session.install("ruff")
    session.run("ruff", "format", "--check", ".")


@nox.session(python="3.14")
def fmt(session):
    """Format code with ruff."""
    session.install("ruff")
    session.run("ruff", "format", ".")


@nox.session(python="3.14")
def docs(session):
    """Build the documentation with Sphinx."""
    session.install("-e", ".[dev]")
    session.install("myst-parser")
    session.run("sphinx-build", "-b", "html", "docs", "docs/_build/html")


@nox.session(python="3.14")
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
