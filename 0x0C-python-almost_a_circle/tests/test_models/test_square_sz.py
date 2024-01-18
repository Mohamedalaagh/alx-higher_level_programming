"""
Unit test for the size setter/getter methods of the Square class
"""

import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquareSizeSetterGetter(unittest.TestCase):
    """Tests for size setter/getter of the Square class"""

    def test_square_size_no_args(self):
        """Test size setter without arguments"""
        with self.assertRaises(TypeError):
            Square.size()

    def test_square_size_getter(self):
        """Test size getter"""
        my_square = Square(2)
        self.assertEqual(my_square.size, 2)

    def test_square_size_setter(self):
        """Test size setter"""
        my_square = Square(2)
        my_square.size = 7
        self.assertEqual(my_square.size, 7)

    def test_square_size_setter_zero(self):
        """Test size setter with 0"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = 0

    def test_square_size_setter_negative(self):
        """Test size setter with negative value"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = -5

    def test_square_size_setter_float(self):
        """Test size setter with wrong type: float"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = 4.5

    def test_square_size_setter_string(self):
        """Test size setter with wrong type: string"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = "School"

    def test_square_size_setter_list(self):
        """Test size setter with wrong type: list"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = [4]

    def test_square_size_setter_tuple(self):
        """Test size setter with wrong type: tuple"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = (4, )

    def test_square_size_setter_dict(self):
        """Test size setter with wrong type: dictionary"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = {4}

