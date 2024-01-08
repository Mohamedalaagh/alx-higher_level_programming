#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int.

This class inverts the behavior of the == and != operators.
"""

class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """
        Override == operator with != behavior.

        Args:
            value: The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override != operator with == behavior.

        Args:
            value: The value to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return self.real == value

