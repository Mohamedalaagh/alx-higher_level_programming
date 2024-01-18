#!/usr/bin/python3
"""
    Unittest for Base
"""

import unittest
from models import base
Base = base.Base

class TestBase(unittest.TestCase):
    """
        test for Base
    """
    def test_creation_id(self):
        """
            test if value of id has the good assignment
        """
        i1 = Base()
        i2 = Base()
        i3 = Base()
        i4 = Base(12)
        i5 = Base(-5)
        i6 = Base(6.3)
        i7 = Base()
        i8 = Base(None)

        self.assertEqual(i1.id, 1)
        self.assertEqual(i2.id, 2)
        self.assertEqual(i3.id, 3)
        self.assertEqual(i4.id, 12)
        self.assertEqual(i5.id, -5)
        self.assertEqual(i6.id, 6.3)
        self.assertEqual(i7.id, 4)
        self.assertEqual(i8.id, 5)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])

if __name__ == '__main__':
    unittest.main()

