def flatten(iterable):

    lst = []
    for row in iterable:
        if isinstance(row, list):
            for element in flatten(row):
                lst.append(element)
        else:
            lst.append(row)
    return lst


print(flatten([0, 1, 2]))
