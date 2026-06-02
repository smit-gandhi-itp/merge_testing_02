"""Simple Math Functions Module

This module provides basic mathematical operations including
arithmetic and some advanced functions.
"""

import math


def add(a, b):
    """Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b


def subtract(a, b):
    """Subtract second number from first number.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Difference of a and b
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    """
    return a * b


def divide(a, b):
    """Divide first number by second number.
    
    Args:
        a (float): Numerator
        b (float): Denominator
    
    Returns:
        float: Quotient of a and b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(base, exponent):
    """Raise base to the power of exponent.
    
    Args:
        base (float): Base number
        exponent (float): Exponent
    
    Returns:
        float: base raised to the power of exponent
    """
    return base ** exponent


def square_root(n):
    """Calculate the square root of a number.
    
    Args:
        n (float): Number to find square root of
    
    Returns:
        float: Square root of n
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return math.sqrt(n)


if __name__ == "__main__":
    # Example usage and tests
    print("=== Simple Math Functions Demo ===")
    print()
    
    # Addition
    print(f"Addition: 10 + 5 = {add(10, 5)}")
    
    # Subtraction
    print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")
    
    # Multiplication
    print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
    
    # Division
    print(f"Division: 10 / 5 = {divide(10, 5)}")
    
    # Power
    print(f"Power: 2 ^ 8 = {power(2, 8)}")
    
    # Square Root
    print(f"Square Root: √16 = {square_root(16)}")
    
    print()
    print("=== Error Handling Demo ===")
    
    # Test division by zero
    try:
        result = divide(10, 0)
    except ValueError as e:
        print(f"Division by zero error: {e}")
    
    # Test square root of negative
    try:
        result = square_root(-4)
    except ValueError as e:
        print(f"Square root error: {e}")
