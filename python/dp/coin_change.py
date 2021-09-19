class CoinChange:
    def get_min_coins_needed_using_dp(self, denominations: list[int], amount: int):
        """
        Finds the minimum number of coins needed of given denominations
        to build an amount (or exchange an amount) k using dynamic programming.
        """

        n = len(denominations)
        dp = [[0] * (amount + 1) for x in range(n + 1)]
        return dp


if __name__ == '__main__':
    obj = CoinChange()
    print(obj.get_min_coins_needed_using_dp(denominations=[1, 3, 4], amount=6))
