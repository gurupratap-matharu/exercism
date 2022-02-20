"""Script to find the search insert position of a target element in a sorted array"""

from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Identifies the index of target if present in nums else
        tells us the index where it would be if inserted in order
        """

        left, right = 0, len(nums) - 1
        found = False

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                found = True
                break

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        search_index = mid if found else left

        return search_index
