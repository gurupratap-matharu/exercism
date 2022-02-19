"""Script to find the first bad version of the API"""


class Solution:
    """Ensemble class to play around with product versions"""

    def __init__(self, bad_entry):
        self.bad_entry = bad_entry

    def first_bad_version(self, n: int) -> int:
        """
        Identifies the first bad version in all versions prior to version `n`
        This method uses binary search and runs in O(logn) time complexity
        """

        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2

            if self.is_bad_version(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def is_bad_version(self, version: int) -> bool:
        """
        Determines if a product version is bad or ok.
        """

        return version >= self.bad_entry
