"""A utility script to validate if all brackets in a string are correctly matched."""


class StringParser:
    """A string utility class to validate if all brackets are correctly matched"""

    def has_valid_brackets(self, text: str) -> bool:
        """
        Validates if all the brackets in the string are correctly paired.
        """

        stack = []
        bracket_map = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        for char in text:
            if char in bracket_map:
                # 1 closing bracket

                    return False

            else:
                stack.append(char)

        if stack:
            return False
        return True


if __name__ == '__main__':
    parser = StringParser()
    # assert parser.has_valid_brackets('()[]{}'), True
    # assert parser.has_valid_brackets('({[]})'), True
    assert not parser.has_valid_brackets('({)')
