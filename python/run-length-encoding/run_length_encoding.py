def decode(string):
    """Decodes a rle string into normal format"""

    rle = ''
    run = 1
    loop = False
    for char in string:

        if char.isalpha() or char.isspace():
            rle += run * char
            run = 1
            loop = False

        elif char.isdigit():

            if loop:
                run = int(str(run) + char)
            else:
                run = int(char)
                loop = True
    return rle


def encode(string):
    """Encodes a normal string into rle format"""

    if string == '':
        return ''
    rle = ''
    count = 0
    current_letter = string[0]

    for char in string:

        if char == current_letter:
            count += 1
        else:
            if count == 1:
                rle += current_letter
            else:
                rle += str(count) + current_letter
            current_letter = char
            count = 1

    if count == 1:
        rle += current_letter
    else:
        rle += str(count) + current_letter
    return rle
