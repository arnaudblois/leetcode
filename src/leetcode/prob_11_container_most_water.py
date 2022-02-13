"""Leetcode 011 - Container with the most max_water

Considering a list of integers corresponding to heights, return the maximum
volume of water that could be contained between two of these.

Example:
[1, 4, 2, 4, 5, 2, 3]

                |
    | *   * | * |
    | *   * | * |       |
    | * | * | * |   |   |
|   | * | * | * |   |   |

Answer is 12.
"""


def find_max_water_brute_force(heights: list[int]) -> int:
    """Return the max volume by brute force.

    Runs in O(n²).
    """
    n = len(heights)
    max_water = 0
    for i in range(n):
        for j in range(i, n):
            max_water = max(max_water, (j - i) * min(heights[j], heights[i]))
    return max_water


def find_max_water(heights: list[int]) -> int:
    """Return the max volume using two pointers.

    Runs in O(n).
    """
    left = 0
    right = len(heights) - 1
    max_water = 0
    while left < right:
        max_water = max(max_water, (right - left) * min(heights[left], heights[right]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water
