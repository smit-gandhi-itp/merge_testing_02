"""Unit tests for the Calculator module

Tests all arithmetic operations including edge cases and error handling.
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(20, 5), 15)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(10, -5), 15)

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(10, 4), 40)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_divide_with_float_result(self):
        """Test division that results in a float."""
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(100, 0), 1)

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        self.assertEqual(self.calc.power(2, -1), 0.5)
        self.assertEqual(self.calc.power(10, -2), 0.01)

    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 4), 3)

    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers."""
        self.assertEqual(self.calc.modulo(-10, 3), 2)
        self.assertEqual(self.calc.modulo(10, -3), -2)

    def test_modulo_by_zero(self):
        """Test that modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulo(10, 0)
        self.assertEqual(str(context.exception), "Cannot perform modulo with zero")

    def test_modulo_exact_division(self):
        """Test modulo when numbers divide evenly."""
        self.assertEqual(self.calc.modulo(10, 5), 0)
        self.assertEqual(self.calc.modulo(20, 10), 0)


if __name__ == '__main__':
    unittest.main()
