#!/usr/bin/python3
"""
    Unittest for the init function of the Base class
"""

import unittest
from models.base import Base


class Test_Base_Init(unittest.TestCase):
    """class test of the init base function"""

    def test_id_int(self):
        """Test integer id"""
        m = Base(5)
        self.assertEqual(m.id, 5)
        m = Base(0)
        self.assertEqual(m.id, 0)
        m = Base(-3)
        self.assertEqual(m.id, -3)

    def test_id_incrementation(self):
        """Test id incrementation"""
        Base._Base__nb_objects = 0
        m = Base()
        self.assertEqual(m.id, 1)
        m = Base(7)
        self.assertEqual(m.id, 7)
        m = Base(None)
        self.assertEqual(m.id, 2)
        m = Base()
        self.assertEqual(m.id, 3)

    def test_id_non_int(self):
        """Test non integer id"""
        m = Base("Holberton")
        self.assertEqual(m.id, "Holberton")
        m = Base('A')
        self.assertEqual(m.id, 'A')
        m = Base([1, 2, 3])
        self.assertEqual(m.id, [1, 2, 3])
        m = Base((1, 2))
        self.assertEqual(m.id, (1, 2))
        m = Base({"id": 7, "name": "Betty"})
        self.assertEqual(m.id, {"id": 7, "name": "Betty"})
        m = Base(False)
        self.assertEqual(m.id, False)

    def test_id_error(self):
        """Test error"""
        with self.assertRaises(TypeError):
            m = Base(1, 2)
        with self.assertRaises(TypeError):
            m = Base(1, None)


if __name__ == '__main__':
    unittest.main()

