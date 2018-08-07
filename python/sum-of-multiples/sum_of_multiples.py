def sum_of_multiples(limit, multiples):
    return sum(set(x for y in multiples for x in range(y, limit, y)))
