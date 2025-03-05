
import unittest
from function_factorial import function_factorial 


class TestFunctionFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(function_factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(function_factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(RecursionError):
            function_factorial(-1)

    def test_factorial_non_integer(self):
        with self.assertRaises(TypeError):
            function_factorial(3.5)

    def test_factorial_large_number(self):
        self.assertEqual(function_factorial(10), 3628800)

if __name__ == '__main__':
    unittest.main()