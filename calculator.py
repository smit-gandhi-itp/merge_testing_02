"""Calculator module with basic arithmetic operations."""


class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b

    def divide(self, a, b):
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        """Raise base to the power of exponent.
        
        Args:
            base: Base number
            exponent: Exponent
            
        Returns:
            base raised to the power of exponent
        """
        return base ** exponent

    def modulo(self, a, b):
        """Calculate the remainder of a divided by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Remainder of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero divisor")
        return a % b


if __name__ == "__main__":
    # Example usage
    calc = Calculator()
    print(f"Addition: 10 + 5 = {calc.add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {calc.subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {calc.multiply(10, 5)}")
    print(f"Division: 10 / 5 = {calc.divide(10, 5)}")
    print(f"Power: 2 ^ 3 = {calc.power(2, 3)}")
    print(f"Modulo: 10 % 3 = {calc.modulo(10, 3)}")
