def slices(series, length):
    """
    Returns a list of adjacent elements of length n in the given series.
    """
    if length > len(series):
        raise ValueError('Length is greater than the total length of the series!')
    elif length < 1:
        raise ValueError('Length should be a positive number greater than zero.')
    else:
        lst = []
        distance = len(series) - length + 1
        for i in range(distance):
            lst.append(series[i:i + length])
        return lst
