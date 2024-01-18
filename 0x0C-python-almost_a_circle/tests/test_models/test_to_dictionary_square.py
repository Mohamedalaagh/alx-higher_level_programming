#!/usr/bin/python3
"""
Unittest for to_dictionary method in the Square class
"""

import unittest
from models import square
Square = square.Square


class TestSquareToDictionary(unittest.TestCase):
    """
    Tests for to_dictionary method in the Square class
    """

    def test_to_dict_with_valid_input(self):
        """
        Test to_dictionary with a normal square
        """
        square_1 = Square(10, 2, 1)
        self.assertEqual(square_1.to_dictionary(), {
                         'id': 1, 'x': 2, 'size': 10, 'y': 1})
        
        square_2 = Square(10, 2, 1, 8)
        self.assertEqual(square_2.to_dictionary(), {
                         'id': 8, 'x': 2, 'size': 10, 'y': 1})
        
        square_3 = Square(3, 12)
        self.assertEqual(square_3.to_dictionary(), {
                         'id': 2, 'x': 12, 'size': 3, 'y': 0})
        
        square_4 = Square(3)
        self.assertEqual(square_4.to_dictionary(), {
                         'id': 3, 'size': 3, 'x': 0, 'y': 0})

    def test_to_dict_with_value_error(self):
        """
        Test to_dictionary with value errors
        """
        with self.assertRaises(ValueError):
            invalid_square_1 = Square(-2, 3, 12)
            invalid_square_1.to_dictionary()
        
        with self.assertRaises(ValueError):
            invalid_square_2 = Square(2, -3, 12)
            invalid_square_2.to_dictionary()
        
        with self.assertRaises(ValueError):
            invalid_square_3 = Square(2, 3, -12)
            invalid_square_3.to_dictionary()

    def test_to_dict_with_type_error(self):
        """
        Test to_dictionary with type errors
        """
        with self.assertRaises(TypeError):
            invalid_square_4 = Square()
            invalid_square_4.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_5 = Square(2.3, 3, 12)
            invalid_square_5.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_6 = Square(2, 3.2, 12)
            invalid_square_6.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_7 = Square(2, (3, 2, 3), 12)
            invalid_square_7.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_8 = Square((2, 8, 9), 3, 12)
            invalid_square_8.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_9 = Square(2, 3, (2, 8, 7))
            invalid_square_9.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_10 = Square((), 3, 12)
            invalid_square_10.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_11 = Square(2, (), 12)
            invalid_square_11.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_12 = Square(2, 3, ())
            invalid_square_12.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_13 = Square(float('inf'), 3, 12)
            invalid_square_13.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_14 = Square(2, float('inf'), 12)
            invalid_square_14.to_dictionary()
        
        with self.assertRaises(TypeError):
            invalid_square_15 = Square(2, 12, float('inf'))
            invalid_square_15.to_dictionary()


if __name__ == '__main__':
    unittest.main()

