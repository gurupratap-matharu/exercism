def selfdividing(left, right):
    lst = []

    for i in range(left, right + 1):
        if self_dividing(i):
            lst.append(i)
    return lst


def self_dividing(n):
    for d in str(n):
        if d == '0' or n % int(d) > 0:
            return False
    return True


print(selfdividing(2, 21))
