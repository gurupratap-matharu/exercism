def convert(number):
    """
    Converts a number into string based on rain drops methodj
    Pling = if 3 is a factor
    Plang = if 5 is a factor
    Plong = if 7 is a factor
    the number itself if none of the above are factors.
    """
    raindrops = ''
    r_3 = divmod(number, 3)[1]
    r_5 = divmod(number, 5)[1]
    r_7 = divmod(number, 7)[1]

    if r_3 != 0 and r_5 != 0 and r_7 != 0:
        return str(number)
    if r_3 == 0:
        raindrops += 'Pling'
    if r_5 == 0:
        raindrops += 'Plang'
    if r_7 == 0:
        raindrops += 'Plong'

    return raindrops


if __name__ == '__main__':
    print(convert(8))
