"""Leetcode 005 - Finding the longest palindrome substring.

A brute force approach,testing every possible substring, runs in O(n³).
It is possible to run in time complexity O(n²) / space complexity O(n²)
by using dynamic programming.

Here we implement an even simpler alternative, based on the fact palindromes
expand from their middle.

There exists even more advanced algorithms, able to resolve this in linear time,
using a suffix tree or Manachar's algorithm.
"""


def expand_from_middle(string: str, left: int, right: int) -> str:
    """Return the longest palindrome centred around the indices left and right.

    left == right for palindrome of odd length
    left == right + 1 for even length
    """
    max_palindrome = ""
    while left >= 0 and right < len(string) and string[left] == string[right]:
        max_palindrome = string[left : right + 1]
        left -= 1
        right += 1
    return max_palindrome


def find_longest_palindromic_substring(string: str) -> str:
    """Return the longest palindromic substring.

    This algorithm is in O(n²) with space complexity O(1). Unlike the brute
    force approach it uses the fact that palindromes can only propagate from a
    centrepoint of which there are only 2*n - 1 in a string.
    """
    n = len(string)
    if n == 0:
        return ""
    max_palindrome = string[0]
    for i in range(n):
        # Get num of odd lengthed palindromes keeping i in the middle
        max_palindrome = max(max_palindrome, expand_from_middle(string, i, i), key=len)
        # Get num of even lengthed palindromes keeping i and i+1 in the middle
        max_palindrome = max(
            max_palindrome, expand_from_middle(string, i, i + 1), key=len
        )
    return max_palindrome
