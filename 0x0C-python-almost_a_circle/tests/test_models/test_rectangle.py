#!/usr/bin/python3
""" Unittest module for rectangle module """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ TestCases for Rectangle """
    def test_id(self):
        """ test rectangle """
        r1 = Rectangle(1, 2, 4, 3, 5)
        self.assertAlmostEqual(r1.id, 5)
        r2 = Rectangle(1, 2)
        self.assertAlmostEqual(r2.id, 1)
        r3 = Rectangle(10, 2)
        self.assertAlmostEqual(r3.id, 2)

    def test_type_validation(self):
        """ test for exception raised for wrong types """
        with self.assertRaises(TypeError):
            Rectangle("2", 10)
        with self.assertRaises(TypeError):
            Rectangle(None, 1)
        with self.assertRaises(TypeError):
            Rectangle((1, 2), 1)
        with self.assertRaises(TypeError):
            Rectangle({1: 2}, 2)
        with self.assertRaises(TypeError):
            Rectangle(4.5, 1)
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 1)

        with self.assertRaises(TypeError):
            Rectangle(2, "10")
        with self.assertRaises(TypeError):
            Rectangle(1, None)
        with self.assertRaises(TypeError):
            Rectangle(1, (1, 2))
        with self.assertRaises(TypeError):
            Rectangle(1, {1: 2})
        with self.assertRaises(TypeError):
            Rectangle(1, 4.5)
        with self.assertRaises(TypeError):
            Rectangle(1, float('inf'))
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.width = "str"
        with self.assertRaises(TypeError):
            r.height = "str"
        r = Rectangle(1, 2, 0, 0, 4)
        with self.assertRaises(TypeError):
            r.x = "4"
        with self.assertRaises(TypeError):
            r.y = "3"

    def test_value_validation(self):
        """ tests the values passed to the attributes of rectangle """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 3)
        with self.assertRaises(ValueError):
            Rectangle(1, -3)
        with self.assertRaises(ValueError):
            Rectangle(2, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 3, 3, -7)
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -3
        with self.assertRaises(ValueError):
            r.height = -4
        r = Rectangle(1, 20, 4, 3)
        with self.assertRaises(ValueError):
            r.x = -2
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        """ tests the area value for Rectangle"""
        r1 = Rectangle(3, 2)
        self.assertAlmostEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertAlmostEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertAlmostEqual(r3.area(), 56)

    """ def test_str(self):
        tests the __str__ output of Rectangle method
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEquals(r1.__str__, "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEquals(r2.__str__, "[Rectangle] (1) 1/0 - 5/5") """
