
import unittest
from MagicSort import (linear_scan, reverse_list,
                       insertionsort, quicksort, mergesort, magic_sort)

class TestLinearScan(unittest.TestCase):
    def test_reverse_sorted_list(self):
        # Test that a reverse sorted list returns "reverse_list"
        lst = [5, 4, 3, 2, 1]
        expected = "reverse_list"
        actual = linear_scan(lst)
        self.assertEqual(expected,actual)


def test_out_of_place_list(self):
    lst = [1, 4, 3, 2, 5, 7, 9, 6, 8, 10]
    expected_result = sorted(lst)
    actual_result = linear_scan(lst)
    self.assertEqual(expected_result, actual_result)

    def test_reverse_sorted_list(self):
        # Test that a reverse sorted list returns "reverse_list"
        lst = [5, 4, 3, 2, 1]
        expected = "reverse_list"
        actual = linear_scan(lst)
        self.assertEqual(expected, actual)


class Test_reverse_list(unittest.TestCase):
    def test_reverse_list(self):
        lst = [8, 3, 4, 5, 6, 2, 1, 7, 10, 9]
        reverse_list(lst)
        self.assertEqual(lst, [9, 10, 7, 1, 2, 6, 5, 4, 3, 8])


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        lst = [1, 7, 3, 5, 2, 4]
        expected = [1, 2, 3, 4, 5, 7]
        actual = insertionsort(lst, 0, len(lst))
        self.assertEqual(actual, expected)


class Test_mergesort(unittest.TestCase):
    def test_already_sorted(self):
        L = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(mergesort(L), expected)

    def test_reverse_list(self):
        L = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(mergesort(L), expected)


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        L = [6, 5, 4, 3, 2]
        expected = [2, 3, 4, 5, 6]
        actual = magic_sort(L)
        self.assertEqual(actual, expected)


def test_quicksort(self):
    L = [5, 2, 4, 1, 3]
    expected = [1, 2, 3, 4, 5]
    self.assertEqual(mergesort(L), expected)


class TestMagicSort(unittest.TestCase):
    def test_already_sorted(self):
        L = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(magic_sort(L), expected)

    def test_reverse_list(self):
        L = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(magic_sort(L), expected)

    def test_insertion_sort(self):
        L = [6, 5, 4, 3, 2]
        expected = [2, 3, 4, 5, 6]
        self.assertEqual(magic_sort(L), expected)

    def test_quicksort(self):
        L = [5, 2, 4, 1, 3]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(magic_sort(L), expected)

    def test_duplicate_items(self):
        L = [1, 2, 3, 2, 1]
        expected = [1, 1, 2, 2, 3]
        self.assertEqual(magic_sort(L), expected)

unittest.main()
