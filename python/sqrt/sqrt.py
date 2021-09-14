class NumberUtils:
    """Base class to play around with numbers."""

    def find_square_root(self, num: int) -> int:
        """
        Finds the nearest truncated square root of a number.
        """
        if num < 0:
            raise ValueError('Number should be greater than or equal to zero!')

        for i in range(0, num + 2):
            if i * i > num:
                return i - 1


if __name__ == '__main__':
    assert NumberUtils().find_square_root(4), 2
    assert NumberUtils().find_square_root(8), 2
    assert NumberUtils().find_square_root(16), 4
    assert NumberUtils().find_square_root(24), 4
    assert NumberUtils().find_square_root(101), 10
