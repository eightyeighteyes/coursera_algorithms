import unittest

from algorithms.count_inversions import sort_and_count_inversions, count_inversions


class Test_InversionCounting(unittest.TestCase):
    def test_smallest_case(self):
        self.assertEqual(1, count_inversions([2, 1]))
        self.assertEqual(0, count_inversions([1, 2]))


class Test_SortAndCount(unittest.TestCase):
    def test_smallest_case(self):
        self.assertEqual((1, [1, 2]), sort_and_count_inversions([2, 1]))
        self.assertEqual((0, [1, 2]), sort_and_count_inversions([1, 2]))

    def test_basic_split_case(self):
        self.assertEqual((1, [1, 2, 3, 4]), sort_and_count_inversions([1, 3, 2, 4]))

    def test_larger_split_case(self):
        self.assertEqual((3, [1, 2, 3, 4, 5, 6]), sort_and_count_inversions([1, 3, 5, 2, 4, 6]))

    def test_total_inversion(self):
        unsorted = [8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        self.assertEqual((28, expected), sort_and_count_inversions(unsorted))
