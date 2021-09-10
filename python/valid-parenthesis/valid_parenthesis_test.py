"""A testing script to check if all the brackets are correctly matched in a string."""

import unittest

from valid_parenthesis import StringParser


class StringParserTests(unittest.TestCase):
    """Test Suite to check edge cases of strings with valid and invalid brackets."""

    def test_small_empty_string(self):
        self.assertTrue(StringParser().has_valid_brackets(''))

    def test_small_valid_string(self):
        self.assertTrue(StringParser().has_valid_brackets('{}'))

    def test_intermediate_valid_string(self):
        self.assertTrue(StringParser().has_valid_brackets('{}[](){{()}}'))

    def test_large_valid_string(self):
        self.assertTrue(StringParser().has_valid_brackets('{([[(({{{{[[]]}}}}))]])}'))

    def test_small_invalid_string(self):
        self.assertFalse(StringParser().has_valid_brackets('('))

    def test_intermediate_invalid_string(self):
        self.assertFalse(StringParser().has_valid_brackets('{(())[]'))

    def test_large_invalid_string(self):
        self.assertFalse(StringParser().has_valid_brackets('{}[[[((([{[{]}])))]]]'))
