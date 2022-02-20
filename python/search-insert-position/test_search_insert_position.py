import unittest

from search_insert_position import Solution


class SearchInsertPositionTests(unittest.TestCase):
    """Test suite for Search Insert Position class"""

    def test_array_with_single_target_element(self):
        nums = [1]
        target = 1
        calculated = Solution().search_insert(nums, target)
        expected = 0
        self.assertEqual(calculated, expected)

    def test_array_with_single_non_target_element(self):
        nums = [1]
        target = -1
        calculated = Solution().search_insert(nums, target)
        expected = 0
        self.assertEqual(calculated, expected)

    def test_small_array_with_target(self):
        nums = [1, 2, 3, 4]
        target = 3
        calculated = Solution().search_insert(nums, target)
        expected = 2
        self.assertEqual(calculated, expected)

    def test_small_array_without_target(self):
        nums = [1, 2, 4, 5]
        target = 3
        calculated = Solution().search_insert(nums, target)
        expected = 2
        self.assertEqual(calculated, expected)

    def test_small_array_without_target_with_all_elements_less_than_target(self):
        nums = [1, 2, 3, 4]
        target = 5
        calculated = Solution().search_insert(nums, target)
        expected = 4
        self.assertEqual(calculated, expected)

    def test_small_array_without_target_with_all_elements_greater_than_target(self):
        nums = [1, 2, 3, 4]
        target = -1
        calculated = Solution().search_insert(nums, target)
        expected = 0
        self.assertEqual(calculated, expected)

    def test_medium_array_with_target(self):
        nums = [x for x in range(1, 50, 2)]
        target = 19
        calculated = Solution().search_insert(nums, target)
        expected = 9
        self.assertEqual(calculated, expected)

    def test_medium_array_without_target(self):
        nums = [x for x in range(1, 50, 2)]
        target = 20
        calculated = Solution().search_insert(nums, target)
        expected = 10
        self.assertEqual(calculated, expected)

    def test_medium_array_without_target_and_all_elems_smaller_than_target(self):
        nums = [x for x in range(100)]
        target = 100
        calculated = Solution().search_insert(nums, target)
        expected = 100
        self.assertEqual(calculated, expected)

    def test_medium_array_without_target_and_all_elems_larger_than_target(self):
        nums = [x for x in range(100)]
        target = -1
        calculated = Solution().search_insert(nums, target)
        expected = 0
        self.assertEqual(calculated, expected)


if __name__ == "__main__":
    unittest.main()
