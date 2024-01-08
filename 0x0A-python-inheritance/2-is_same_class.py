#!/usr/bin/python3
"""
Defines a utility function for class type checking.
"""

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.

    Example:
        ```
        # Example usage
        instance_of_list = [1, 2, 3]
        result = is_same_class(instance_of_list, list)
        # Output: True
        ```
    """
    return type(obj) == a_class

