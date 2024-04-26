#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Defines a student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize student properties in the constructor."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts student object to a dictionary."""
        return self.__dict__
