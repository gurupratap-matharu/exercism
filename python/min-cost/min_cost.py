from typing import List


class Stairs:
    """
    Represents the stairs and exposes utility methods to find the
    costs of climbing them.
    """

    def min_cost_of_climbing_stairs(self, cost: List[int]) -> int:
        """
        Finds the minimum cost of climbing stairs using dynamic programming
        """
        if not cost:
            return 0

        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        print("Veer cost: ", cost)
        print("Veer dp: ", dp)

        return min(dp[-1], dp[-2])


if __name__ == "__main__":
    res = Stairs().min_cost_of_climbing_stairs(
        cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    )
    print(res)
