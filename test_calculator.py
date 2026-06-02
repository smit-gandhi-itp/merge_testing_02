"""Unit tests for calculator module using pytest.

Run tests with:
    pytest test_calculator.py
    pytest test_calculator.py -v  # verbose output
    pytest test_calculator.py --cov=calculator  # with coverage
"""

import pytest
from calculator import add, subtract, multiply, divide


class TestAddition:
    """Test cases for addition function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, -20) == -30
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(-5, 5) == 0
        assert add(10, -3) == 7
        assert add(-10, 3) == -7
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(0, 0) == 0


class TestSubtraction:
    """Test cases for subtraction function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 5) == 5
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -5) == -5
    
    def test_subtract_mixed_numbers(self):
        """Test subtracting mixed positive and negative numbers."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
    
    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(10.7, 3.2) == pytest.approx(7.5)
    
    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
    
    def test_subtract_same_number(self):
        """Test subtracting a number from itself."""
        assert subtract(5, 5) == 0
        assert subtract(-5, -5) == 0


class TestMultiplication:
    """Test cases for multiplication function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-5, -4) == 20
    
    def test_multiply_mixed_numbers(self):
        """Test multiplying positive and negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(5, -4) == -20
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 4) == 10.0
        assert multiply(1.5, 2.5) == pytest.approx(3.75)
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_by_one(self):
        """Test multiplying by one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5


class TestDivision:
    """Test cases for division function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(6, 3) == 2.0
        assert divide(10, 2) == 5.0
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-6, -3) == 2.0
        assert divide(-10, -2) == 5.0
    
    def test_divide_mixed_numbers(self):
        """Test dividing positive and negative numbers."""
        assert divide(-6, 3) == -2.0
        assert divide(10, -2) == -5.0
    
    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(7.5, 2.5) == 3.0
        assert divide(10.0, 4.0) == 2.5
    
    def test_divide_with_remainder(self):
        """Test division that results in a decimal."""
        assert divide(5, 2) == 2.5
        assert divide(7, 3) == pytest.approx(2.333333, rel=1e-5)
    
    def test_divide_by_one(self):
        """Test dividing by one."""
        assert divide(5, 1) == 5.0
        assert divide(-5, 1) == -5.0
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0.0
        assert divide(0, -5) == 0.0
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(0, 0)


# Parametrized tests for comprehensive coverage
class TestParametrized:
    """Parametrized test cases for efficient testing."""
    
    @pytest.mark.parametrize("a, b, expected", [
        (1, 1, 2),
        (0, 0, 0),
        (-1, -1, -2),
        (100, 200, 300),
        (0.1, 0.2, pytest.approx(0.3)),
    ])
    def test_add_parametrized(self, a, b, expected):
        """Parametrized test for addition."""
        assert add(a, b) == expected
    
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),
        (0, 0, 0),
        (-5, -3, -2),
        (100, 50, 50),
    ])
    def test_subtract_parametrized(self, a, b, expected):
        """Parametrized test for subtraction."""
        assert subtract(a, b) == expected
    
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 3, -6),
        (4, 5, 20),
    ])
    def test_multiply_parametrized(self, a, b, expected):
        """Parametrized test for multiplication."""
        assert multiply(a, b) == expected
    
    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2.0),
        (10, 2, 5.0),
        (-6, 3, -2.0),
        (5, 2, 2.5),
    ])
    def test_divide_parametrized(self, a, b, expected):
        """Parametrized test for division."""
        assert divide(a, b) == expected
