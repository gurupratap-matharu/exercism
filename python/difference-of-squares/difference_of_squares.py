def square_of_sum(count):
    """We know that the sum of n natural numbers is given by n(n+1)/2.
       We simply do that return the squared value."""
    return (count * (count + 1) / 2) ** 2


def sum_of_squares(count):
    lst = [x ** 2 for x in range(count + 1)]
    return sum(lst)


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
