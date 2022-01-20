""" Tests for leetcode 007 - Reverse integer."""

from leetcode.prob_7_reverse_integer import reverse_int


def test_zigzag_conversion():
    """Test zigzag conversion for various input."""
    assert reverse_int(1234) == 4321
    assert reverse_int(0) == 0
    assert reverse_int(-4321) == -1234
    assert reverse_int(2147483647) == 0
    assert reverse_int(-2147483648) == 0
