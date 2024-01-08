#!/usr/bin/python3
"""
Defines a base class for geometry, called BaseGeometry.
"""

class BaseGeometry:
    """
    Represents the base geometry class.

    This class can be used as a foundation for more specific geometry classes.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

