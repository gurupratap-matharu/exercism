import unittest

from repeated_string_pattern import Parser


class ParserTests(unittest.TestCase):
    """Test Suite to check all edge cases for string parsing"""

    def test_string_with_no_pattern_returns_false(self):
        self.assertFalse(Parser().is_repeated_string_pattern('abcdxyz'))

    def test_string_with_no_pattern_but_tricky_returns_false(self):
        self.assertFalse(Parser().is_repeated_string_pattern('abcdeabcdeabcd'))

    def test_string_with_single_letter_pattern_returns_true(self):
        self.assertTrue(Parser().is_repeated_string_pattern('aaaaaaaaaa'))

    def test_string_with_two_letter_pattern_returns_true(self):
        self.assertTrue(Parser().is_repeated_string_pattern('ababababababab'))

    def test_string_with_three_pattern_returns_true(self):
        self.assertTrue(Parser().is_repeated_string_pattern('xyzxyzxyz'))

    def test_string_with_four_letter_pattern_returns_true(self):
        self.assertTrue(Parser().is_repeated_string_pattern('abcdabcdabcd'))
