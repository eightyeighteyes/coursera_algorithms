import unittest

from algorithms.karatsuba import karatsuba


class test_karatsuba(unittest.TestCase):
    def test_smallest_case(self):
        self.assertEqual(25, karatsuba(5, 5))

    def test_double_digits(self):
        self.assertEqual(408, karatsuba(12, 34))

    def test_triples_digits(self):
        self.assertEqual(56088, karatsuba(123, 456))

    def test_base_mismatch_between_args(self):
        self.assertEqual(70077626, karatsuba(1234, 56789))

    def test_something_random(self):
        self.assertEqual(1082152022374638, karatsuba(12345678, 87654321))
