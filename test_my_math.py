# test_my_math.py
import unittest
from my_math import add

class TestMyMath(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add(-10, -7)
        self.assertEqual(result, -17)

    def test_add_mixed_numbers(self):
        result = add(0, 12)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()