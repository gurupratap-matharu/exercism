"""Testing script to check edge cases to identify the first bad version in the product upgrades"""


import unittest

from first_bad_version import Solution


class FirstBadVersionTests(unittest.TestCase):
    """Test suite for First Bad Version class"""

    def test_single_bad_version(self):
        s = Solution(bad_entry=1)
        self.assertEqual(s.first_bad_version(1), 1)

    def test_small_set_of_versions_with_late_bad_version(self):
        s = Solution(bad_entry=4)
        self.assertEqual(s.first_bad_version(5), 4)

    def test_small_set_of_versions_with_early_bad_version(self):
        s = Solution(bad_entry=2)
        self.assertEqual(s.first_bad_version(10), 2)

    def test_large_set_of_versions_with_late_bad_version(self):
        s = Solution(bad_entry=98)
        self.assertEqual(s.first_bad_version(100), 98)


if __name__ == "__main__":
    unittest.main()
