"""A script that converts excel sheet's column numbers to their title equivalent"""

import string


class Excel:
    """Utility class to get useful info about excel files."""

    def convertToTitle(self, columnNumber: int) -> str:
        """
        Converts an excel sheet column number to its title equivalent
        """

        char_map = dict(zip(range(1, 27), string.ascii_uppercase))
        print("char_map: ", char_map)

        chars = []

        while columnNumber > 26:
            columnNumber, rem = divmod(columnNumber, 26)
            chars.append(char_map.get(rem))

        chars.append(char_map.get(columnNumber))
        print('chars: ', chars)

        return "".join(reversed(chars))

if __name__=='__main__':
    print(Excel().convertToTitle(52))
