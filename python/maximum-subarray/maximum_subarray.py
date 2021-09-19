"""Utility script to find the maximum subarray problem"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    """Finds the maximum sum possible of any contigous array elements"""

    best_sum = current_sum = float('-inf')

    for element in nums:
        current_sum = max(element, current_sum + element)
        best_sum = max(best_sum, current_sum)

    return best_sum


if __name__ == "__main__":
    assert max_sub_array(nums=[-2, -1, -3, -4, -5, -2, -11, -55, -4]), -1
    assert max_sub_array(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6
