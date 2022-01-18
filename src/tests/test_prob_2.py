"""Tests for Leetcode 2 - Add two numbers."""

from leetcode.prob_2_add_two_numbers import add_two_numbers
from leetcode.structures import ListNode


def test_1():
    """Test 243 + 564 = 708."""
    num_1 = ListNode(2, ListNode(4, ListNode(3)))
    num_2 = ListNode(5, ListNode(6, ListNode(4)))
    assert add_two_numbers(num_1, num_2) == ListNode(7, ListNode(0, ListNode(8)))


def test_2():
    """Test empties."""
    num_1 = ListNode()
    num_2 = ListNode()
    assert add_two_numbers(num_1, num_2) == ListNode()


def test_3():
    """Test number requiring carry."""
    num_1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    num_2 = ListNode(9, ListNode(9))
    result = add_two_numbers(num_1, num_2)
    expected = ListNode(8, ListNode(9, ListNode(0, ListNode(0, ListNode(1)))))
    assert result == expected
