import unittest

from pangram import is_pangram


class PangramTest(unittest.TestCase):
    """Out test class holds all the methods for verifying is the given argument string is a pangram or no."""

    def test_empty_string(self):
        self.assertIs(is_pangram(''), False)

    def test_all_lower_case_perfect_string(self):
        self.assertIs(is_pangram('abcdefghijklmnopqrstuvwxyz'), True)

    def test_all_upper_case_string(self):
        self.assertIs(is_pangram('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), True)

    def test_missing_only_one_character(self):
        self.assertIs(is_pangram('abcdefghijklmnopqrstuvwxy'), False)

    def test_string_with_puncutation_marks(self):
        self.assertIs(is_pangram('A!@bcDEF$%^ghiJKLm)((nOPPPQQQrstuvWxy&*((>?":<MM~!@~~``@z:"{}||}{+_)_(_*&*(^*%('), True)

    def test_string_with_mixed_caps(self):
        self.assertIs(is_pangram('ZZZzzzzXXxxCCccvvVVbbNNmmLLkkjjHHGGffggDDddssAAAqqwwEEEeeRRrrttTTyyYYYuuUUiiOOpp'), True)

    def test_complex_string_with_long_length(self):
        self.assertIs(is_pangram("""Today was a difficult day. Golu but you still handed it really well. Days like these pass and all you
can do is to keep yourself occupied and look ahead for better times.
To handle so much solitude all alone make you tougher from inside and it's changing you but heroes
don't complain.
Everybody in our family has problems and difficulties. You are not the only one. Inface you are not
having any major responsibility.
God. Please give me some.
Universe is a very strange place. It doesn't work according to our thoughts or feelings and neither we
are the center of it. This is a hard fact and we should accept is Now.
Nothing really matter in the end and when your life will be coming to an end Golu do you think the
problems you think you have in Argentina will even matter?
Think about it for a second.

What happened to you in school, infosys or prasad is the past and you don't remember anything now. Correct? So what do you fear? Just be yourself and do as much as you can with a good hardworking attitude.
All rest will fall into place.
Don't let some small failures affect you as you have gained so much here. Do not procrastinate and work
very hard. Let's accept this right now itself.
ACTIONS SPEAK A THOUSAND TIMES LOUDER THAN WORDS.
We should be acting fast and quick without wasting minutes. This is it.

From this moment onwards. Stop crumbling and start acting towards your dreams and goals. Take small steps no matter how small they are. You are good at learning and taking criticism. Thinks will click in no time. Be fearless and bold. You are a courageous man. So don't let anything deter you.

Act on small things that you learn rather than putting things on the back burner. It's really now in themoment or never. Life is really what is happening to us now.
I don't have much to say here as you already know a lot. We are together in this. Lets fight it out together. Now go and take rest.
I'm with you.

Your inner voice.
"""), False)

    def test_sentence_empty(self):
        self.assertIs(is_pangram(''), False)

    def test_recognizes_a_perfect_lower_case_pangram(self):
        self.assertIs(is_pangram('abcdefghijklmnopqrstuvwxyz'), True)

    def test_pangram_with_only_lower_case(self):
        self.assertIs(
            is_pangram('the quick brown fox jumps over the lazy dog'),
            True)

    def test_missing_character_x(self):
        self.assertIs(
            is_pangram('a quick movement of the enemy will '
                       'jeopardize five gunboats'),
            False)

    def test_another_missing_character(self):
        self.assertIs(is_pangram('five boxing wizards jump quickly at it'),
                      False)

    def test_pangram_with_underscores(self):
        self.assertIs(
            is_pangram('the_quick_brown_fox_jumps_over_the_lazy_dog'),
            True)

    def test_pangram_with_numbers(self):
        self.assertIs(
            is_pangram('the 1 quick brown fox jumps over the 2 lazy dogs'),
            True)

    def test_missing_letters_replaced_by_numbers(self):
        self.assertIs(
            is_pangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'),
            False)

    def test_pangram_with_mixedcase_and_punctuation(self):
        self.assertIs(
            is_pangram('"Five quacking Zephyrs jolt my wax bed."'),
            True)

    def test_upper_and_lower_case_versions_of_the_same_character(self):
        self.assertIs(
            is_pangram('the quick brown fox jumped over the lazy FX'),
            False)


if __name__ == '__main__':
    unittest.main()
