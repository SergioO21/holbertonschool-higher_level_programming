#!/usr/bin/python3
"""
===============================================================================

████████╗███████╗███████╗████████╗     ██████╗ █████╗ ███████╗███████╗███████╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
   ██║   █████╗  ███████╗   ██║       ██║     ███████║███████╗█████╗  ███████╗
   ██║   ██╔══╝  ╚════██║   ██║       ██║     ██╔══██║╚════██║██╔══╝  ╚════██║
   ██║   ███████╗███████║   ██║       ╚██████╗██║  ██║███████║███████╗███████║
   ╚═╝   ╚══════╝╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
===============================================================================
"""

from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """
    # Test cases of:
        - ``Base`` Class
        - ``Square`` Class
        - ``Rectangle`` Class
    """

    def test_id(self):

        b1 = Rectangle(20, 30)
        self.assertEqual(b1.id, 1)

        s1 = Square(10)
        self.assertEqual(s1.id, 2)

        b2 = Rectangle(7, 7, 7, 7, 7)
        self.assertEqual(b2.id, 7)

        s2 = Square(21, 21, 21, 21)
        self.assertEqual(s2.id, 21)

        b3 = Rectangle(50, 70, 96, 74)
        self.assertEqual(b3.id, 3)

        s3 = Square(6, 9, 3)
        self.assertEqual(s3.id, 4)

    def test_value_and_typerrors(self):

        with self.assertRaises(TypeError):
            Rectangle("hello", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "Bye")

        with self.assertRaises(TypeError):
            Square("hello")

        with self.assertRaises(TypeError):
            Rectangle(10, 2, (1, 2))
        with self.assertRaises(TypeError):
            Square(10, (1, 2))

        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, [1, 2, 3])
        with self.assertRaises(TypeError):
            Square(10, 1, [1, 2, 3])

        with self.assertRaises(ValueError):
            Rectangle(-5, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, -5)

        with self.assertRaises(TypeError):
            Rectangle(-10)
