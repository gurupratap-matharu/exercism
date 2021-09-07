import unittest

from slowest_key import KeyUtils


class KeyUtilsTests(unittest.TestCase):
    """Test Suite to run unit tests for all edge cases of KeyUtils."""

    def setUp(self) -> None:
        self.obj = KeyUtils()

    def test_slowest_key_works_correctly_for_multiple_keys_with_equal_duration(self):
        calculated = self.obj.slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed='cbcd')
        expected = 'c'
        self.assertEqual(calculated, expected)

    def test_slowest_key_works_correctly_for_keys_with_unique_duration(self):
        calculated = self.obj.slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed='spuda')
        expected = 'a'
        self.assertEqual(calculated, expected)
