"""A Utility script to do conversions between roman numbers and their modern equivalent integers"""

import re


class Converter:
    """Utility class for coverting numbers"""

    CHAR_VALUE = [('CM', 900), ('CD', 400),
                  ('XC', 90), ('XL', 40),
                  ('IX', 9), ('IV', 4),
                  ('M', 1000), ('D', 500),
                  ('C', 100), ('L', 50),
                  ('X', 10), ('V', 5), ('I', 1)]

    def roman_to_integer(self, roman: str) -> int:
        """
        Converts a roman string to its equivalent integer.
        """

        value = 0

        if not self._is_valid_roman_numeral(roman):
            return value

        while roman:
            for s, v in self.CHAR_VALUE:
                if roman.startswith(s):
                    roman = roman.removeprefix(s)
                    value += v
                    break

        return value

    def _is_valid_roman_numeral(self, roman_literal=None):
        """Internal method to validate if a roman literal is valid or not"""

        regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
        result = bool(re.search(regex_pattern, roman_literal))
        return result


if __name__ == '__main__':
    converter = Converter()
    assert converter.roman_to_integer("MCMXCIV"), 1994
