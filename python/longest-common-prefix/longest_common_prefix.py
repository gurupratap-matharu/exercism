"""Finds the longest common prefix among an array for words"""

from typing import List


class Solution:
    """Abstract class to hold our solution"""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix in a array of strings.
        """

        prefix = []
        for tup in zip(*strs):
            print(tup)


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['flower', 'flow', 'florencia']))
