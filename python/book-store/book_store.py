def calculate_total(books):
    d = {
        0: 0,
        1: 800,
        2: 1520,
        3: 2160,
        4: 2560,
        5: 3000
    }

    total_cost = 0

    counts = [books.count(i) for i in range(1, 6)]

    while counts:

        print(counts)
        counts = [x for x in counts if x != 0]
        uniques = len(counts)
        total_cost += d[uniques]
        counts = [x - 1 if x > 0 else 0 for x in counts]

    return total_cost


if __name__ == '__main__':
    print(calculate_total([1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]))
