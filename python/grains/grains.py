def on_square(integer_number):
    """This function returns the number of grains on a particular square of the chessboard. See README file for how it is calculated."""

    # We ensure that the input number is greater than zero and less than 65
    if integer_number <= 0 or integer_number > 64:
        raise ValueError('Value should be a positive integer between 1 and 64(inclusive)')
    return 2 ** (integer_number - 1)


def total_after(integer_number):
    """Returns the total number of grains on the chess board for given number of squares.
    See README file for how it is calculated.
    The calculation is essentially a Geometric series where a=1, r=2 and the sum of such a series is given by
                            a(1-r**n)
                        S = _________
                               1-r

    """
    if integer_number <= 0 or integer_number > 64:
        raise ValueError('Value should be a positive integer between 1 and 64(inclusive)')
    return -(1 - 2**integer_number)  # This is the formula for a geometric series!
