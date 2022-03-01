"""
Merge two sorted arrays into one. This is an inplace merge for the first
array. The script does not return anything.
"""

from typing import List
import pdb

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 and maintains the non-decreasing order.
        Note:

            This is an inplace merge and the function does not return
            anything.
        """

        nums1 = nums1[:m]
        i = j = 0

        while (i < m and j < n):
            n_1, n_2 = nums1[i], nums2[j]
            print(f'i: {i}, j: {j}, n_1: {n_1}, n_2: {n_2}, nums1: {nums1}')
            pdb.set_trace()

            if n_1 < n_2:
                i += 1
            else:
                nums1.insert(i, n_2)
                j += 1

        pdb.set_trace()

        if j < n:
            nums1 += nums2[j:]

        print(nums1)


if __name__ == "__main__":
    A = [1, 2, 3, 0, 0, 0]
    B = [2, 5, 6]
    Solution().merge(nums1=A, m=3, nums2=B, n=3)
    print(A)
