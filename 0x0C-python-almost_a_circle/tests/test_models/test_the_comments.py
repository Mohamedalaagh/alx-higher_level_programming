#!/usr/bin/python3
"""
    Unittests for Base, Rectangle, and Square classes
"""

import unittest
import pycodestyle
from models import base
from models import rectangle
from models import square

BaseClass = base.Base
RectangleClass = rectangle.Rectangle
SquareClass = square.Square


class TestClassesConformance(unittest.TestCase):
    """
        Test conformance to PEP-8 for Base, Rectangle, and Square classes
    """

    def test_conformance_base(self):
        """
            Test that we conform to PEP-8 for Base class
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_conformance_rectangle(self):
        """
            Test that we conform to PEP-8 for Rectangle class
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_conformance_square(self):
        """
            Test that we conform to PEP-8 for Square class
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()

