
def parse_text(text):
    """Parses the string by removing characters before each hash symbol"""

    stack = []

    for char in text:

        if char != '#':
            stack.append(char)

        else:
            if len(stack) > 0:
                stack.pop()

    return ''.join(stack)


def check_if_equal(text_1, text_2):
    """
    Checks if two strings are equal after parsing them with rules
    of hash character.
    """
    print(parse_text(text_1))
    print(parse_text(text_2))

    return parse_text(text_1) == parse_text(text_2)


if __name__ == '__main__':
    assert check_if_equal('xy#z', 'xw#z') == True
    assert check_if_equal('abcd##', 'acbd##') == False
    assert check_if_equal('z##y', '#d#y') == True
    assert check_if_equal('er##', 'u#u#') == True
