"""
Testing script to check edge cases for word_pattern.py
"""

import unittest

from word_pattern import Solution


class WordPatternTests(unittest.TestCase):
    """
    Test suite to check edge cases for word patterns.
    """

    def test_small_valid_word_pattern(self):
        self.assertTrue(Solution().word_pattern("abb", "dog cat cat"))

    def test_medium_valid_word_pattern(self):
        self.assertTrue(
            Solution().word_pattern(
                "xxyyzzxx", "hola hola como como estas estas hola hola"
            )
        )

    def test_large_valid_word_pattern(self):
        self.assertTrue(
            Solution().word_pattern(
                "abcabccbacba", "how are you how are you you are how you are how"
            )
        )

    def test_small_tricky_valid_word_pattern(self):
        self.assertTrue(
            Solution().word_pattern("abccbbaa", "me you love love you you me me")
        )

    def test_medium_tricky_valid_word_pattern(self):
        self.assertTrue(
            Solution().word_pattern("xyzzzzzyx", "how are you you you you you are how")
        )

    def test_small_invalid_word_pattern(self):
        self.assertFalse(Solution().word_pattern("abb", "cat dog cat"))

    def test_medium_invalid_word_pattern(self):
        self.assertFalse(Solution().word_pattern("abcabca", "cat dog bull cat dog bull dog"))
