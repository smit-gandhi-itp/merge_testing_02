# merge_testing_02

A simple Python calculator module with comprehensive unit tests.

## Overview

This repository contains a basic calculator implementation in Python that provides essential arithmetic operations. The calculator is designed with clean code principles, proper documentation, and extensive test coverage.

## Features

The calculator supports the following operations:

- **Addition** (`add`): Add two numbers
- **Subtraction** (`subtract`): Subtract one number from another
- **Multiplication** (`multiply`): Multiply two numbers
- **Division** (`divide`): Divide one number by another (with zero-division protection)
- **Power** (`power`): Raise a number to a power
- **Modulo** (`modulo`): Calculate the remainder of division (with zero-division protection)

## Project Structure

```
merge_testing_02/
├── calculator.py          # Main calculator module
├── test_calculator.py     # Comprehensive unit tests
└── README.md             # This file
```

## Installation

No external dependencies are required. This project uses only Python standard library.

### Requirements

- Python 3.6 or higher

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/smit-gandhi-itp/merge_testing_02.git
   cd merge_testing_02
   ```

## Usage

### As a Module

```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(10, 5)        # 15
result = calc.subtract(10, 5)   # 5
result = calc.multiply(10, 5)   # 50
result = calc.divide(10, 5)     # 2.0
result = calc.power(2, 3)       # 8
result = calc.modulo(10, 3)     # 1
```

### Running the Demo

Run the calculator module directly to see a demonstration:

```bash
python calculator.py
```

Output:
```
Calculator Demo
========================================
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
10 ** 2 = 100
10 % 3 = 1
========================================
```

## Testing

The project includes comprehensive unit tests covering:

- Basic operations with positive numbers
- Operations with negative numbers
- Floating-point arithmetic
- Edge cases (zero, large numbers, small numbers)
- Error handling (division by zero, modulo by zero)
- Mixed type operations (int and float)

### Running Tests

Run all tests with verbose output:

```bash
python test_calculator.py
```

Or use Python's unittest module:

```bash
python -m unittest test_calculator.py -v
```

Or run specific test cases:

```bash
python -m unittest test_calculator.TestCalculator.test_add_positive_numbers -v
```

### Test Coverage

The test suite includes:

- **TestCalculator**: 30+ test methods covering all operations
- **TestCalculatorEdgeCases**: Additional tests for boundary conditions

All tests validate:
- ✅ Correct mathematical results
- ✅ Proper error handling
- ✅ Edge case behavior
- ✅ Type compatibility

## Error Handling

The calculator includes proper error handling:

```python
# Division by zero
try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(e)  # "Cannot divide by zero"

# Modulo by zero
try:
    result = calc.modulo(10, 0)
except ValueError as e:
    print(e)  # "Cannot perform modulo with zero"
```

## Code Quality

- **Documentation**: All functions include docstrings with parameter and return type information
- **Type Hints**: Clear parameter descriptions in docstrings
- **Error Messages**: Descriptive error messages for invalid operations
- **Test Coverage**: Comprehensive unit tests with 100% code coverage
- **Code Style**: Follows PEP 8 Python style guidelines

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Guidelines

1. Ensure all tests pass before submitting PR
2. Add tests for any new functionality
3. Follow PEP 8 style guidelines
4. Update documentation as needed

## License

This project is open source and available for educational purposes.

## Author

Created for testing and demonstration purposes.

## Changelog

### Version 1.0.0 (Initial Release)
- ✨ Basic arithmetic operations (add, subtract, multiply, divide)
- ✨ Advanced operations (power, modulo)
- ✨ Comprehensive error handling
- ✨ Full unit test suite with 30+ test cases
- ✨ Complete documentation
