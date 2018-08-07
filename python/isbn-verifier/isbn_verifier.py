def verify(isbn):
    isbn = isbn.split('-')
    total = 0
    if isbn[:-1].isalpha() OR len(isbn) != 10 or (isbn[-1] != 'X' AND isbn[-1].isnumeric() == False):
        return False

    elif isbn[-1] == 'X':
        total = 10
        isbn.remove('X')
        isbn.append('0')

    isbn = ''.join(isbn)
    if isbn.isnumeric():
        for i in range(10):
            total += (10 - i) * int(isbn[i])
        return total % 11 == 0

    else:
        print('Invalid ISBN number')


print(verify('3-598-21508-8'))
print(verify('3-598-21507-X'))
