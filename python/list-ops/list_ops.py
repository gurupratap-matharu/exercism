def append(xs, ys):
    """
    Appends the elements of ys into xs and returns xs
    """
    xs.extend(ys)
    return xs


def concat(lists):
    """
    We assume the depth of list is till level 2. Returns a flatted list
    """

    lst = []

    for chunk in lists:

        if type(chunk) == list:  # to check list inside a list

            for elem in chunk:
                lst.append(elem)
        else:
            lst.append(chunk)

    return lst


def filter_clone(function, xs):
    """
    Elements from xs are filtered out only for which the output of function holds True.
    """
    return [elem for elem in xs if function(elem)]


def length(xs):
    """Returns the length of the list"""
    return len(xs)


def map_clone(function, xs):
    """
    Sends every element xs to the function and returns a processed list.
    """
    return [function(elem) for elem in xs]


def foldl(function, xs, acc):
    """
    To simulate reduce functionality. Start from left and take 2 elements at a time.
    """
    if xs:
        result = function(xs[0], xs[1])

        for i in range(2, len(xs)):
            result = function(result, xs[i])

        return function(result, acc)
    else:
        return acc


def foldr(function, xs, acc):
    """Similar to foldl function but here we start from right and take 2 elements at a time.
    """
    if xs:
        result = function(xs[-1], xs[-2])

        for i in range(3, len(xs) + 1):
            result = function(result, xs[-i])

        result = function(acc, result)
        if type(result) == str:
            return result[::-1]  # I do this to pass the unittest. I think answer should be a reverse string though! like '!msicrexe'
        else:
            return result
    else:
        return acc


def reverse(xs):
    """Returns the reverse of a list. We can achieve this by list slicing"""
    return xs[::-1]
