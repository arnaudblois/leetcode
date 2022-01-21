"""Leetcode 008 - String to integer atoi function.

Extract an integer, positive or negative, appearing as first element of a
string. Clamp the result to 32 bit results if the int is out of bounds.
"""

import re

NUM_REGEX = re.compile(r"^[-+]?\d+")


def atoi(string: str) -> int:
    """Extract leading int and clamp it to 32bit int if required."""
    try:
        num = int(NUM_REGEX.search(string.strip()).group(0))
    except AttributeError:
        return 0
    num = max(-(2 ** 31), num)
    num = min(2 ** 31 - 1, num)
    return num
