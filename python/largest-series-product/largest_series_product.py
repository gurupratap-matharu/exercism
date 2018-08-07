def largest_product(series, size):

    if size < 0:
        raise ValueError('Size of consideration should be >= 0')
    elif size > len(series):
        raise ValueError('Size is greater than the length of the series itself!')
    elif (series.isnumeric() == False) & (len(series) != 0):
        raise ValueError('Invalid Characters in the series. It should be numeric')

    lst_of_products = []  # To store all sub products in this list
    run = len(series) - size + 1  # We run the loop till the run value to avoid range
    # error and take into account all the digits
    for i in range(run):
        intermediate_product = 1
        for element in series[i:(i + size)]:
            intermediate_product *= int(element)
        lst_of_products.append(intermediate_product)

    return max(lst_of_products)


print(largest_product("...", 2))
