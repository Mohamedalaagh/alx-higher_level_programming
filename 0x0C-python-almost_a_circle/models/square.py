#!/usr/bin/python3
"""Define square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize new reectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string represintation for user"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
