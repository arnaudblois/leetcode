"""Leetcode 006 - Conversion zigzag

A string gets written in a zigzaggy way over a number of rows in this fashion.
MyExampleString, 4

M           p           i
  y       m   l       r   n
    E   a       e   t        g
      x           S

The result is then read as-is: MpiymlrnEaetgxS
"""

from enum import Enum


class Direction(Enum):
    """Helper Enum to make the zigzag current direction more readable."""

    UP = True
    DOWN = False


def convert_zigzag(string: str, number_of_rows: int) -> str:
    """Perform the zigzag conversion.

    Runs in O(n).
    """

    if number_of_rows <= 1 or number_of_rows >= len(string):
        return string

    rows = ["" for _ in range(number_of_rows)]
    direction = Direction.DOWN
    row_nb = 0
    for letter in string:
        rows[row_nb] += letter
        if direction == Direction.UP:
            direction = Direction.DOWN if row_nb == 1 else Direction.UP
            row_nb -= 1
        else:
            direction = Direction.UP if row_nb == number_of_rows - 2 else Direction.DOWN
            row_nb += 1
    return "".join(rows)
