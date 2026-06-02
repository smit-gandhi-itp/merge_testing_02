"""Comprehensive math module with various mathematical functions."""

import math as builtin_math
from typing import List, Union


class MathError(Exception):
    """Custom exception for math operations."""
    pass


# Basic Arithmetic Operations
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract b from a.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divide a by b.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Quotient of a and b
        
    Raises:
        MathError: If b is zero
    """
    if b == 0:
        raise MathError("Cannot divide by zero")
    return a / b


def modulo(a: int, b: int) -> int:
    """Calculate a modulo b.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Remainder of a divided by b
        
    Raises:
        MathError: If b is zero
    """
    if b == 0:
        raise MathError("Cannot perform modulo with zero")
    return a % b


# Power and Root Operations
def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """Raise base to the power of exponent.
    
    Args:
        base: Base number
        exponent: Exponent
        
    Returns:
        base raised to the power of exponent
    """
    return base ** exponent


def square(n: Union[int, float]) -> Union[int, float]:
    """Calculate the square of a number.
    
    Args:
        n: Number to square
        
    Returns:
        Square of n
    """
    return n ** 2


def cube(n: Union[int, float]) -> Union[int, float]:
    """Calculate the cube of a number.
    
    Args:
        n: Number to cube
        
    Returns:
        Cube of n
    """
    return n ** 3


def square_root(n: Union[int, float]) -> float:
    """Calculate the square root of a number.
    
    Args:
        n: Number to find square root of
        
    Returns:
        Square root of n
        
    Raises:
        MathError: If n is negative
    """
    if n < 0:
        raise MathError("Cannot calculate square root of negative number")
    return builtin_math.sqrt(n)


def nth_root(n: Union[int, float], root: int) -> float:
    """Calculate the nth root of a number.
    
    Args:
        n: Number to find root of
        root: Which root to calculate
        
    Returns:
        nth root of n
        
    Raises:
        MathError: If root is zero or if n is negative with even root
    """
    if root == 0:
        raise MathError("Root cannot be zero")
    if n < 0 and root % 2 == 0:
        raise MathError("Cannot calculate even root of negative number")
    return n ** (1 / root)


# Factorial and Combinatorics
def factorial(n: int) -> int:
    """Calculate the factorial of n.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        MathError: If n is negative
    """
    if n < 0:
        raise MathError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        nth Fibonacci number
        
    Raises:
        MathError: If n is negative
    """
    if n < 0:
        raise MathError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of a and b.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Greatest common divisor of a and b
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of a and b.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Least common multiple of a and b
        
    Raises:
        MathError: If either a or b is zero
    """
    if a == 0 or b == 0:
        raise MathError("LCM is not defined for zero")
    return abs(a * b) // gcd(a, b)


# Trigonometric Functions
def sin(angle: float, degrees: bool = False) -> float:
    """Calculate the sine of an angle.
    
    Args:
        angle: Angle value
        degrees: If True, angle is in degrees; otherwise radians
        
    Returns:
        Sine of the angle
    """
    if degrees:
        angle = builtin_math.radians(angle)
    return builtin_math.sin(angle)


def cos(angle: float, degrees: bool = False) -> float:
    """Calculate the cosine of an angle.
    
    Args:
        angle: Angle value
        degrees: If True, angle is in degrees; otherwise radians
        
    Returns:
        Cosine of the angle
    """
    if degrees:
        angle = builtin_math.radians(angle)
    return builtin_math.cos(angle)


def tan(angle: float, degrees: bool = False) -> float:
    """Calculate the tangent of an angle.
    
    Args:
        angle: Angle value
        degrees: If True, angle is in degrees; otherwise radians
        
    Returns:
        Tangent of the angle
    """
    if degrees:
        angle = builtin_math.radians(angle)
    return builtin_math.tan(angle)


# Statistical Functions
def mean(numbers: List[Union[int, float]]) -> float:
    """Calculate the arithmetic mean of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Mean of the numbers
        
    Raises:
        MathError: If the list is empty
    """
    if not numbers:
        raise MathError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: List[Union[int, float]]) -> float:
    """Calculate the median of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Median of the numbers
        
    Raises:
        MathError: If the list is empty
    """
    if not numbers:
        raise MathError("Cannot calculate median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def mode(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Calculate the mode of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Mode of the numbers (most frequent value)
        
    Raises:
        MathError: If the list is empty
    """
    if not numbers:
        raise MathError("Cannot calculate mode of empty list")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    return max(frequency, key=frequency.get)


def variance(numbers: List[Union[int, float]]) -> float:
    """Calculate the variance of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Variance of the numbers
        
    Raises:
        MathError: If the list is empty
    """
    if not numbers:
        raise MathError("Cannot calculate variance of empty list")
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)


def standard_deviation(numbers: List[Union[int, float]]) -> float:
    """Calculate the standard deviation of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Standard deviation of the numbers
        
    Raises:
        MathError: If the list is empty
    """
    return builtin_math.sqrt(variance(numbers))


# Number Theory Functions
def is_prime(n: int) -> bool:
    """Check if a number is prime.
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(builtin_math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_even(n: int) -> bool:
    """Check if a number is even.
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is even, False otherwise
    """
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Check if a number is odd.
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is odd, False otherwise
    """
    return n % 2 != 0


def absolute(n: Union[int, float]) -> Union[int, float]:
    """Calculate the absolute value of a number.
    
    Args:
        n: Number
        
    Returns:
        Absolute value of n
    """
    return abs(n)


def ceiling(n: float) -> int:
    """Round a number up to the nearest integer.
    
    Args:
        n: Number to round
        
    Returns:
        Smallest integer greater than or equal to n
    """
    return builtin_math.ceil(n)


def floor(n: float) -> int:
    """Round a number down to the nearest integer.
    
    Args:
        n: Number to round
        
    Returns:
        Largest integer less than or equal to n
    """
    return builtin_math.floor(n)


def round_number(n: float, decimals: int = 0) -> float:
    """Round a number to a specified number of decimal places.
    
    Args:
        n: Number to round
        decimals: Number of decimal places
        
    Returns:
        Rounded number
    """
    return round(n, decimals)


# Logarithmic Functions
def log(n: Union[int, float], base: Union[int, float] = builtin_math.e) -> float:
    """Calculate the logarithm of n with specified base.
    
    Args:
        n: Number to calculate logarithm of
        base: Base of the logarithm (default: e)
        
    Returns:
        Logarithm of n with specified base
        
    Raises:
        MathError: If n is not positive or base is invalid
    """
    if n <= 0:
        raise MathError("Logarithm is only defined for positive numbers")
    if base <= 0 or base == 1:
        raise MathError("Invalid logarithm base")
    return builtin_math.log(n, base)


def log10(n: Union[int, float]) -> float:
    """Calculate the base-10 logarithm of n.
    
    Args:
        n: Number to calculate logarithm of
        
    Returns:
        Base-10 logarithm of n
        
    Raises:
        MathError: If n is not positive
    """
    if n <= 0:
        raise MathError("Logarithm is only defined for positive numbers")
    return builtin_math.log10(n)


def natural_log(n: Union[int, float]) -> float:
    """Calculate the natural logarithm (base e) of n.
    
    Args:
        n: Number to calculate logarithm of
        
    Returns:
        Natural logarithm of n
        
    Raises:
        MathError: If n is not positive
    """
    if n <= 0:
        raise MathError("Logarithm is only defined for positive numbers")
    return builtin_math.log(n)


# Distance and Geometry
def distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculate the Euclidean distance between two 2D points.
    
    Args:
        x1: X-coordinate of first point
        y1: Y-coordinate of first point
        x2: X-coordinate of second point
        y2: Y-coordinate of second point
        
    Returns:
        Distance between the two points
    """
    return builtin_math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def distance_3d(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    """Calculate the Euclidean distance between two 3D points.
    
    Args:
        x1: X-coordinate of first point
        y1: Y-coordinate of first point
        z1: Z-coordinate of first point
        x2: X-coordinate of second point
        y2: Y-coordinate of second point
        z2: Z-coordinate of second point
        
    Returns:
        Distance between the two points
    """
    return builtin_math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def circle_area(radius: float) -> float:
    """Calculate the area of a circle.
    
    Args:
        radius: Radius of the circle
        
    Returns:
        Area of the circle
        
    Raises:
        MathError: If radius is negative
    """
    if radius < 0:
        raise MathError("Radius cannot be negative")
    return builtin_math.pi * radius ** 2


def circle_circumference(radius: float) -> float:
    """Calculate the circumference of a circle.
    
    Args:
        radius: Radius of the circle
        
    Returns:
        Circumference of the circle
        
    Raises:
        MathError: If radius is negative
    """
    if radius < 0:
        raise MathError("Radius cannot be negative")
    return 2 * builtin_math.pi * radius


def rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        length: Length of the rectangle
        width: Width of the rectangle
        
    Returns:
        Area of the rectangle
        
    Raises:
        MathError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise MathError("Dimensions cannot be negative")
    return length * width


def triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle.
    
    Args:
        base: Base of the triangle
        height: Height of the triangle
        
    Returns:
        Area of the triangle
        
    Raises:
        MathError: If base or height is negative
    """
    if base < 0 or height < 0:
        raise MathError("Dimensions cannot be negative")
    return 0.5 * base * height
