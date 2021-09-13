import unittest

from sqrt import NumberUtils


class NumberUtilsTests(unittest.TestCase):
    """Test Suite to check edge cases for finding approximate square roots."""

    def test_square_root_of_zero_is_zero(self):
        self.assertEqual(NumberUtils().find_square_root(0), 0)

    def test_square_root_of_small_perfect_square(self):
        self.assertEqual(NumberUtils().find_square_root(25), 5)

    def test_square_root_of_medium_perfect_square(self):
        self.assertEqual(NumberUtils().find_square_root(250000), 500)

    def test_square_root_of_large_perfect_square(self):
        self.assertEqual(NumberUtils().find_square_root(1522756), 1234)

    def test_square_root_of_small_imperfect_squre(self):
        self.assertEqual(NumberUtils().find_square_root(8), 2)

    def test_square_root_of_medium_imperfect_squre(self):
        self.assertEqual(NumberUtils().find_square_root(8), 2)

    def test_square_root_of_small_imperfect_squre(self):
        self.assertEqual(NumberUtils().find_square_root(251000), 500)

    def test_square_root_of_large_imperfect_squre(self):
        self.assertEqual(NumberUtils().find_square_root(1525224), 1234)

    def test_square_root_of_negative_number_raises_valid_exception(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
