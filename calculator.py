"""Basic Calculator Module

This module provides basic arithmetic operations including:
- Addition
- Subtraction
- Multiplication
- Division
"""


def add(a, b):
    """Add two numbers.
    
    Args:
        a (int|float): First number
        b (int|float): Second number
    
    Returns:
        int|float: Sum of a and b
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(2.5, 3.5)
        6.0
    """
    return a + b


def subtract(a, b):
    """Subtract second number from first number.
    
    Args:
        a (int|float): First number
        b (int|float): Second number to subtract
    
    Returns:
        int|float: Difference of a and b
    
    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(3, 5)
        -2
        >>> subtract(10.5, 2.5)
        8.0
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers.
    
    Args:
        a (int|float): First number
        b (int|float): Second number
    
    Returns:
        int|float: Product of a and b
    
    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(-2, 3)
        -6
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


def divide(a, b):
    """Divide first number by second number.
    
    Args:
        a (int|float): Numerator
        b (int|float): Denominator
    
    Returns:
        float: Quotient of a and b
    
    Raises:
        ValueError: If b is zero
    
    Examples:
        >>> divide(6, 3)
        2.0
        >>> divide(5, 2)
        2.5
        >>> divide(10, 4)
        2.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    # Example usage
    print("Calculator Demo")
    print("===============")
    print(f"Addition: 10 + 5 = {add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
    print(f"Division: 10 / 5 = {divide(10, 5)}")
