import unittest

from contains_duplicates import Solution


class ContainsDuplicateTests(unittest.TestCase):
    """Test suite to check if all duplicates are caught correctly"""

    def test_small_list_with_unique_numbers(self):
        self.assertFalse(Solution().contains_duplicate([1, 2, 3]))

    def test_small_list_with_duplicate_numbers(self):
        self.assertTrue(Solution().contains_duplicate([1, 2, 3, 3]))

    def test_medium_list_with_unique_numbers(self):
        self.assertFalse(Solution().contains_duplicate([x for x in range(1, 50)]))

    def test_medium_list_with_duplicate_numbers(self):
        self.assertTrue(
            Solution().contains_duplicate([x for x in range(1, 50)] + [49, 50])
        )

    def test_large_list_with_unique_numbers(self):
        self.assertFalse(Solution().contains_duplicate([x for x in range(1, 50000)]))

    def test_large_list_with_only_one_duplicate_number(self):
        self.assertTrue(
            Solution().contains_duplicate([x for x in range(1, 50000)] + [49999])
        )


if __name__ == "__main__":
    unittest.main()
