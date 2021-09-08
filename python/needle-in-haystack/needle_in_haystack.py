class NeedleHayStack:
    def find_index_of_needle_in_haystack(self, haystack: str, needle: str) -> int:
        """
        Returns the index of needle in the haystack.
        Returns -1 if needle is not present in the haystack
        Returns 0 if needle is an empty string.
        """
        needle_index = 0

        try:
            needle_index = haystack.index(needle)
        except ValueError:
            needle_index = -1

        return needle_index


if __name__ == '__main__':
    obj = NeedleHayStack()
    assert obj.find_index_of_needle_in_haystack(haystack='hello', needle='ll'), 2
    assert obj.find_index_of_needle_in_haystack(haystack='hello', needle='xy'), -1
