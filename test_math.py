"""Comprehensive test suite for the math module."""

import unittest
import math as builtin_math
from math import (
    add, subtract, multiply, divide, modulo,
    power, square, cube, square_root, nth_root,
    factorial, fibonacci, gcd, lcm,
    sin, cos, tan,
    mean, median, mode, variance, standard_deviation,
    is_prime, is_even, is_odd, absolute, ceiling, floor, round_number,
    log, log10, natural_log,
    distance_2d, distance_3d,
    circle_area, circle_circumference, rectangle_area, triangle_area,
    MathError
)


class TestBasicArithmetic(unittest.TestCase):
    """Test basic arithmetic operations."""

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(2.5, 3.7), 6.2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -2), -1)
        self.assertAlmostEqual(subtract(5.5, 2.3), 3.2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 5), -2)
        with self.assertRaises(MathError):
            divide(5, 0)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 5), 0)
        self.assertEqual(modulo(7, 4), 3)
        with self.assertRaises(MathError):
            modulo(5, 0)


class TestPowerAndRoot(unittest.TestCase):
    """Test power and root operations."""

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, 2), 100)
        self.assertAlmostEqual(power(2, 0.5), builtin_math.sqrt(2))

    def test_square(self):
        self.assertEqual(square(5), 25)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(0), 0)
        self.assertAlmostEqual(square(2.5), 6.25)

    def test_cube(self):
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(-2), -8)
        self.assertEqual(cube(0), 0)
        self.assertAlmostEqual(cube(2.5), 15.625)

    def test_square_root(self):
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), builtin_math.sqrt(2))
        with self.assertRaises(MathError):
            square_root(-1)

    def test_nth_root(self):
        self.assertAlmostEqual(nth_root(27, 3), 3)
        self.assertAlmostEqual(nth_root(16, 4), 2)
        self.assertAlmostEqual(nth_root(-8, 3), -2)
        with self.assertRaises(MathError):
            nth_root(5, 0)
        with self.assertRaises(MathError):
            nth_root(-4, 2)


class TestFactorialAndCombinatorics(unittest.TestCase):
    """Test factorial and combinatorics functions."""

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        with self.assertRaises(MathError):
            factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        with self.assertRaises(MathError):
            fibonacci(-1)

    def test_gcd(self):
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(17, 5), 1)
        self.assertEqual(gcd(100, 50), 50)
        self.assertEqual(gcd(-12, 8), 4)

    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(3, 7), 21)
        self.assertEqual(lcm(12, 18), 36)
        with self.assertRaises(MathError):
            lcm(0, 5)


class TestTrigonometric(unittest.TestCase):
    """Test trigonometric functions."""

    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(builtin_math.pi / 2), 1)
        self.assertAlmostEqual(sin(90, degrees=True), 1)
        self.assertAlmostEqual(sin(30, degrees=True), 0.5)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(builtin_math.pi), -1)
        self.assertAlmostEqual(cos(0, degrees=True), 1)
        self.assertAlmostEqual(cos(60, degrees=True), 0.5)

    def test_tan(self):
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(builtin_math.pi / 4), 1)
        self.assertAlmostEqual(tan(45, degrees=True), 1)


class TestStatistical(unittest.TestCase):
    """Test statistical functions."""

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(mean([10, 20, 30]), 20)
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5]), 2.5)
        with self.assertRaises(MathError):
            mean([])

    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([5, 1, 3, 2, 4]), 3)
        with self.assertRaises(MathError):
            median([])

    def test_mode(self):
        self.assertEqual(mode([1, 2, 2, 3, 4]), 2)
        self.assertEqual(mode([5, 5, 5, 1, 2]), 5)
        self.assertEqual(mode([1, 1, 2, 2, 3]), 1)  # Returns first max
        with self.assertRaises(MathError):
            mode([])

    def test_variance(self):
        self.assertAlmostEqual(variance([1, 2, 3, 4, 5]), 2.0)
        self.assertAlmostEqual(variance([10, 10, 10]), 0.0)
        with self.assertRaises(MathError):
            variance([])

    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([1, 2, 3, 4, 5]), builtin_math.sqrt(2.0))
        self.assertAlmostEqual(standard_deviation([10, 10, 10]), 0.0)
        with self.assertRaises(MathError):
            standard_deviation([])


class TestNumberTheory(unittest.TestCase):
    """Test number theory functions."""

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(-5))

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-7))

    def test_is_odd(self):
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(-5))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(0))

    def test_absolute(self):
        self.assertEqual(absolute(5), 5)
        self.assertEqual(absolute(-5), 5)
        self.assertEqual(absolute(0), 0)
        self.assertAlmostEqual(absolute(-3.7), 3.7)

    def test_ceiling(self):
        self.assertEqual(ceiling(3.2), 4)
        self.assertEqual(ceiling(5.0), 5)
        self.assertEqual(ceiling(-2.3), -2)

    def test_floor(self):
        self.assertEqual(floor(3.7), 3)
        self.assertEqual(floor(5.0), 5)
        self.assertEqual(floor(-2.3), -3)

    def test_round_number(self):
        self.assertEqual(round_number(3.7), 4)
        self.assertEqual(round_number(3.2), 3)
        self.assertAlmostEqual(round_number(3.14159, 2), 3.14)
        self.assertAlmostEqual(round_number(3.14159, 4), 3.1416)


class TestLogarithmic(unittest.TestCase):
    """Test logarithmic functions."""

    def test_log(self):
        self.assertAlmostEqual(log(builtin_math.e), 1)
        self.assertAlmostEqual(log(8, 2), 3)
        self.assertAlmostEqual(log(100, 10), 2)
        with self.assertRaises(MathError):
            log(0)
        with self.assertRaises(MathError):
            log(-5)
        with self.assertRaises(MathError):
            log(10, 1)

    def test_log10(self):
        self.assertAlmostEqual(log10(100), 2)
        self.assertAlmostEqual(log10(1000), 3)
        self.assertAlmostEqual(log10(1), 0)
        with self.assertRaises(MathError):
            log10(0)
        with self.assertRaises(MathError):
            log10(-5)

    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(builtin_math.e), 1)
        self.assertAlmostEqual(natural_log(1), 0)
        with self.assertRaises(MathError):
            natural_log(0)
        with self.assertRaises(MathError):
            natural_log(-5)


class TestGeometry(unittest.TestCase):
    """Test geometry and distance functions."""

    def test_distance_2d(self):
        self.assertAlmostEqual(distance_2d(0, 0, 3, 4), 5)
        self.assertAlmostEqual(distance_2d(1, 1, 4, 5), 5)
        self.assertAlmostEqual(distance_2d(0, 0, 0, 0), 0)

    def test_distance_3d(self):
        self.assertAlmostEqual(distance_3d(0, 0, 0, 1, 1, 1), builtin_math.sqrt(3))
        self.assertAlmostEqual(distance_3d(1, 2, 3, 4, 6, 8), builtin_math.sqrt(50))

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), builtin_math.pi)
        self.assertAlmostEqual(circle_area(2), 4 * builtin_math.pi)
        self.assertEqual(circle_area(0), 0)
        with self.assertRaises(MathError):
            circle_area(-1)

    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(1), 2 * builtin_math.pi)
        self.assertAlmostEqual(circle_circumference(2), 4 * builtin_math.pi)
        self.assertEqual(circle_circumference(0), 0)
        with self.assertRaises(MathError):
            circle_circumference(-1)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 3), 15)
        self.assertEqual(rectangle_area(10, 10), 100)
        self.assertEqual(rectangle_area(0, 5), 0)
        with self.assertRaises(MathError):
            rectangle_area(-5, 3)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(10, 5), 25)
        self.assertEqual(triangle_area(6, 4), 12)
        self.assertEqual(triangle_area(0, 5), 0)
        with self.assertRaises(MathError):
            triangle_area(5, -3)


if __name__ == '__main__':
    unittest.main()
