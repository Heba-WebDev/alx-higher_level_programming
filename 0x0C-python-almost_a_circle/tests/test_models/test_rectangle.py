#!/usr/bin/python3
"""Defines unittests for rectangle.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Tests for class Rectangle"""

    def test_instance_cls(self):
        """Checks for a instance of the class
        """
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(id(Rectangle) != id(Base))
        self.assertTrue(type(Rectangle) == type(Base))
        r2 = Rectangle(2, 5)
        self.assertTrue(type(r1) == type(r2))
        self.assertFalse(id(r1) == id(r2))

    def test_init_attributes(self):
        """Checks when id is none
        """
        r1 = Rectangle(10, 60)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 60)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 4)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 4, 5, 50)
        self.assertEqual(r3.id, 50)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 5)

    def test_raise_errors(self):
        """Check for raises errors
        """

        # Checks for diferents instances
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(AttributeError):
            r1 = Rectangle(10, 80)
            r1.to_json()
        with self.assertRaises(TypeError):
            r2 = Rectangle(10)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -4)
        with self.assertRaises(TypeError):
            r4 = Rectangle("10", 4)
        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 4, -5, 7)
        with self.assertRaises(TypeError):
            r6 = Rectangle(10, 4, 5, 10, 30, 60)
        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 10)

        # Checks for setters
        with self.assertRaises(TypeError):
            r1.x = "4"
        with self.assertRaises(ValueError):
            r1.x = -4
        with self.assertRaises(ValueError):
            r1.width = -10
        with self.assertRaises(TypeError):
            r1.width = "10"
        with self.assertRaises(TypeError):
            r1.height = "30"
        with self.assertRaises(ValueError):
            r1.height = -10
        with self.assertRaises(TypeError):
            r1.y = "10"
        with self.assertRaises(ValueError):
            r1.y = -10

        # Checks for update method
        with self.assertRaises(ValueError):
            r1.update(10, -10, 20, 40)
        with self.assertRaises(TypeError):
            r1.update(10, 10, "20", 40)
        with self.assertRaises(ValueError):
            r1.update(id=10, x=10, y=20, width=40, height=-60)
        with self.assertRaises(TypeError):
            r1.update(id=10, x=10, y=20, width="30", height=40)
        with self.assertRaises(AttributeError):
            r2 = None
            r2.to_dictionary

        def test_area(self):
            """Check area method of rectangle objects
            """
            r1 = Rectangle(3, 2)
            area = r1.area()
            self.assertEqual(area, 6)

            r2 = Rectangle(3, 2)
            area = Rectangle.area(r2)
            self.assertEqual(area, 6)

            r3 = Rectangle(30, 20, 4, 5, 10)
            area = r3.area()
            self.assertEqual(area, 600)

            r4 = Rectangle(5, 5, 4)
            area = r4.area()
            self.assertEqual(area, 25)

    if __name__ == '__main__':
        unittest.main()
