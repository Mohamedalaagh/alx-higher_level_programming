"""
UNIT TEST FOR THE LOAD_FROM_FILE METHOD OF THE BASE CLASS
"""
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquareSize(unittest.TestCase):
    """ Tests for load_from_file of base.py """

    def test_load_empty_file(self):
        """Tests for nonexistent and empty file"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])
        os.mknod("Rectangle.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_load_rectangle(self):
        """Test for loading a list of rectangles"""
        RectA = Rectangle(2, 4)
        RectB = Rectangle(1, 1)
        RectC = Rectangle(6, 6)
        my_list = [RectA, RectB, RectC]
        Rectangle.save_to_file([RectA, RectB, RectC])
        my_list_loaded = Rectangle.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Rectangle.json")

    def test_load_square(self):
        """Test for loading a list of squares"""
        SquareA = Square(2)
        SquareB = Square(1)
        SquareC = Square(6)
        my_list = [SquareA, SquareB, SquareC]
        Square.save_to_file([SquareA, SquareB, SquareC])
        my_list_loaded = Square.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Square.json")

    def test_extra_args(self):
        """Test calling the function with an additional argument"""
        with self.assertRaises(TypeError):
            Base.load_from_file("Hello")

