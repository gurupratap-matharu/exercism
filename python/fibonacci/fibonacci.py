class Fibonacci:
    """
    Represents a Fibonacci sequence starting with 0, 1...
    """

    def find_nth_number(self, n: int) -> int:
        """
        Finds the `n`th number in the fibonacci sequence.
        """

        a, b = 0, 1

        for _ in range(n):
            a, b = b, a + b

        return a


if __name__ == "__main__":
    for i in list(range(0, 135, 2)):
        res = Fibonacci().find_nth_number(i)
        print(i, ' => ', res)
