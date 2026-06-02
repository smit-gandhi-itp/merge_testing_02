"""Unit tests for the calculator module."""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(10, -5), 5)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_add_floats(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.3), 3.8)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
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
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(-10, 5), -50)
        self.assertEqual(self.calc.multiply(10, -5), -50)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiply_floats(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.5), 3.75)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_divide_floats(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=5)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        self.assertEqual(self.calc.power(2, -1), 0.5)
        self.assertEqual(self.calc.power(10, -2), 0.01)

    def test_power_zero_base(self):
        """Test power with zero base."""
        self.assertEqual(self.calc.power(0, 5), 0)
        self.assertEqual(self.calc.power(0, 0), 1)

    def test_power_floats(self):
        """Test power with floating point numbers."""
        self.assertAlmostEqual(self.calc.power(2.5, 2), 6.25)
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2.0)

    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 4), 3)
        self.assertEqual(self.calc.modulo(20, 5), 0)

    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers."""
        self.assertEqual(self.calc.modulo(-10, 3), 2)
        self.assertEqual(self.calc.modulo(10, -3), -2)

    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulo(10, 0)
        self.assertEqual(str(context.exception), "Cannot perform modulo with zero divisor")


if __name__ == "__main__":
    unittest.main()
