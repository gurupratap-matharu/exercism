def is_armstrong(number):

    total = 0
    length = len(str(number))
    for i in str(number):
        total += int(i) ** int(length)

    return total == number
