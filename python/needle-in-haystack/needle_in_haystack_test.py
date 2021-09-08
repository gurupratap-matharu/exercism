import unittest

from needle_in_haystack import NeedleHayStack


class NeedleHayStackTests(unittest.TestCase):
    def test_needle_existing_in_a_small_haystack(self):
        nh = NeedleHayStack()
        calculated = nh.find_index_of_needle_in_haystack(haystack='hello', needle='ll')
        expected = 2
        self.assertEqual(calculated, expected)

    def test_needle_not_existing_in_a_small_haystack(self):
        nh = NeedleHayStack()
        calculated = nh.find_index_of_needle_in_haystack(haystack='aaaaaaaa', needle='baa')
        expected = -1
        self.assertEqual(calculated, expected)

    def test_empty_needle_in_empty_haystack(self):
        nh = NeedleHayStack()
        calculated = nh.find_index_of_needle_in_haystack(haystack='', needle='')
        expected = 0
        self.assertEqual(calculated, expected)
