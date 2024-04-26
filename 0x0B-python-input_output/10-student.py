#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student properties."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        """
        Return dictionary representation of Student instance.

        If 'attributes' is provided and is a list of strings, only attributes
        with matching names will be included.
        """
        if isinstance(attributes, list) and all(isinstance(attr, str) for attr in attributes):
            return {attr: getattr(self, attr) for attr in attributes if hasattr(self, attr)}
        return self.__dict__
