def sieve(limit):
    if limit < 2:
        return []
    multiples = set()
    primes = [2]

    for i in range(3, limit+1, 2):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i, limit+1, i))
    return primes



