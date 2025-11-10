"""Unit tests for testmodule."""

import pytest
from testmodule import add2


def test_add2_positive():
    """Test add2 with positive integer."""
    assert add2(5) == 7


def test_add2_negative():
    """Test add2 with negative integer."""
    assert add2(-3) == -1


def test_add2_zero():
    """Test add2 with zero."""
    assert add2(0) == 2


def test_add2_float():
    """Test add2 with float."""
    assert add2(3.5) == 5.5


def test_add2_large_number():
    """Test add2 with large number."""
    assert add2(1000000) == 1000002
