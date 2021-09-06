"""Utility function which flattens an arbitrary nested iterable (list/tuple)"""


def iter_flatten(iterable):
    """
    Flattens a list or tuple of arbitrary depth into one single list.
    """

    my_iter = iter(iterable)

    for element in my_iter:
        if isinstance(element, (list, tuple)):
            for nested_element in iter_flatten(element):
                yield nested_element
        else:
            yield element


def flattener(iterable):
    return list(iter_flatten(iterable))


if __name__ == '__main__':

    a = []
    for i in range(15):
        a = [a, i]
    print("Nested Iterator: {}".format(a))
    print("Flattened Iterator: {}".format(flattener(a)))
