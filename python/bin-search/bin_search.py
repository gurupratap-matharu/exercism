"""Script to find an element in a sorted array using binary search"""


class Solution:
    """A generic class the exposes the api to solve this problem"""

    def search(self, A: list[int], target: int) -> int:
        """
        Returns the index of target in the array A using binary search.
        if not found returns -1
        """

        left, right = 0, len(A) - 1
        found = False

        while left <= right:

            mid = (left + right) // 2

            if A[mid] == target:
                found = True
                break

            elif A[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        res = mid if found else -1

        return res
