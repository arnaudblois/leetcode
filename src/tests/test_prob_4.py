"""Tests for LeetCode 004 - Finding the median of two sorted arrays."""

from leetcode.prob_4_median_of_two_sorted_arrays import (
    find_median,
    find_median_simpler_bit_less_efficient,
)


def test_median_even():
    """Test the median for even number of items."""
    list_1 = [0, 1, 2, 3, 4, 5, 6]
    list_2 = [7, 8, 9]
    assert (
        find_median(list_1, list_2)
        == find_median_simpler_bit_less_efficient(list_1, list_2)
        == 4.5
    )


def test_median_odd():
    """Test the median for odd number of items."""
    list_1 = [0, 1, 2, 3, 4, 5, 6]
    list_2 = [7, 8]
    assert (
        find_median(list_1, list_2)
        == find_median_simpler_bit_less_efficient(list_1, list_2)
        == 4
    )


def test_median_one_empty():
    """Test with one list empty."""
    list_1 = [2, 4, 6, 8, 10]
    list_2 = []
    assert (
        find_median(list_1, list_2)
        == find_median_simpler_bit_less_efficient(list_1, list_2)
        == 6
    )
