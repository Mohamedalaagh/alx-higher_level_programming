#!/usr/bin/python3
"""
Unit tests for the Rectangle class in models.rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestRectangleArea(unittest.TestCase):
    """ Test the area method for the Rectangle class in models.rectangle """

    def test_area_positive_integers(self):
        """ Test with positive integers for width and height """
        rectangle = Rectangle(3, 5)
        self.assertEqual(rectangle.area(), 15)

    def test_area_float_width_int_height(self):
        """ Test with float for width and int for height"""
        with self.assertRaises(TypeError):
            rectangle = Rectangle(0.3, 5)
            rectangle.area()

    def test_area_int_width_float_height(self):
        """ Test with int for width and float for height """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(3, 0.5)
            rectangle.area()

    def test_area_zero_width_int_height(self):
        """ Test with 0 for width and int for height """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 5)
            rectangle.area()

    def test_area_int_width_zero_height(self):
        """ Test with int for width and 0 for height """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(3, 0)
            rectangle.area()

    def test_area_negative_width_int_height(self):
        """ Test with negative for width and int for height """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-3, 5)
            rectangle.area()

    def test_area_negative_width_negative_height(self):
        """ Test with negative for width and height """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-3, -5)
            rectangle.area()

    def test_area_single_arg_width(self):
        """ Test with 1 arg for width """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(3)
            rectangle.area()

    def test_area_no_args(self):
        """ Test without any args """
        with self.assertRaises(TypeError):
            rectangle = Rectangle()
            rectangle.area()

    def test_area_args_None(self):
        """ Test with arg None """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(None)
            rectangle.area()

    def test_area_function_width_int_height(self):
        """ Test with function for width and int for height """
        with self.assertRaises(UnboundLocalError):
            rectangle = Rectangle(rectangle.area(), 6)
            rectangle.area()

    def test_area_strings(self):
        """ Test with strings for width and height """
        with self.assertRaises(TypeError):
            rectangle = Rectangle("Hello!", "World")
            rectangle.area()

    def test_area_tuples(self):
        """ Test with tuples for width and height """
        with self.assertRaises(TypeError):
            rectangle = Rectangle((1, 2, 3), (1, 2, 3))
            rectangle.area()

    def test_area_lists(self):
        """ Test with lists for width and height """
        with self.assertRaises(TypeError):
            rectangle = Rectangle([1, 2, 3], [1, 2, 3])
            rectangle.area()

    def test_area_dicts(self):
        """ Test with dictionaries for width and height """
        with self.assertRaises(TypeError):
            rectangle = Rectangle({1, 2, 3}, {1, 2, 3})
            rectangle.area()

    def test_area_float_inf_width_int_height(self):
        """ Test with float("inf") for width and int for height """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(float("inf"), 3)
            rectangle.area()

    def test_area_float_nan_width_int_height(self):
        """ Test with float("Nan") for width and int for height """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(float("NaN"), 5)
            rectangle.area()

    def test_area_None_args(self):
        """ Test with None for args """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(None, None)
            rectangle.area()

    def test_area_string_width_int_height(self):
        """ Test with string for width and int for height """
        with self.assertRaises(TypeError):
            rectangle = Rectangle("Hello!", 5)
            rectangle.area()

    def test_area_int_width_string_height(self):
        """ Test with int for width and string for height """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(3, "World")
            rectangle.area()

    def test_area_single_string_arg(self):
        """ Test with 1 string as the only argument """
        with self.assertRaises(TypeError):
            rectangle = Rectangle("Hello!")
            rectangle.area()

    def test_area_method_call(self):
        """ Test with method call instead of creating an instance """
        with self.assertRaises(TypeError):
            Rectangle.area()


if __name__ == "__main__":
    unittest.main()

