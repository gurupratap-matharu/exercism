def append(xs, ys):
    return xs.append(ys)


def concat(lists):
    lst = []
    for i in lists:
        if isinstance(i, (list, tuple)) & bool(i):
            for j in concat(i):
                lst.append(j)
        else:
            return lst.append(i)
    return lst


def filter_clone(function, xs):
    return [function(elem) for elem in xs]


def length(xs):
    for count, elem in enumerate(xs):
        pass
    return count


def map_clone(function, xs):
    return [function(elem) for elem in xs]


def foldl(function, xs, acc):
    pass


def foldr(function, xs, acc):
    pass


def reverse(xs):
    return xs.reverse()
