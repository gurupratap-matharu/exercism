"""Testing script for dynamic programming calculation of climbing stairs"""


import unittest

from min_cost import Stairs


class StairsTests(unittest.TestCase):
    """Test Suite for climbing stairs"""

    def test_cost_of_climbing_medium_steps(self):
        calculated = Stairs().min_cost_of_climbing_stairs(
            cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        )
        expected = 6

        self.assertEqual(calculated, expected)


if __name__ == "__main__":
    unittest.main()
