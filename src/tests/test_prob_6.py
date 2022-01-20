""" Tests for leetcode 006 - Zigzag Conversion"""

from leetcode.prob_6_conversion_zigzag import convert_zigzag


def test_zigzag_conversion():
    """Test zigzag conversion for various input."""
    assert convert_zigzag("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert_zigzag("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert_zigzag("A", 10) == "A"
    assert convert_zigzag("AB", 1) == "AB"
    assert convert_zigzag("", 42) == ""
    assert convert_zigzag("STRING", 42) == "STRING"
    assert convert_zigzag("MyExampleString", 4) == "MpiymlrnEaetgxS"
