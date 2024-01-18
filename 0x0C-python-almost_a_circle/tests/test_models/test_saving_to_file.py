#!/usr/bin/python3
"""
Unit tests for the save_to_file method of the Base class
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    def test_save_one_rectangle(self):
        """Test save_to_file with one rectangle"""
        rectangle = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_two_rectangles(self):
        """Test save_to_file with two rectangles"""
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_one_square(self):
        """Test save_to_file with one square"""
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_two_squares(self):
        """Test save_to_file with two squares"""
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_save_overwrite(self):
        """Test save_to_file with overwrite"""
        square = Square(8, 5, 9, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_empty_list(self):
        """Test save_to_file with an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_no_args(self):
        """Test save_to_file with no argument"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_two_arg(self):
        """Test save_to_file with two arguments"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

if __name__ == "__main__":
    unittest.main()

