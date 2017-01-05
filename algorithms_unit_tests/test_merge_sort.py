import random
import unittest

from algorithms.merge_sort import merge_sort


class Test_Merge_Sort(unittest.TestCase):
    def test_smallest_case(self):
        unsorted = [3, 1]
        expected = [1, 3]

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)

    def test_smallest_merge_sort(self):
        unsorted = [8, 1, 6, 3]
        expected = [1, 3, 6, 8]

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)

    def test_larger_case(self):
        unsorted = [8, 4, 6, 2, 7, 3, 5, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)

    def test_already_sorted_ish(self):
        unsorted = [1, 3, 2, 4, 6, 5, 8, 7]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)

    def test_odd_man(self):
        unsorted = [1, 3, 5, 4, 2]
        expected = [1, 2, 3, 4, 5]

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)

    def test_mostly_the_same(self):
        unsorted = [2, 2, 2, 2, 2, 2, 2, 1]
        expected = [1, 2, 2, 2, 2, 2, 2, 2]

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)

    def test_mulitple_sames(self):
        unsorted = [2, 1, 2, 2, 4, 3, 3, 3]
        expected = [1, 2, 2, 2, 3, 3, 3, 4]

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)

    def test_nothing(self):
        unsorted = []
        expected = []

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)

    def test_random_and_small(self):
        expected = range(100)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)

    def test_random_and_small_a_bunch_of_times(self):
        for _ in range(100):
            expected = range(100)
            unsorted = list(expected)
            random.shuffle(unsorted)

            actual = merge_sort(unsorted)

            self.assertEqual(expected, actual)

    def test_random_and_big(self):
        expected = range(10000)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = merge_sort(unsorted)

        self.assertEqual(expected, actual)
