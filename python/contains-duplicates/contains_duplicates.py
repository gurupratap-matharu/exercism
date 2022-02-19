"""Finds if an array of integers contains any duplicates or not"""

from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Identifies if there are any duplicates in the array of integers.
        """

        return len(nums) != len(set(nums))
