def iter_flatten(iterable):
    """
    Flattens a list or tuple of arbitrary nested depth into one single list.
    """

    my_iter = iter(iterable)

    for element in my_iter:
        if isinstance(element, (list, tuple)):
            for nested_element in iter_flatten(element):
                yield nested_element
        else:
            yield element


def flatten(iterable):
    """
    Helper method which returns an in-memory list from a generator based flattener."""

    return [x for x in list(iter_flatten(iterable)) if x is not None]
