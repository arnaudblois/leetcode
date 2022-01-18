"""
Given a string, find the length of the longest substring
without repeating characters.
"""


def longest_no_repeat(string: str) -> int:
    """Return longest length of a substring with no repeating characters."""
    last_seen = {}
    max_so_far = 0
    current_streak = 0
    for i, letter in enumerate(string):
        try:
            index_last_seen = last_seen[letter]
            current_streak = i - index_last_seen
        except KeyError:
            current_streak += 1
            max_so_far = max(max_so_far, current_streak)
        last_seen[letter] = i
    return max_so_far
