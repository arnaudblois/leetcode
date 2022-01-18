"""LeetCode problem 001 - Two Sum

Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution.

Example:
>>>> two_sum(nums=[2, 5, 8, 21], target=13)
[1, 2].
"""


def two_sum(nums: list, target: int) -> list[int]:
    """Run in O(n) time, O(n) memory by using a dictionary.

    The hint is in the `each input would have exactly one solution`.
    For each number n, we check if we there is a matching `target - n`:
        if so, then we have our pair
        if not, we update the dictionary and check the next number
    """
    num_dict = {}
    for i1, num in enumerate(nums):
        try:
            i2 = num_dict[target - num]
            return [i1, i2]
        except KeyError:
            num_dict[num] = i1
    return []


def two_sum_brute(nums: list, target: int) -> list[int]:
    """Run in O(n**2) with memory O(1)."""
    i1 = 0
    while i1 < len(nums) - 1:
        i2 = i1 + 1
        while i2 < len(nums):
            print(i1, i2, nums[i1], nums[i2])
            if nums[i1] + nums[i2] == target:
                return [i1, i2]
            i2 += 1
        i1 += 1
    return []
