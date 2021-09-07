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
            if len(set(tup)) == 1:
                prefix.append(tup[0])
            else:
                break

        return ''.join(prefix)


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['flower', 'flow', 'florencia']))
    print(s.longestCommonPrefix(['abc', 'abcd', 'abcde']))
    print(s.longestCommonPrefix(['1', '1ab', '1abc']))
    print(s.longestCommonPrefix(['abc', 'bcd', 'abc']))
