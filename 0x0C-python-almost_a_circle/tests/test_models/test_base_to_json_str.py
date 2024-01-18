#!/usr/bin/python3
"""Unittests for to_json_string(list_dictionaries)"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestToJsonString(unittest.TestCase):
    """Unittest for to_json_string"""
    def test_rectangle_to_json_str(self):
        """True if to_json_string returns str type"""
        rectangle_instance = Rectangle(10, 7, 4, 6, 1)
        rectangle_dict = rectangle_instance.to_dictionary()
        json_str = Base.to_json_string([rectangle_dict])
        self.assertEqual(str, type(json_str))

    def test_rectangle_instance_length(self):
        """Test rectangle instance with len()"""
        rectangle_instance = Rectangle(10, 7, 6, 4, 1)
        rectangle_dict = rectangle_instance.to_dictionary()
        json_str = Base.to_json_string([rectangle_dict])
        self.assertTrue(len(json_str) == 53)

    def test_more_rectangles_to_json_str(self):
        """True if to_json_string returns str type"""
        rect1 = Rectangle(10, 7, 4, 6, 1)
        rect2 = Rectangle(7, 10, 6, 4, 1)
        rectangles_list = [rect1.to_dictionary(), rect2.to_dictionary()]
        json_str = Base.to_json_string(rectangles_list)
        self.assertEqual(str, type(json_str))

    def test_more_rectangle_instances_length(self):
        """Test rectangle instances with len()"""
        rect1 = Rectangle(10, 7, 4, 6, 1)
        rect2 = Rectangle(7, 10, 6, 4, 1)
        rectangles_list = [rect1.to_dictionary(), rect2.to_dictionary()]
        json_str = Base.to_json_string(rectangles_list)
        self.assertTrue(len(json_str) == 106)

    def test_square_to_json_str(self):
        """True if to_json_string returns str type"""
        square_instance = Square(10, 4, 6, 1)
        square_dict = square_instance.to_dictionary()
        json_str = Base.to_json_string([square_dict])
        self.assertEqual(str, type(json_str))

    def test_square_instance_length(self):
        """Test square instance with len()"""
        square_instance = Square(10, 4, 6, 1)
        square_dict = square_instance.to_dictionary()
        json_str = Base.to_json_string([square_dict])
        self.assertTrue(len(json_str) == 37)

    def test_more_squares_to_json_str(self):
        """True if to_json_string returns str type"""
        square1 = Square(10, 4, 6, 1)
        square2 = Square(7, 6, 4, 1)
        squares_list = [square1.to_dictionary(), square2.to_dictionary()]
        json_str = Base.to_json_string(squares_list)
        self.assertEqual(str, type(json_str))

    def test_more_square_instances_length(self):
        """Test square instances with len()"""
        square1 = Square(10, 4, 6, 1)
        square2 = Square(7, 6, 4, 1)
        squares_list = [square1.to_dictionary(), square2.to_dictionary()]
        json_str = Base.to_json_string(squares_list)
        self.assertTrue(len(json_str) == 77)

    def test_empty_list(self):
        """Test with empty value"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none_value(self):
        """Test with None"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_parameters(self):
        """Test if no parameter (list_dictionaries)"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_parameters(self):
        """Test if more undefined parameters"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 3600)


if __name__ == "__main__":
    unittest.main()

