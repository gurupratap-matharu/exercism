"""A script to find the total number of ways you can reach `n` steps"""

class Stairs:
    """Utility class to play with stairs"""

    def find_distinct_ways(self, n: int) -> int:
        """
        Finds the distinct number of ways in which you can take `n` steps
        given than you can only take `1` or `2` steps at a time.
        """
        a, b = 1, 2

        if n <= 0: return 0
        if n == 1: return a
        if n == 2: return b

        for i in range(2, n):
            sum = a + b
            b, a = sum, b

        return sum


if __name__=='__main__':
    res = Stairs().find_distinct_ways(n=4)
    print(res)
