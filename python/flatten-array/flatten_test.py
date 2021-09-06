import unittest

from flatten import flattener


class FlattenTests(unittest.TestCase):
    def test_single_small_nested_list(self):
        calculated = flattener([1, [2, 3]])
        expected = [1, 2, 3]
        self.assertEqual(calculated, expected)


if __name__ == "__main__":
    unittest.main()
