def distance(strand_a, strand_b):
    """In this function we compare both the arguments in a loop using the zip utility since both of them are of the same length.
    For each inequality we encounter we shall keep a record of hamming distance in a simple variable and finally return it."""
    if len(strand_a) != len(strand_b):
        raise ValueError('Length of both the DNA strands should be exactly the same to calculate the Hamming distance.')
    hamming_distance = 0

    for i, j in zip(strand_a, strand_b):
        if i != j:
            hamming_distance += 1
    return hamming_distance


print(distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))
