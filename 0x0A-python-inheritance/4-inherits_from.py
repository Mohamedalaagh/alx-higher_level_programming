#!/usr/bin/python3
"""
Defines a utility function for checking if an object is an inherited instance of a class.
"""

def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is an inherited instance of a_class, otherwise False.

    Example:
        ```
        # Example usage
        class ParentClass:
            pass

        class ChildClass(ParentClass):
            pass

        obj = ChildClass()
        result = inherits_from(obj, ParentClass)
        # Output: True
        ```
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

