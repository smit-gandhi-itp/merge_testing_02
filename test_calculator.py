"""Unit tests for the Calculator module.

This module contains comprehensive unit tests for all calculator operations
including edge cases and error handling.
"""

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

    def test_add_floats(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(self.calc.add(5.5, 3.2), 8.7, places=1)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=1)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)

    def test_subtract_floats(self):
        """Test subtraction with floating point numbers."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 3.2), 2.3, places=1)
        self.assertAlmostEqual(self.calc.subtract(10.7, 5.2), 5.5, places=1)

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
        self.assertAlmostEqual(self.calc.multiply(5.5, 2), 11.0, places=1)
        self.assertAlmostEqual(self.calc.multiply(3.3, 3), 9.9, places=1)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_divide_floats(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(self.calc.divide(5.5, 2), 2.75, places=2)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333, places=3)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_power_positive_numbers(self):
        """Test power operation with positive numbers."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)

    def test_power_negative_exponent(self):
        """Test power operation with negative exponent."""
        self.assertEqual(self.calc.power(2, -1), 0.5)
        self.assertEqual(self.calc.power(10, -2), 0.01)

    def test_power_fractional_exponent(self):
        """Test power operation with fractional exponent."""
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2.0, places=1)
        self.assertAlmostEqual(self.calc.power(27, 1/3), 3.0, places=1)

    def test_modulo_positive_numbers(self):
        """Test modulo operation with positive numbers."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(20, 7), 6)
        self.assertEqual(self.calc.modulo(15, 5), 0)

    def test_modulo_negative_numbers(self):
        """Test modulo operation with negative numbers."""
        self.assertEqual(self.calc.modulo(-10, 3), 2)
        self.assertEqual(self.calc.modulo(10, -3), -2)

    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulo(10, 0)
        self.assertEqual(str(context.exception), "Cannot perform modulo with zero")

    def test_modulo_floats(self):
        """Test modulo operation with floating point numbers."""
        self.assertAlmostEqual(self.calc.modulo(10.5, 3), 1.5, places=1)
        self.assertAlmostEqual(self.calc.modulo(7.5, 2.5), 0.0, places=1)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_large_numbers(self):
        """Test operations with very large numbers."""
        large_num = 10**10
        self.assertEqual(self.calc.add(large_num, large_num), 2 * large_num)
        self.assertEqual(self.calc.multiply(large_num, 2), 2 * large_num)

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        small_num = 10**-10
        result = self.calc.add(small_num, small_num)
        self.assertAlmostEqual(result, 2 * small_num, places=15)

    def test_mixed_types(self):
        """Test operations with mixed int and float types."""
        self.assertEqual(self.calc.add(5, 3.5), 8.5)
        self.assertEqual(self.calc.multiply(2, 3.5), 7.0)


def run_tests():
    """Run all tests and display results."""
    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorEdgeCases))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on test results
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    exit(run_tests())
