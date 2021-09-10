"""A utility script to validate if all brackets in a string are correctly matched."""


class StringParser:
    """A string utility class to validate if all brackets are correctly matched"""

    def has_valid_brackets(self, text: str) -> bool:
        """
        Validates if all the brackets in the string are correctly paired.
        """
        pass


if __name__ == '__main__':
    parser = StringParser()
    assert parser.has_valid_brackets('()[]{}'), True
    assert parser.has_valid_brackets('({[]})'), True
    assert parser.has_valid_brackets('({)'), False
