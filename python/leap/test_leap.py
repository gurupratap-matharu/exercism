"""First we import the 'unittest module' and our function 'is_leap_year' which we want to test"""

import unittest

from leap import is_leap_year


class leapTest(unittest.TestCase):
    """Here we shall write all the various functions for testing our leapyear script"""

    def test_year_divisible_by_4(self):
        self.assertIs(is_leap_year(1996), True)
        self.assertIs(is_leap_year(8), True)
        self.assertIs(is_leap_year(1412), True)
        self.assertIs(is_leap_year(1236), True)

    def test_year_divisible_by_100_but_not_divisible_by_400(self):
        self.assertIs(is_leap_year(200), False)
        self.assertIs(is_leap_year(1400), False)
        self.assertIs(is_leap_year(600), False)
        self.assertIs(is_leap_year(1900), False)
        self.assertIs(is_leap_year(1000), False)

    def test_year_divisible_by_400(self):
        self.assertIs(is_leap_year(40000), True)
        self.assertIs(is_leap_year(2400), True)
        self.assertIs(is_leap_year(3600), True)
        self.assertIs(is_leap_year(1600), True)
        self.assertIs(is_leap_year(2400), True)


if __name__ == '__main__':
    unittest.main()
