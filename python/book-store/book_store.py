def calculate_total(books):
    """
    Returns the minimum cost of books for any conceivable shopping cart
    """
    # We store the discounted price of occurences of each type
    d = {
        0: 0,
        1: 800,
        2: 1520,
        3: 2160,
        4: 2560,
        5: 3000
    }

    total_cost = 0
    total_cost_lst = 0

    counts = [books.count(i) for i in range(1, 6)]  # Tells us the number or each type of book in the shopping cart.
    counts.sort(reverse=True)

    lst = counts.copy()

    # First we find the total cost descending from highest groupings of 5 to the lowest groupings of 1.
    # We do this since higher groupings have larger absolute discounts.
    while counts:

        counts = [x for x in counts if x != 0]  # Removes zeroes
        uniques = len(counts)  # This the current highest unique combination
        counts = [x - 1 if x > 0 else 0 for x in counts]  # Reduce 1 item from entire basket.

        total_cost += d[uniques]  # Store the total cost here

    # Now we calculate costs using preferred groupings of 4! In some cases this yields better discounts.
    while lst:

        lst = [x for x in lst if x != 0]  # Remove zeroes

        if len(lst) >= 4:
            total_cost_lst += d[4]
            for i in range(4):
                lst[i] -= 1  # Reduce 1 item from first four elements.

        else:
            total_cost_lst += d[len(lst)]
            lst = [x - 1 if x > 0 else 0 for x in lst]  # Reduce 1 item from entire basket.

    return min(total_cost_lst, total_cost)
