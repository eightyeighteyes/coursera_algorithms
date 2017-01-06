import os
import random
import unittest

from algorithms.quicksort import quicksort, partition, swap, median_of_three, QuickSort

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')


class Test_Quicksort(unittest.TestCase):
    def test_single_element(self):
        actual = [1]
        expected = [1]

        quicksort(actual)

        self.assertEqual(expected, actual)

    def test_basic_case(self):
        unsorted = [3, 8, 2, 5, 1, 4, 7, 6]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        actual = quicksort(unsorted)

        self.assertEqual(expected, actual)

    def test_already_sorted_ish(self):
        unsorted = [1, 3, 2, 4, 6, 5, 8, 7]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        actual = quicksort(unsorted)

        self.assertEqual(expected, actual)

    def test_odd_man(self):
        unsorted = [1, 3, 5, 4, 2]
        expected = [1, 2, 3, 4, 5]

        actual = quicksort(unsorted)

        self.assertEqual(expected, actual)

    def test_mostly_the_same(self):
        unsorted = [2, 2, 2, 2, 2, 2, 2, 1]
        expected = [1, 2, 2, 2, 2, 2, 2, 2]

        actual = quicksort(unsorted)

        self.assertEqual(expected, actual)

    def test_mulitple_sames(self):
        unsorted = [2, 1, 2, 2, 4, 3, 3, 3]
        expected = [1, 2, 2, 2, 3, 3, 3, 4]

        actual = quicksort(unsorted)

        self.assertEqual(expected, actual)

    def test_nothing(self):
        unsorted = []
        expected = []

        actual = quicksort(unsorted)

        self.assertEqual(expected, actual)

    def test_random_and_small(self):
        expected = range(100)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = quicksort(unsorted)

        self.assertEqual(expected, actual)

    def test_random_and_small_a_bunch_of_times(self):
        for _ in range(100):
            expected = range(100)
            unsorted = list(expected)
            random.shuffle(unsorted)

            actual = quicksort(unsorted)

            self.assertEqual(expected, actual)

    def test_random_and_big(self):
        expected = range(10000)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = quicksort(unsorted)

        self.assertEqual(expected, actual)


class Test_Partition(unittest.TestCase):
    def test_index_0(self):
        array = [3, 8, 2, 5, 1, 4, 7, 6]
        start = 0
        end = len(array) - 1

        i = partition(array, start, end, pivot=0)
        expected_i = 2
        expected_border = 3

        self.assertEqual(expected_i, i)

        self.assertEqual(expected_border, array[expected_i])
        for n in array[:expected_i]:
            self.assertLess(n, expected_border)

        for n in array[expected_i + 2:]:
            self.assertGreater(n, expected_border)

    def test_index_1(self):
        array = [3, 8, 2, 5, 1, 4, 7, 6]
        start = 0
        end = len(array) - 1

        i = partition(array, start, end, pivot=1)
        expected_i = 7
        expected_border = 8

        self.assertEqual(expected_i, i)

        self.assertEqual(expected_border, array[expected_i])
        for n in array[:expected_i]:
            self.assertLess(n, expected_border)

        for n in array[expected_i + 2:]:
            self.assertGreater(n, expected_border)

    def test_index_2(self):
        array = [3, 8, 2, 5, 1, 4, 7, 6]
        start = 0
        end = len(array) - 1

        i = partition(array, start, end, pivot=2)
        expected_i = 1
        expected_border = 2

        self.assertEqual(expected_i, i)

        self.assertEqual(expected_border, array[expected_i])
        for n in array[:expected_i]:
            self.assertLess(n, expected_border)

        for n in array[expected_i + 2:]:
            self.assertGreater(n, expected_border)


class Test_Swap(unittest.TestCase):
    def test_basic_swap(self):
        actual = [1, 2, 3, 4, 5, 6]
        expected = [6, 2, 3, 4, 5, 1]

        swap(actual, 0, 5)

        self.assertEqual(expected, actual)


class Test_Median_of_Three(unittest.TestCase):
    def test_first_is_median(self):
        array = [2, 1, 0, 3, 4]
        median = median_of_three(array, 0, 4)
        self.assertEqual(0, median)

    def test_mid_is_median(self):
        array = [0, 1, 2, 3, 4]
        median = median_of_three(array, 0, 4)
        self.assertEqual(2, median)

    def test_end_is_median(self):
        array = [4, 1, 0, 3, 2]
        median = median_of_three(array, 0, 4)
        self.assertEqual(4, median)

    def test_even_array_elements(self):
        array = [8, 2, 4, 5, 7, 1]
        median = median_of_three(array, 0, 6)
        self.assertEqual(2, median)


class Test_QuickSort_Obj(unittest.TestCase):
    def test_single_element(self):
        unsorted = [1]
        expected = [1]

        actual = QuickSort(unsorted)

        self.assertEqual(expected, actual)

    def test_basic_case(self):
        unsorted = [3, 8, 2, 5, 1, 4, 7, 6]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        actual = QuickSort(unsorted)

        self.assertEqual(expected, actual)

    def test_already_sorted_ish(self):
        unsorted = [1, 3, 2, 4, 6, 5, 8, 7]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        actual = QuickSort(unsorted)

        self.assertEqual(expected, actual)

    def test_odd_man(self):
        unsorted = [1, 3, 5, 4, 2]
        expected = [1, 2, 3, 4, 5]

        actual = QuickSort(unsorted)

        self.assertEqual(expected, actual)

    def test_mostly_the_same(self):
        unsorted = [2, 2, 2, 2, 2, 2, 2, 1]
        expected = [1, 2, 2, 2, 2, 2, 2, 2]

        actual = QuickSort(unsorted)

        self.assertEqual(expected, actual)

    def test_mulitple_sames(self):
        unsorted = [2, 1, 2, 2, 4, 3, 3, 3]
        expected = [1, 2, 2, 2, 3, 3, 3, 4]

        actual = QuickSort(unsorted)

        self.assertEqual(expected, actual)

    def test_nothing(self):
        unsorted = []
        expected = []

        actual = QuickSort(unsorted)

        self.assertEqual(expected, actual)
        self.assertEqual(0, actual.comparisons)

    def test_random_and_small(self):
        expected = range(100)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted)

        self.assertEqual(expected, actual)

    def test_random_and_small_a_bunch_of_times(self):
        for _ in range(100):
            expected = range(100)
            unsorted = list(expected)
            random.shuffle(unsorted)

            actual = QuickSort(unsorted)

            self.assertEqual(expected, actual)

    def test_random_and_big(self):
        expected = range(10000)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted)

        self.assertEqual(expected, actual)

    def test_pivot_first(self):
        expected = range(100)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted, pivot='first')

        self.assertEqual(expected, actual)

    def test_pivot_first_large_data(self):
        expected = range(10000)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted, pivot='first')

        self.assertEqual(expected, actual)

    def test_pivot_last(self):
        expected = range(100)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted, pivot='last')

        self.assertEqual(expected, actual)

    def test_pivot_last_large_data(self):
        expected = range(10000)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted, pivot='last')

        self.assertEqual(expected, actual)

    def test_pivot_median(self):
        expected = range(100)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted, pivot='median')

        self.assertEqual(expected, actual)

    def test_pivot_median_large_data(self):
        expected = range(10000)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted, pivot='median')

        self.assertEqual(expected, actual)

    def test_pivot_random(self):
        expected = range(100)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted, pivot='random')

        self.assertEqual(expected, actual)

    def test_pivot_random_large_data(self):
        expected = range(10000)
        unsorted = list(expected)
        random.shuffle(unsorted)

        actual = QuickSort(unsorted, pivot='random')

        self.assertEqual(expected, actual)

    def test_pivot_invalid(self):
        expected = range(100)
        unsorted = list(expected)
        random.shuffle(unsorted)

        with self.assertRaises(ValueError):
            QuickSort(unsorted, pivot='invalid')


class Test_QuickSort_Obj_Pivots_On_Real_Data(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(DATA_PATH, 'quicksort.txt'), 'r') as data_file:
            test_data = data_file.readlines()

        self.data = [int(line.strip()) for line in test_data]

    def test_pivot_first_real_data(self):
        expected = range(1, 10001)
        actual = QuickSort(self.data, pivot='first')

        self.assertEqual(expected, actual)

    def test_pivot_last_real_data(self):
        expected = range(1, 10001)
        actual = QuickSort(self.data, pivot='last')

        self.assertEqual(expected, actual)

    def test_pivot_median_real_data(self):
        expected = range(1, 10001)
        actual = QuickSort(self.data, pivot='median')

        self.assertEqual(expected, actual)

    def test_pivot_random_real_data(self):
        expected = range(1, 10001)
        actual = QuickSort(self.data, pivot='random')

        self.assertEqual(expected, actual)


class Test_QuickSort_Obj_Pivots_DataSize_10(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(DATA_PATH, '10.txt'), 'r') as data_file:
            test_data = data_file.readlines()

        self.data = [int(line.strip()) for line in test_data]

    def test_pivot_first_10(self):
        expected_comparisons = 25
        actual_comparisons = QuickSort(self.data, pivot='first').comparisons

        self.assertEqual(expected_comparisons, actual_comparisons)

    def test_pivot_last_10(self):
        expected_comparisons = 29
        actual_comparisons = QuickSort(self.data, pivot='last').comparisons

        self.assertEqual(expected_comparisons, actual_comparisons)

    def test_pivot_median_10(self):
        expected_comparisons = 21
        actual_comparisons = QuickSort(self.data, pivot='median').comparisons

        self.assertEqual(expected_comparisons, actual_comparisons)


class Test_QuickSort_Obj_Pivots_DataSize_100(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(DATA_PATH, '100.txt'), 'r') as data_file:
            test_data = data_file.readlines()

        self.data = [int(line.strip()) for line in test_data]

    def test_pivot_first_100(self):
        expected_comparisons = 615
        actual_comparisons = QuickSort(self.data, pivot='first').comparisons

        self.assertEqual(expected_comparisons, actual_comparisons)

    def test_pivot_last_100(self):
        expected_comparisons = 587
        actual_comparisons = QuickSort(self.data, pivot='last').comparisons

        self.assertEqual(expected_comparisons, actual_comparisons)

    def test_pivot_median_100(self):
        expected_comparisons = 518
        actual_comparisons = QuickSort(self.data, pivot='median').comparisons

        self.assertEqual(expected_comparisons, actual_comparisons)


class Test_QuickSort_Obj_Pivots_DataSize_1000(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(DATA_PATH, '1000.txt'), 'r') as data_file:
            test_data = data_file.readlines()

        self.data = [int(line.strip()) for line in test_data]

    def test_pivot_first_1000(self):
        expected_comparisons = 10297
        actual_comparisons = QuickSort(self.data, pivot='first').comparisons

        self.assertEqual(expected_comparisons, actual_comparisons)

    def test_pivot_last_1000(self):
        expected_comparisons = 10184
        actual_comparisons = QuickSort(self.data, pivot='last').comparisons

        self.assertEqual(expected_comparisons, actual_comparisons)

    def test_pivot_median_1000(self):
        expected_comparisons = 8921
        actual_comparisons = QuickSort(self.data, pivot='median').comparisons

        self.assertEqual(expected_comparisons, actual_comparisons)
