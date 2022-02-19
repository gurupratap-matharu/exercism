"""Script to find pairs of three numbers in an array whose sum is zero"""

import itertools


def find_three_sum_pairs(nums):
    """
    Finds unique pairs of three numbers in the array whose sum is zero
    """

    pairs = []

    for t in itertools.combinations(nums, 3):
        if not sum(t):
            pairs.append(sorted(t))

    pairs = sorted(pairs)
    return [pairs for pairs, _ in itertools.groupby(pairs)]


if __name__ == "__main__":
    nums = [-1, 0]
    res = find_three_sum_pairs(nums)
    print(res)
