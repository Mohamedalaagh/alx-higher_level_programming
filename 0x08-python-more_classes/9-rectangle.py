#!/usr/bin/python3
"""Module 9-rectangle

This module contains the definition of the Rectangle class.
"""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances (int): A counter for the number instances.
        print_symbol (str): The symbol used for printing the rectangle .
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle .
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal string representation of the rectangle.

        Returns:
            str: A string representing the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Returns an internal string representation of a Rectangle instance.

        Returns:
            str: A formal string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The larger rectangle, or rect_1 if areas are equal.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Returns:
            Rectangle: A new Rectangle instance representing a square.

        """
        return cls(size, size)
