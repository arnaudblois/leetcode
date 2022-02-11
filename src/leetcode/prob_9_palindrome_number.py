"""Leetcode 009 - Palindrome number.

Check if a number is a palindrome, e.g. 1234321 is one,
-1234321 is not (1234321- is invalid), neither is 10.
"""


def is_palindrome(number: int) -> bool:
    """Check if number is palindromic."""
    return str(number) == str(number)[::-1]
