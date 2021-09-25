from typing import List


class ArrayUtils:
    def binary_search(self, nums: List[int], target: int) -> int:
        """
        Finds the index of a target in the array nums using
        binary search. If target is not found then returns -1
        """

        def condition(value) -> bool:
            return nums[value] <= target

        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    utils = ArrayUtils()
    assert utils.binary_search(nums=[1, 2, 3, 4, 5], target=4), 3
