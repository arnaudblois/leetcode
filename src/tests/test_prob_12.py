""" Tests for leetcode 012 - integer to Roman."""

from leetcode.prob_12_integer_to_roman import convert_to_roman


def test_convert_to_roman():
    """Test the conversion on a few numbers.

    Leetcode 13 codes the reverse function.
    We'll use it to test all integers in the range [1; 3999] there.
    """
    assert convert_to_roman(1) == "I"
    assert convert_to_roman(50) == "L"
    assert convert_to_roman(3) == "III"
    assert convert_to_roman(4) == "IV"
    assert convert_to_roman(7) == "VII"
    assert convert_to_roman(9) == "IX"
    assert convert_to_roman(12) == "XII"
    assert convert_to_roman(34) == "XXXIV"
    assert convert_to_roman(49) == "XLIX"
    assert convert_to_roman(284) == "CCLXXXIV"
