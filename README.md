# merge_testing_02

## Python Calculator Project

A simple Python calculator module with comprehensive test coverage using pytest.

### Features

- **Basic arithmetic operations:**
  - Addition
  - Subtraction
  - Multiplication
  - Division (with zero-division protection)

### Files

- `calculator.py` - Main calculator module with four basic functions
- `test_calculator.py` - Comprehensive pytest test suite
- `requirements.txt` - Python dependencies (pytest)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/smit-gandhi-itp/merge_testing_02.git
   cd merge_testing_02
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Running the Calculator

```python
from calculator import add, subtract, multiply, divide

# Addition
result = add(10, 5)  # Returns 15

# Subtraction
result = subtract(10, 5)  # Returns 5

# Multiplication
result = multiply(10, 5)  # Returns 50

# Division
result = divide(10, 5)  # Returns 2.0
```

Or run the demo:
```bash
python calculator.py
```

#### Running Tests

Run all tests:
```bash
pytest test_calculator.py
```

Run with verbose output:
```bash
pytest test_calculator.py -v
```

Run with coverage report:
```bash
pytest test_calculator.py --cov=calculator --cov-report=term-missing
```

### Test Coverage

The test suite includes:
- ✅ 40+ test cases
- ✅ Positive and negative number tests
- ✅ Floating-point arithmetic tests
- ✅ Edge cases (zero, division by zero)
- ✅ Parametrized tests for efficiency
- ✅ Exception handling tests

### Project Structure

```
merge_testing_02/
├── calculator.py          # Main calculator module
├── test_calculator.py     # Pytest test suite
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

### License

This project is open source and available for educational purposes.
