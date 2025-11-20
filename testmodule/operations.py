"""
Operations module containing mathematical functions.

This module provides basic mathematical operations, such as adding a constant to numbers.
"""


def add2(number: int | float) -> int | float:
    """
    Add 2 to a given number.

    Parameters
    ----------
    number : int or float
        The number to add 2 to.

    Returns
    -------
    int or float
        The result of adding 2 to the input number.

    Examples
    --------
    >>> add2(5)
    7
    >>> add2(3.5)
    5.5
    """
    return number + 2
