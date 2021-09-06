"""Testing script for Longest Common Prefix"""

import unittest

from longest_common_prefix import Solution


class LongestCommonPrefixTests(unittest.TestCase):
    """Test Suite to execute unit tests for all common prefix cases"""

    def setUp(self) -> None:
        self.obj = Solution()

    def test_common_prefix_works_for_single_letter_prefix(self):
        words = ['a', 'ab', 'abc']
        expected = 'a'
        calculated = self.obj.longestCommonPrefix(words)
        self.assertEqual(calculated, expected)

    def test_common_prefix_works_for_double_letter_prefix(self):
        words = ['xy', 'xyz', 'xyzz']
        expected = 'xy'
        calculated = self.obj.longestCommonPrefix(words)
        self.assertEqual(calculated, expected)

    def test_common_prefix_returns_blank_string_for_valid_cases(self):
        words = ['Mr', 'Sr', 'Res', 'Hon.', 'Sra']
        expected = ''
        calculated = self.obj.longestCommonPrefix(words)
        self.assertEqual(calculated, expected)

    def test_common_prefix_returns_blank_string_for_one_uncommon_word(self):
        words = ['Mr', 'Mrs', 'Mra', 'mrA', 'Sra']
        expected = ''
        calculated = self.obj.longestCommonPrefix(words)
        self.assertEqual(calculated, expected)

    def test_common_prefix_works_for_long_prefixes(self):
        words = ['Sr. # 1. Doctor', 'Sr. # 1. Doctorate', 'Sr. # 1. Doctors in Medical']
        expected = 'Sr. # 1. Doctor'
        calculated = self.obj.longestCommonPrefix(words)
        self.assertEqual(calculated, expected)

    def test_common_prefix_works_for_intermediate_spaces_in_words(self):
        words = ['Inr Usd ', 'Inr Usd Aus', 'Inr Usd Aus Yen', 'Inr Usd Aus Yen Gbp']
        expected = 'Inr Usd'
        calculated = self.obj.longestCommonPrefix(words)
        self.assertEqual(calculated, expected)


if __name__ == '__main__':
    unittest.main()
