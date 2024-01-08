#!/usr/bin/python3
"""
Defines a specialized list class, MyList, which inherits from the built-in list class.
This class adds the capability to print its elements in sorted ascending order.
"""

class MyList(list):
    """
    Implements sorted printing for the built-in list class.

    Attributes:
    - Inherits all attributes from the built-in list class.

    Methods:
    - print_sorted(): Print the elements of the list in sorted ascending order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted ascending order.

        Example:
        ```
        my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        my_list.print_sorted()
        # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        ```
        """
        print(sorted(self))

