"""Script to reverse only vowels in a string"""


class StringUtils:
    """Multi purpose string transformation class"""

    def reverse_vowels(self, text: str) -> str:
        """
        Reverses only the vowels of a string using
        the two pointer technique.

        Ex:
            'hello' -> 'holle'
            'leetcode' -> 'leotcede'
        """

        text = list(text)

        i, j = 0, len(text) - 1
        is_vowel = lambda x: x.lower() in "aeiou"

        while i < j:

            is_left_vowel = is_vowel(text[i])
            is_right_vowel = is_vowel(text[j])

            if is_left_vowel and is_right_vowel:
                # perform the swap
                text[i], text[j] = text[j], text[i]
                i += 1
                j -= 1

            if not is_left_vowel:
                i += 1

            if not is_right_vowel:
                j -= 1

        return "".join(text)


if __name__ == "__main__":
    print(StringUtils().reverse_vowels("hello"))
    print(StringUtils().reverse_vowels("leetcode"))
