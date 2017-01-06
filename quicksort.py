from random import randint


class QuickSort(list):
    def __init__(self, *args, **kwargs):
        # noinspection PyTypeChecker
        list.__init__(self, *args)
        self.comparisons = 0
        if not kwargs:
            self.pivot = 'random'
        else:
            self.pivot = kwargs['pivot']
        self.quicksort()

    def quicksort(self, start=0, end=None):
        if len(self) < 2:
            return

        if end is None:
            end = len(self) - 1

        i = self.partition(start, end)

        if start < i - 1:
            self.quicksort(start, i - 1)

        if i + 1 < end:
            self.quicksort(i + 1, end)

    def partition(self, start, end):
        self.comparisons += end - start

        pivot = self._get_pivot(start, end)

        swap(self, start, pivot)
        pivot_value = self[start]

        border = marker = start + 1

        while marker <= end:
            marker_value = self[marker]
            if marker_value <= pivot_value:
                swap(self, border, marker)
                border += 1
            marker += 1

        swap(self, start, border - 1)
        return border - 1

    def _get_pivot(self, start, end):
        first = 'first'
        last = 'last'
        median = 'median'
        random = 'random'

        if self.pivot not in [first, last, median, random]:
            raise ValueError("Invalid pivot selection strategy.")

        if self.pivot == first:
            return start
        elif self.pivot == last:
            return end
        elif self.pivot == median:
            return median_of_three(self, start, end)
        elif self.pivot == random:
            return randint(start, end)


def median_of_three(array, start, end):
    diff = end - start + 1
    if diff % 2:
        mid = start + (diff / 2)
    else:
        mid = start + (diff / 2) - 1

    sub = [(array[start], start), (array[mid], mid), (array[end], end)]
    sub.sort()

    return sub[1][1]


def quicksort(array, start=0, end=None):
    if len(array) < 2:
        return array

    if end is None:
        end = len(array) - 1

    i = partition(array, start, end)

    if start < i - 1:
        quicksort(array, start, i - 1)

    if i + 1 < end:
        quicksort(array, i + 1, end)

    return array


def partition(array, start, end, pivot=None):
    if pivot is None:
        pivot = randint(start, end)

    swap(array, start, pivot)
    pivot_value = array[start]

    border = marker = start + 1

    while marker <= end:
        marker_value = array[marker]
        if marker_value <= pivot_value:
            swap(array, border, marker)
            border += 1
        marker += 1

    swap(array, start, border - 1)
    return border - 1


def swap(l, a, b):
    l[a], l[b] = l[b], l[a]
