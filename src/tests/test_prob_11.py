""" Tests for leetcode 011 - Container with most water."""

from leetcode.prob_11_container_most_water import (
    find_max_water,
    find_max_water_brute_force,
)


def test_empty():
    """Check that no height is zero."""
    find_max_water([]) == 0
    find_max_water_brute_force([]) == 0


def test_only_one_height():
    """Test output when there is only one height."""
    find_max_water([42]) == 0
    find_max_water_brute_force([42]) == 0


def test_only_two_heights():
    """Check trivial answer with only one height."""
    find_max_water([42, 42]) == 42
    find_max_water_brute_force([42, 42]) == 42


def test_profile_1():
    """Test a first profile."""
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    find_max_water(heights) == 49
    find_max_water_brute_force(heights) == 49


def test_profile_2():
    """Test another profile"""
    heights = [1, 4, 2, 3, 5, 2, 3]
    find_max_water(heights) == 12
    find_max_water_brute_force(heights) == 12
