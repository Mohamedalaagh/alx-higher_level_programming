#!/usr/bin/python3
"""Define a Rectangle class"""
from  models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a new rectangle.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x, y: Variables

        Return: always nothing.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """getter for width"""
            return self.__width

        @width.setter
        """setter for width"""
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be positive value")
            self.__width = value

        @property
        def height(self):
            """getter for height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for width"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be positive value")
            self.__height = value

        @property
        def x(self):
            """gettetr for x"""
            return self.__x

        @x.setter
        def x(self, value):
            """setter for x"""
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be non-negative value")
            self.__x = value

        @property
        def y(self):
            """getter for y"""
            return self.__y

        @y.setter
        def y(self, value):
            """setter for y"""
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be positive value")
            self.__y = value
