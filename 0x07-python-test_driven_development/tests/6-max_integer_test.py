#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer using unittest module"""

    def test_all_positive_int_list(self):
        """test a list of allpositive element"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_all_negative_integers_list(self):
        """testing a list of all megative numbers"""
        self.assertEqual(max_integer([-2, -1, -4, -8]), -1)

    def test_mix_of_positive_and_negatives(self):
        """testing a list contain a mixture of positive / negative numbers"""
        self.assertEqual(max_integer([3, -1, 5, -8]), 5)

    def test_list_of_floats(self):
        """testing a list of floats"""
        self.assertEqual(max_integer([4.5, 1.7, 2.0, 4.6]), 4.6)

    def test_with_no_arguments(self):
        """testing a function max_integer with no argument passing"""
        self.assertEqual(max_integer(), None)

    def test_string(self):
        """Test a string."""
        string = "Ehoneah"
        self.assertEqual(max_integer(string), 'o')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Ehoneah", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
