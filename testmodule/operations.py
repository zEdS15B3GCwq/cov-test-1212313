"""Operations module containing mathematical functions."""


def add2(number: int | float) -> int | float:
    """Add 2 to a given number.

    Args:
        number: The number to add 2 to.

    Returns:
        The result of adding 2 to the input number.

    Examples:
        >>> add2(5)
        7
        >>> add2(3.5)
        5.5
    """
    return number + 2
