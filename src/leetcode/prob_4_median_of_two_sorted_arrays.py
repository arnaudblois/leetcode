""" LeetCode 004 - find the median of two sorted arrays."""


def find_median(list_1: list[int], list_2: list[int]) -> float:
    """Return the median of two sorted arrays.

    This is the most efficient way to do it, in O(n + m), relying on the fact
    both lists are already sorted.

    It relies on finding the cutoff index in the shortest list where everything
    on the left is below the median and on the right above.

    It is a rather complicated solution. A slightly less efficient but much
    easier-to-read function is given below.
    """

    n = len(list_1)
    m = len(list_2)
    merged_mid_index = (n + m + 1) // 2
    if n > m:
        return find_median(list_2, list_1)

    # We set up the interval of possible values for this cutoff index.
    # It must be in list_1, so the bounds are 0 and n
    cutoff_min_index, cutoff_max_index = 0, n

    # We then try to narrow down this interval.
    # We set cutoff_1, a trial value for this cutoff. cutoff_2 is the
    # corresponding cutoff in list_2.
    while cutoff_min_index <= cutoff_max_index:
        cutoff_1 = (cutoff_min_index + cutoff_max_index) // 2
        cutoff_2 = merged_mid_index - cutoff_1

        # These cutoff separates both lists in two parts each.
        # We want to compare the minimum of the left part of list_2
        # with the maximum of the right part of list_1, and vice-versa.
        max_left_1 = list_1[cutoff_1 - 1] if cutoff_1 > 0 else float("-inf")
        max_left_2 = list_2[cutoff_2 - 1] if cutoff_2 > 0 else float("-inf")
        min_right_1 = list_1[cutoff_1] if cutoff_1 < n else float("inf")
        min_right_2 = list_2[cutoff_2] if cutoff_2 < m else float("inf")

        # If this condition is true, it means we have found the real cutoff
        # value, which means we can return the median.
        if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
            if (m + n) % 2 == 1:
                return max(max_left_1, max_left_2)
            else:
                return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2

        # Otherwise, we narrow down the interval
        if max_left_1 > min_right_2:
            cutoff_max_index = cutoff_1 - 1
        else:
            cutoff_min_index = cutoff_1 + 1


def find_median_simpler_bit_less_efficient(list1: list[int], list2: list[int]) -> float:
    """Alternative way to find the median.

    Since we need to sort the combined list, this is in O ((n+m) ln(n+m)).
    That said, Python sorting uses a variation of the timsort algo which does
    take into account pre-existing sorting so it might come only with a small
    penalty compared to the above.
    """
    merged_list = sorted(list1 + list2)
    length = len(merged_list)
    if length == 0:
        return None
    if length % 2 == 0:
        return (merged_list[length // 2 - 1] + merged_list[length // 2]) / 2
    else:
        return merged_list[length // 2]
