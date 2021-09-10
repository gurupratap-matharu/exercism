class Parser:
    def is_repeated_string_pattern(self, s: str) -> bool:
        """
        Determines if a string can be resconstructed by simply
        adding one of its own substrings

        In other words if it has a repeated pattern of a substring
        inside it.
        """

        length = len(s)

        for i in range(1, length):
            repeated_sub_string = s[:i] * (length // i)
            if repeated_sub_string == s:
                return True
        return False


if __name__ == '__main__':
    obj = Parser()
    obj.is_repeated_string_pattern('abcdabcd')
