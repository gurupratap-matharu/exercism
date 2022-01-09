from typing import List


class ArrayUtils:
    def binary_search(self, nums: List[int], target: int) -> int:
        """
        Finds the index of a target in the array nums using
        binary search. If target is not found then returns -1
        """

        if len(nums) == 1 and nums[0] == target:
            return 0

        def condition(value) -> bool:
            return nums[value] <= target

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if condition(mid):
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    utils = ArrayUtils()
    assert utils.binary_search(nums=[1, 2, 3, 4, 5], target=4), 3
    assert utils.binary_search(nums=[1, 2, 3, 4, 5], target=6), -1
    assert utils.binary_search(nums=[-1, 0, 3, 5, 9, 12], target=9), 4
    print(utils.binary_search(nums=[-2, 0, 3, 5, 9, 12], target=13))
    utils.binary_search(nums=[2, 5], target=5), 1
