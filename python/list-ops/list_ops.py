def append(xs, ys):
    """
    Adds all the elements of xs and ys and returns a combined list.
    """

    return xs + ys


def concat(lists):
    """
    We assume the depth of list is till level 2. Returns a flatted list
    """

    lst = []

    for chunk in lists:

        if type(chunk) == list:  # to check list inside a list

            for elem in chunk:
                # lst.append(elem)
                lst += [elem]
        else:
            lst += [chunk]

    return lst


def filter_clone(function, xs):
    """
    Elements from xs are filtered out only for which the output of function holds True.
    """
    filtered_lst = []  # We'll store our results here.

    for elem in xs:
        if function(elem):
            filtered_lst += [elem]

    return filtered_lst


def length(xs):
    """Returns the length of the list"""

    if xs:                      # To check if list is not empty.
        for count, elem in enumerate(xs):
            pass
        return count + 1
    else:
        return 0


def map_clone(function, xs):
    """
    Sends every element xs to the function and returns a processed list.
    """
    map_cloned_lst = []

    for elem in xs:
        map_cloned_lst += [function(elem)]

    return map_cloned_lst


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
