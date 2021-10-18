"""Unit test script for testing reversing of vowels on a string"""

import unittest

from reverse_vowels import StringUtils


class StringUtilsTests(unittest.TestCase):
    """Test suite to check edge cases while manipulating strings"""

    def test_reverse_vowels_on_blank_string(self):
        self.assertEqual(StringUtils().reverse_vowels(text=""), "")

    def test_reverse_vowels_on_small_string(self):
        self.assertEqual(StringUtils().reverse_vowels(text="hello"), "holle")

    def test_reverse_vowels_on_string_with_repeated_vowels(self):
        self.assertEqual(StringUtils().reverse_vowels(text="aaeeiioouu"), "uuooiieeaa")

    def test_reverse_vowels_on_string_with_uppercase_letters(self):
        self.assertEqual(StringUtils().reverse_vowels(text="HELLO"), "HOLLE")

    def test_reverse_vowels_on_string_with_mixed_case_letters(self):
        self.assertEqual(StringUtils().reverse_vowels(text="lEeTCOde"), "leOTCedE")
