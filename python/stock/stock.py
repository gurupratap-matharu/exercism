"""Utility script to find the stock statistics"""

from typing import List


class Stocks:
    """Base class to play around with stock prices"""

    def get_max_profit(self, prices: List[int]) -> int:
        """Used to find the maximum profile we can make from any stock"""

        n = len(prices)
        profit = 0

        for i in range(n-1):
            for j in range(i+1, n):
                current_profit = prices[j] - prices[i]
                profit = max(profit, current_profit)
        return profit


if __name__ == '__main__':
    stocks = Stocks()
    print(stocks.get_max_profit(prices=[7, 1, 5, 3, 6, 4]))
    print(stocks.get_max_profit(prices=[7, 6, 4, 3, 1]))
