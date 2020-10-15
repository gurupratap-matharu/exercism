BRACKET_PAIRS = {
    "(": ")",
    "{": "}",
    "[": "]"
}


def are_brackets_matched(chunk):
    """
    Tells us whether the chunk has all the brackets matched correctly.
    Returns a boolean.
    """
    stack = []

    for char in chunk:

        # its a closing bracket
        if char in BRACKET_PAIRS.values():

            if not stack:
                return False

            most_recent_bracket = stack.pop()

            if most_recent_bracket in BRACKET_PAIRS.keys() and BRACKET_PAIRS[most_recent_bracket] == char:
                continue
            else:
                return False

        # it's an opening bracket
        elif char in BRACKET_PAIRS.keys():
            stack.append(char)

            # it's not at all a bracket
        else:
            continue

    return not stack


if __name__ == '__main__':
    assert are_brackets_matched('{{{{{}}}}}((())){()}') == True
