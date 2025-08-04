import unittest
from app.utils.operations import power, fibonacci, factorial


class TestMathOperations(unittest.TestCase):

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(9, 0.5), 3)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(7), 13)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)
        with self.assertRaises(ValueError):
            factorial(-3)


if __name__ == '__main__':
    unittest.main()
