"""Tests for Leetcode 1 - two sums."""

from leetcode.prob_1_two_sums import two_sum, two_sum_brute


def test_two_sum_1():
    """Test the optimal function."""
    assert set(two_sum(nums=[2, 7, 11, 15], target=9)) == set([0, 1])
    assert set(two_sum(nums=[3, 2, 4], target=6)) == set([1, 2])
    assert set(two_sum(nums=[3, 3], target=6)) == set([0, 1])
    assert two_sum(nums=[], target=6) == []


def test_two_sum_2():
    """Test the brute-force solution for consistency."""
    assert set(two_sum_brute(nums=[2, 7, 11, 15], target=9)) == set([0, 1])
    assert set(two_sum_brute(nums=[3, 2, 4], target=6)) == set([1, 2])
    assert set(two_sum(nums=[3, 3], target=6)) == set([0, 1])
    assert two_sum_brute(nums=[], target=6) == []
