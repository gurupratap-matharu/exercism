import unittest

from brackets import are_brackets_matched


class BracketsTests(unittest.TestCase):
    """Unit test class where different test cases are defined in the form of methods"""

    def test_empty_string(self):
        self.assertTrue(are_brackets_matched(''))

    def test_valid_small_string(self):
        self.assertTrue(are_brackets_matched('({})'))

    def test_invalid_small_string(self):
        self.assertFalse(are_brackets_matched('({]'))

    def test_valid_large_string(self):
        self.assertTrue(are_brackets_matched('(((([[[[{{{{}}}}]]]]))))'))

    def test_invalid_large_string(self):
        self.assertFalse(are_brackets_matched('(((([[[{{{}}}]]]'))

    def test_string_with_numeric_characters(self):
        self.assertTrue(are_brackets_matched('345{}5436[](){}5556'))

    def test_tricky_invalid_string(self):
        self.assertFalse(are_brackets_matched('(((({{{{[[[[()]]]]}}}})))'))

    def test_integer_input_raises_type_error(self):
        chunk = 234523654436545
        with self.assertRaises(TypeError):
            result = are_brackets_matched(chunk)

    def test_boolean_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            result = are_brackets_matched(True)

    def test_list_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            result = are_brackets_matched(['(', ')'])

    def test_tuple_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            result = are_brackets_matched(('[', ']'))


if __name__ == '__main__':
    unittest.main()
