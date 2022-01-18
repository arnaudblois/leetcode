"""Tests for LeetCode 003 - Longest substring without repeating characters."""

from leetcode.prob_3_longest_substring_without_repeating_characters import (
    longest_no_repeat,
)


def test_longest_no_repeat():
    """Test a variety of strings."""
    assert longest_no_repeat("abcabcbb") == 3
    assert longest_no_repeat("abcabcbb") == 3
    assert longest_no_repeat("b") == 1
    assert longest_no_repeat("pwwkew") == 3
    assert longest_no_repeat("") == 0
