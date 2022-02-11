""" Tests for leetcode 009 - Palindrome number."""

from leetcode.prob_9_palindrome_number import is_palindrome


def test_is_palindrome():
    """Test different inputs for aoi function."""
    assert is_palindrome(121)
    assert is_palindrome(0)
    assert is_palindrome(7)
    assert is_palindrome(22)
    assert is_palindrome(12321)
    assert not is_palindrome(42)
    assert not is_palindrome(-12321)
