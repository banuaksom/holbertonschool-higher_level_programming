#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_pos_int(self):
        self.assertEqual(max_integer([4, 6, 2]), 6)

    def test_neg_int(self):
        self.assertEqual(max_integer([-2, -4, -6]), -2)

    def test_one(self):
        self.assertEqual(max_integer([4]), 4)

    def test_string(self):
        self.assertEqual(max_integer(['d', 'b', 'z']), 'z')

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_float_int(self):
        self.assertEqual(max_integer([1.1, 4, 2.5, 9, 8.9]), 9)

    def test_mix_data(self):
        with self.assertRaises(TypeError):
            max_integer(['B', 2, 3])

if __name__ == '__main__':
    unittest.main()
