"""A utility script to identify if a pair of strings can break each other or not."""


class Breaker:
    """Main class to handle strings and see their compatibility"""

    def check_if_can_break(self, sentence_1: str, sentence_2: str) -> bool:
        """
        Checks if all possible permutations of both s1 and s2
        can break each other or not.
        """
        sentence_1 = ''.join(sorted(sentence_1))
        sentence_2 = ''.join(sorted(sentence_2))

        is_s1_dominant = all(i >= j for i, j in zip(sentence_1, sentence_2))
        is_s2_dominant = all(j >= i for i, j in zip(sentence_1, sentence_2))

        return is_s1_dominant or is_s2_dominant


if __name__ == '__main__':
    breaker = Breaker()
    assert breaker.check_if_can_break(sentence_1='abc', sentence_2='xya'), True
