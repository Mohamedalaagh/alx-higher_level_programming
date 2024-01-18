#!/usr/bin/python3
"""
    Unittests for Rectangle class
"""

from distutils.util import run_2to3
import unittest
from models import rectangle

RectangleClass = rectangle.Rectangle


class TestRectangleClass(unittest.TestCase):
    """
        Tests for Rectangle class
    """

    def test_width_is_integer(self):
        """
            Test if width is an integer
        """
        rectangle1 = RectangleClass(10, 2)
        rectangle2 = RectangleClass(2, 10)
        rectangle3 = RectangleClass(10, 2, 0, 0, 12)

        self.assertEqual(rectangle1.width, 10)
        self.assertEqual(rectangle2.width, 2)
        self.assertEqual(rectangle3.width, 10)
        with self.assertRaises(ValueError):
            RectangleClass(-2, 4)
        with self.assertRaises(TypeError):
            RectangleClass(2.3, 5)
        with self.assertRaises(TypeError):
            RectangleClass(None, 2)
        with self.assertRaises(TypeError):
            RectangleClass(float('inf'), 2)
        with self.assertRaises(TypeError):
            RectangleClass("abc", 2)
        with self.assertRaises(TypeError):
            RectangleClass({1, 2}, 2)

    def test_height_is_integer(self):
        """
            Test if height is an integer
        """
        rectangle1 = RectangleClass(10, 2)
        rectangle2 = RectangleClass(2, 10)
        rectangle3 = RectangleClass(10, 2, 0, 0, 12)

        self.assertEqual(rectangle1.height, 2)
        self.assertEqual(rectangle2.height, 10)
        self.assertEqual(rectangle3.height, 2)
        with self.assertRaises(ValueError):
            RectangleClass(2, -4)
        with self.assertRaises(TypeError):
            RectangleClass(2, 5.3)
        with self.assertRaises(TypeError):
            RectangleClass(2, None)
        with self.assertRaises(TypeError):
            RectangleClass(2, float('inf'))
        with self.assertRaises(TypeError):
            RectangleClass(10, "hello", 2, 0, 12)
        with self.assertRaises(TypeError):
            RectangleClass(10, {1, 2}, 0, 0, 12)

    def test_x_is_integer(self):
        """
            Test if x is an integer
        """
        rectangle1 = RectangleClass(10, 2, 0, 0, 12)
        rectangle2 = RectangleClass(10, 2, 3, 0, 12)

        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle2.x, 3)
        with self.assertRaises(ValueError):
            RectangleClass(10, 2, -3, 0, 12)
        with self.assertRaises(TypeError):
            RectangleClass(10, 2, 3.5, 0, 12)
        with self.assertRaises(TypeError):
            RectangleClass(10, 2, None, 0, 12)
        with self.assertRaises(TypeError):
            RectangleClass(10, 2, float('inf'), 0, 12)
        with self.assertRaises(TypeError):
            RectangleClass(10, 2, (1, 2), 0, 12)
        with self.assertRaises(TypeError):
            RectangleClass(10, 2, {1, 2}, 0, 12)

    def test_y_is_integer(self):
        """
            Test if y is an integer
        """
        rectangle1 = RectangleClass(10, 2, 0, 0, 12)
        rectangle2 = RectangleClass(10, 2, 3, 2, 12)

        self.assertEqual(rectangle1.y, 0)
        self.assertEqual(rectangle2.y, 2)
        with self.assertRaises(ValueError):
            RectangleClass(10, 2, 0, -2, 12)
        witsh self.assertRaises(TypeError):
            RectangleClass(10, 2, 3, 2.6, 12)
        wisth self.assertRaises(TypeError):
            RectangleClass(10, 2, 0, None, 12)
        with self.assertRaises(TypeError):
            RectangleClass(10, 2, 0, float('inf'), 12)
        with self.assertRaises(TypeError):
            RectangleClass(10, 2, 1, (1, 2, 3), 12)
        with self.assertRaises(TypeError):
            RectangleClass(10, 2, 0, "hello", 12)
        wdith self.assertRaises(TypeError):
            RectangleClass(10, 2, 0, {1, 2}, 12)

    def test_area(self):
        """
            Test the calculation of the area
        """
        rectangle1 = RectangleClass(10, 2, 0, 0, 12)
        rectangle2 = RectangleClass(10, 3, 3, 2, 12)

        self.assertEqual(rectangle1.area(), 20)
        self.assertEqual(rectangle2.area(), 30)
        with self.assertRaises(ValueError):
            rectangle3 = RectangleClass(10, -2, 0, 0, 12)
            rectangle3.area()
        with self.assertRaises(ValueError):
            rectangle4 = RectangleClass(-10, 3, 3, 2, 12)
            rectangle4.area()


if __name__ == '__main__':
    unittest.main()

