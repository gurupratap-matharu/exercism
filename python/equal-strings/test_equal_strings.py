import unittest

from equal_strings import check_if_equal


class EqualStringTests(unittest.TestCase):
    def test_check_empty_string(self):
        self.assertTrue(check_if_equal('', ''))

    def test_check_valid_small_string(self):
        self.assertTrue(check_if_equal('xy#z', 'xw#z'))

    def test_check_invalid_small_string(self):
        self.assertFalse(check_if_equal('abcd##', 'acbd##'))

    def test_check_valid_another_small_string(self):
        self.assertTrue(check_if_equal('z##y', '#d#y'))

    def test_check_valid_string(self):
        self.assertTrue(check_if_equal('er##', 'u#u#'))
