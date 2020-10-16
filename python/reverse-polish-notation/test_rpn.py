import unittest

from rpn import evaluate_rpn


class RPNTests(unittest.TestCase):
    def test_addition_of_two_numbers(self):
        self.assertEqual(evaluate_rpn('4 7 +'), 11)

    def test_subtraction_of_two_numbers(self):
        self.assertEqual(evaluate_rpn('7 4 -'), 3)

    def test_multiplication_of_two_numbers(self):
        self.assertEqual(evaluate_rpn('5 8  *'), 40)

    def test_floor_division_of_two_numbers(self):
        self.assertEqual(evaluate_rpn('5 2 //'), 2)

    def test_negation_of_a_number(self):
        self.assertEqual(evaluate_rpn('40 n'), -40)

    def test_exponential_of_two_numbers(self):
        self.assertEqual(evaluate_rpn('6 2 e'), 36)
