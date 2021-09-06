import unittest

from break_another_string import Breaker


class BreakerTests(unittest.TestCase):
    """Test Suite to incorporate all unit tests for Breaker"""

    def setUp(self) -> None:
        self.breaker = Breaker()

    def test_check_if_can_break_is_true_for_small_valid_strings(self):
        self.assertTrue(self.breaker.check_if_can_break('abc', 'xya'))

    def test_check_if_can_break_is_true_for_long_valid_strings(self):
        self.assertTrue(self.breaker.check_if_can_break("leetcodee", "interview"))

    def test_check_if_can_break_is_false_for_small_invalid_strings(self):
        self.assertFalse(self.breaker.check_if_can_break('abe', 'acd'))


if __name__ == '__main__':
    unittest.main()
