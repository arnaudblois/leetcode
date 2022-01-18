"""LeetCode 002 - Add two numbers

We are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain
a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8
"""
from leetcode.structures import ListNode


def add_nodes(num1: ListNode, num2: ListNode, carry: int = 0) -> tuple[int, int]:
    """Add two nodes representing single digits.

    Return a tuple: value for the added digit, potential carry
    """
    num1 = num1.val if num1 else 0
    num2 = num2.val if num2 else 0
    total = num1 + num2 + carry
    return total % 10, total // 10


def add_two_numbers(num1: ListNode, num2: ListNode) -> ListNode:
    """Add two numbers represented as linked lists."""
    val, carry = add_nodes(num1, num2, 0)
    result = current = ListNode(val)
    num1 = num1.next if num1 else None
    num2 = num2.next if num2 else None

    while num1 or num2 or carry:
        val, carry = add_nodes(num1, num2, carry)
        current.next = ListNode(val)
        num1 = num1.next if num1 else None
        num2 = num2.next if num2 else None
        current = current.next
    return result
