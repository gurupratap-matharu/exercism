
def numeral(number):
    """Returs a roman numeral for an integer."""

    to_roman = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                2000: 'MM', 3000: 'MMM'}

    roman_numeral = []

    count = 1

    # We travel the number from the left and add corresponding values from the to_roman
    # dictionary

    for digit in str(number)[::-1]:

        digit = int(digit)
        i = to_roman.get(digit * count)
        roman_numeral.append(i)
        count *= 10

    return ''.join(roman_numeral[::-1])
