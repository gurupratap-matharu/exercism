"""Unit test script for testing reversing of vowels on a string"""

import unittest

from reverse_vowels import StringUtils

class StringUtilsTests(unittest.TestCase):
    """Test suite to check edge cases while manipulating strings"""

    def test_reverse_vowels_on_blank_string(self):
        self.assertEqual(StringUtils().reverse_vowels(text=''), '')
