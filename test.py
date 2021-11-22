#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from prog import check_perfect_square

class TestSquare(unittest.TestCase):
    def test_list_int_0(self):
        data = 15
        result = check_perfect_square(data)
        self.assertEqual(result, [1,4,9])
    def test_list_int_1(self):
        data = 25
        result = check_perfect_square(data)
        self.assertEqual(result, [1,4,9,16,25])
    def test_list_int_2(self):
        data = -10
        result = check_perfect_square(data)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
