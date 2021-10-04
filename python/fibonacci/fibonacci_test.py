"""Testing script for the fibonacci sequence"""

import unittest


from fibonacci import Fibonacci


class FibonacciTests(unittest.TestCase):
    """Test Suite to find the nth number of a fibonacci sequence"""

    def test_first_fibonacci_number(self):
        self.assertEqual(Fibonacci().find_nth_number(0), 0)

    def test_second_fibonacci_number(self):
        self.assertEqual(Fibonacci().find_nth_number(1), 1)

    def test_small_fibonacci_number(self):
        self.assertEqual(Fibonacci().find_nth_number(7), 13)

    def test_medium_fibonacci_number(self):
        self.assertEqual(Fibonacci().find_nth_number(16), 987)

    def test_large_fibonacci_number(self):
        self.assertEqual(Fibonacci().find_nth_number(36), 14930352)


if __name__ == "__main__":
    unittest.main()
