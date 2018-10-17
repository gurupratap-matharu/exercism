import unittest

from acronym import abbreviate

# Now we write the class which will include all our tests.


class AcronymTest(unittest.TestCase):
    """Unit test class where different test cases are defined in the form of methods"""

    def test_basic(self):
        self.assertEqual(abbreviate('Buenos Aires Ciudad'), 'BAC')

    def test_lowercase_words(self):
        self.assertEqual(abbreviate("too long didn't read"), 'TLDR')

    def test_punctuation(self):
        self.assertEqual(abbreviate("O'Lord Almighty, the Only one."), 'OATOO')

    def test_all_caps_words(self):
        self.assertEqual(abbreviate('WHAT YOU SEE IS WHAT YOU GET'), 'WYSIWYG')

    def test_punctuation_without_whitespace(self):
        self.assertEqual(abbreviate('document-object-model'), 'DOM')

    def test_very_long_abbreviation(self):
        self.assertEqual(abbreviate('Last Friday Night We Did it all again, Thank God its Friday'), 'LFNWDIAATGIF')


if __name__ == '__main__':
    unittest.main(exit=False)
