"""Leetcode 007 - Reverse integer

Reverse the digits of an integer, if it lies outside the bounds of an Integer
of 32 bits, return 0.
"""


def reverse_int(integer: int) -> int:
    """Reverse an integer."""
    reversed_int = int(str(abs(integer))[::-1])
    if integer < 0:
        reversed_int *= -1
    return reversed_int if -(2**31) < reversed_int < 2**31 - 1 else 0
