#!/usr/bin/python3
"""
Unit test for the Square class
"""

import unittest
from models.square import Square
from models.base import Base

class TestSquareStrMethod(unittest.TestCase):
    """Tests for the __str__ method of the Square class"""

    # Resetting the counter for the number of objects
    Base._Base__nb_objects = 0

    def test_str_with_full_information(self):
        """Test __str__ method with all information provided"""
        square = Square(2, 1, 3, 6)
        self.assertEqual("[Square] (6) 1/3 - 2", str(square))

    def test_str_with_default_values(self):
        """Test __str__ method with default values"""
        square_default = Square(2, 1)
        self.assertEqual("[Square] (1) 1/0 - 2", str(square_default))

    def test_str_with_partial_information(self):
        """Test __str__ method with partial information provided"""
        square_partial = Square(3, 1, 6)
        self.assertEqual("[Square] (2) 1/6 - 3", str(square_partial))

    def test_str_with_minimum_information(self):
        """Test __str__ method with minimum information provided"""
        square_minimal = Square(3)
        self.assertEqual("[Square] (3) 0/0 - 3", str(square_minimal))

    def test_str_with_invalid_parameters(self):
        """Test __str__ method with invalid parameters"""
        with self.assertRaises(ValueError):
            Square(-2)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(TypeError):
            Square(3.2)
        with self.assertRaises(TypeError):
            Square({1, 2})
        with self.assertRaises(TypeError):
            Square([1, 34])
        with self.assertRaises(TypeError):
            Square(float('inf'))

if __name__ == '__main__':
    unittest.main()

