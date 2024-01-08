#!/usr/bin/python3
"""
Defines a Rectangle subclass, Square.
"""

# Import the Rectangle class from an external module
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square, inheriting from the Rectangle class.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        # Validate and set the size using integer_validator from the base class
        self.integer_validator("size", size)
        
        # Initialize the square using the Rectangle class with equal width and height
        super().__init__(size, size)
        
        # Set the size attribute specific to the Square class
        self.__size = size

