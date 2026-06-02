"""Simple Calculator Module

This module provides basic arithmetic operations including addition,
subtraction, multiplication, division, power, and modulo operations.
"""


class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    @staticmethod
    def add(a, b):
        """Add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """Subtract b from a.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Difference of a and b
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """Divide a by b.
        
        Args:
            a (float): Numerator
            b (float): Denominator
            
        Returns:
            float: Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a, b):
        """Raise a to the power of b.
        
        Args:
            a (float): Base number
            b (float): Exponent
            
        Returns:
            float: a raised to the power of b
        """
        return a ** b

    @staticmethod
    def modulo(a, b):
        """Calculate the modulo of a and b.
        
        Args:
            a (float): Dividend
            b (float): Divisor
            
        Returns:
            float: Remainder of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")
        return a % b


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    
    print("Calculator Demo")
    print("=" * 40)
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"10 ** 2 = {calc.power(10, 2)}")
    print(f"10 % 3 = {calc.modulo(10, 3)}")
    print("=" * 40)


if __name__ == "__main__":
    main()
