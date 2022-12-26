#!/usr/bin/python3

"""This is a unittest for finding the maximum integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_arranged_list(self):
        arranged = [5, 7, 9, 12]
        self.assertEqual(max_integer(arranged), 12)

    def test_unarranged_list(self):
        unarranged = [5, 12, 7, 9]
        self.assertEqual(max_integer(unarranged), 12)

    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_max_integer_at_beginning(self):
        max_integer_at_beginning = [12, 7, 9, 5]
        self.assertEqual(max_integer(max_integer_at_beginning), 12)

    def test_one_element_list(self):
        one_element = [4]
        self.assertEqual(max_integer(one_element), 4)

    def test_floats(self):
        floats_list = [20.7, 10.1, -2.42, 1.2, 6.8]
        self.assertEqual(max_integer(floats_list), 20.7)

    def test_ints_and_floats(self):
        ints_and_floats_list = [9.43, 11.5, -3, 12, 3]
        self.assertEqual(max_integer(ints_and_floats_list), 11.5)

    def test_string(self):
        string = "zimbabwe"
        self.assertEqual(max_integer(string), 'z')

    def test_list_of_strings(self):
        strings = ["Peter", "is", "your", "name"]
        self.assertEqual(max_integer(strings), "your")

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()


