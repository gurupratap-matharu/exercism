"""
Defines the Solution for the WordPatter problem.
The API is exposed in a Solution class which can be
instantiated and run via suitable methods.
"""


class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        """
        Identifies if the string `s` and the argument `pattern follow the same pattern.
        """
        s = s.split()
        return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s)))
