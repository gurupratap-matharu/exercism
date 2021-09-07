"""Testing script for Roman strings to integer equivalents."""

import unittest

from roman_to_integer import Converter


class ConverterTests(unittest.TestCase):
    """Test Suite for testing edge cases of roman strings to integers"""

    def test_conversion_works_for_small_roman_numbers(self):
        self.assertEqual(Converter().roman_to_integer('IV'), 4)

    def test_conversion_works_for_valid_medium_size_roman_numbers(self):
        self.assertEqual(Converter().roman_to_integer('IL'), 49)

    def test_conversion_works_for_valid_large_roman_numbers(self):
        self.assertEqual(Converter().roman_to_integer('MCIVV'), 1109)

    def test_conversion_works_for_tricky_large_roman_numbers(self):
        self.assertEqual(Converter().roman_to_integer('CDCM'), 1300)

    def test_conversion_works_for_very_large_valid_roman_numbers(self):
        self.assertEqual(Converter().roman_to_integer('MCMXCIV'), 1994)

    def test_conversion_raises_exception_for_invalid_roman_numbers(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
