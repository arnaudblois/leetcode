""" Tests for leetcode 008 - String to integer atoi."""

from leetcode.prob_8_string_to_integer_atoi import atoi


def test_atoi():
    """Test different inputs for aoi function."""
    assert atoi("42") == 42
    assert atoi("+42") == 42
    assert atoi("     -42") == -42
    assert atoi(" invalid leading with text   -42 string     ") == 0
    assert atoi("Invalid string no integer anywhere") == 0
    assert atoi(" -42 in a string") == -42
    assert atoi("    42 in a string") == 42
    assert atoi(" 999999999999 s") == 2**31 - 1
    assert atoi(" -999999999999 s") == -(2**31)
