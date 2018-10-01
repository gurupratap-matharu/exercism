import os
pronunciations = [
    (0, 'zero'),
    (1, 'one'),
    (2, 'two'),
    (3, 'three'),
    (4, 'four'),
    (5, 'five'),
    (6, 'six'),
    (7, 'seven'),
    (8, 'eight'),
    (9, 'nine'),
    (10, 'ten'),
    (11, 'eleven'),
    (12, 'twelve'),
    (13, 'thirteen'),
    (14, 'fourteen'),
    (15, 'fifteen'),
    (16, 'sixteen'),
    (17, 'seventeen'),
    (18, 'eighteen'),
    (19, 'nineteen'),
    (20, 'twenty'),
    (30, 'thirty'),
    (40, 'forty'),
    (50, 'fifty'),
    (60, 'sixty'),
    (70, 'seventy'),
    (80, 'eighty'),
    (90, 'ninety'),
    (100, 'one hundred'),
]
pronun = dict(pronunciations)


def say(number):
    """
    Says the number out loud through the default say command of terminal.
    Parses long numbers out systematically but has a limit to handle uptil trillion and no more.
    """
    # n = ('{:,}'.format(number))
    # # os.system('say %s' % n)
    # x, y = splitter(number)
    # if y == 0:
    #     return pronun[x]
    # else:
    #     return pronun[x], pronun[y]

    return (pronun[x] for x in splitter(number))

def splitter(number):
    """
    splits the number in 10's for correct pronunciation.
    """
    if number <= 20:
        return number, 0
    elif 21 <= number <= 100:
        x, y = divmod(number, 10)
        return 10 * x, y
    elif 101 <= number <= 1000:
        x, y = divmod(number, 100)
        return 100 * x, y


for i in range(100, 140):
    print(say(i))
