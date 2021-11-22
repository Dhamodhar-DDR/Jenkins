#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from prog import check_perfect_square

class TestSquare(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = 15
        result = check_perfect_square(data)
        self.assertEqual(result, [1,4,9])

if __name__ == '__main__':
    unittest.main()