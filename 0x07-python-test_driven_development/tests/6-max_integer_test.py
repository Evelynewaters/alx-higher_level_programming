#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class"""
    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_negative_and_positive_integers(self):
        self.assertEqual(max_integer([-21, 20, -414, 16]), 20)

    def test_None(self):
        self.assertEqual(max_integer([None]), None)

    def test_one_integers(self):
        self.assertEqual(max_integer([1]), 1)

    def test_one_integers(self):
        self.assertEqual(max_integer([]), None)
