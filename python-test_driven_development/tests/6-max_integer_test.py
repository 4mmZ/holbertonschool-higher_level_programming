#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([9, 1, 3, 2]), 9)
        self.assertEqual(max_integer([1, -19, 3, 2]), 3)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-1, -5, -7, -2, -3]), -1)


if __name__ == '__main__':
    unittest.main()