#!/usr/bin/python3
"""
    Unittest for the create function of the Base class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Base_Create(unittest.TestCase):
    """class test of the create base function"""

    def test_rectangle_create(self):
        """test rectangle creation"""
        n1 = Rectangle(3, 5, 1)
        n1_dictionary = n1.to_dictionary()
        n2 = Rectangle.create(**n1_dictionary)
        self.assertEqual(str(n1), str(n2))
        self.assertIsNot(n1, n2)
        self.assertNotEqual(n1, n2)

    def test_square_create(self):
        """test square creation"""
        n1 = Square(3, 5, 1)
        n1_dictionary = n1.to_dictionary()
        n2 = Square.create(**n1_dictionary)
        self.assertEqual(str(n1), str(n2))
        self.assertIsNot(n1, n2)
        self.assertNotEqual(n1, n2)

if __name__ == '__main__':
    unittest.main()

