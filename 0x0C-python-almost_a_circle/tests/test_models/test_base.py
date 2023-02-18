#!/usr/bin/python3
""" Unittest module for Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Base model test cases """
    def test_id(self):
        """ tests the initialisation of the id of each instance """
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
        b3 = Base(12)
        self.assertAlmostEqual(b3.id, 12)
        b4 = Base()
        self.assertAlmostEqual(b4.id, 3)
        b5 = Base(8)
        self.assertAlmostEqual(b5.id, 8)
