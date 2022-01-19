""" Tests for leetcode 005 - longest palindromic substring."""

from leetcode.prob_5_longest_palindromic_substring import (
    expand_from_middle,
    find_longest_palindromic_substring,
)


def test_expand_from_middle():
    """Test for the helper function."""
    assert expand_from_middle("abcba", 2, 2) == "abcba"
    assert expand_from_middle("abccba", 2, 3) == "abccba"


def check_string(string, palindrome):
    assert find_longest_palindromic_substring(string) == palindrome


def test_longest_palindromic_substring():
    """Test for main function against various input"""
    check_string("", "")
    check_string("aa", "aa")
    check_string("aaba", "aba")
    check_string("aaba", "aba")
    check_string("abbbbabbab", "abbbba")
    check_string("abbbbbabbab", "abbbbba")
    # Trivia Time
    # The longest single word palindrome is a Finnish word meaning a lye dealer.
    check_string("saippuakivikauppias", "saippuakivikauppias")
    # The longest single word palindrome in English is
    check_string("detartrated", "detartrated")
