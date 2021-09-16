import unittest

from stock import Stocks


class StocksTests(unittest.TestCase):
    """Test suite to check edge cases for getting profits from stocks"""

    def test_returns_zero_for_no_prices(self):
        self.assertEqual(Stocks().get_max_profit(prices=[]), 0)

    def test_returns_zero_for_all_decreasing_prices(self):
        profit = Stocks().get_max_profit(prices=[x for x in range(100, 0, -1)])
        self.assertEqual(profit, 0)

    def test_returns_correct_profit_for_small_price_list(self):
        profit = Stocks().get_max_profit(prices=[12, 8, 3, 9, 10])
        self.assertEqual(profit, 7)

    def test_returns_correct_profile_for_medium_price_list(self):
        prices = [x for x in range(1, 101)] + [x for x in range(100, 1, -1)]
        profit = Stocks().get_max_profit(prices=prices)
        self.assertEqual(profit, 99)

    def test_returns_correct_profit_for_large_price_list(self):
        prices = [x for x in range(2, 1001)] + [1]
        profit = Stocks().get_max_profit(prices=prices)
        self.assertEqual(profit, 998)

    def test_returns_correct_profit_for_ever_increasing_prices(self):
        profit = Stocks().get_max_profit(prices=[x for x in range(1, 101)])
        self.assertEqual(profit, 99)

    def test_returns_correct_profit_for_tricky_price_list(self):
        profit = Stocks().get_max_profit(prices=[101, 100, 99, 98, 97, 96, 101])
        self.assertEqual(profit, 5)
