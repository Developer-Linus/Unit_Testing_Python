# Unit Testing Python
- Testing ensures that code functions as intended.
- **Benefits**
(a) Catch bugs early <br>
(b) Improve code quality. <br>
(c) Increase confidence in code changes. 

- There are various types of tests to do depending on test's purpose.
- Here, we will dwell on unit testing. **Unit testing** involves testing individual units of code, typically functions or classes.
- It ensures that each unit performs its intended behaviour with specific inputs.
## Why Unit Tests
- Python provides a built-in module called `unittest` for writing tests. 
## Test Cases
- We define individual tests as test cases within a TestCase. Each test case has specific method named with `test_` followed by descriptive name. Inside this method, we write code to:
1. Set up the test environment (e.g, create objects, initialize data). <br>
2. Execute the code we want to test (e.g., call the function with specific inputs).
    - Assert the expected outcome using `self.assertEqual(actual, expected)`.

## Test Runners
- Once you've written your test cases, you need a test runner to execute them. The `unittest` module provides a `TextTestRunner` class that can be used to run all test cases within a test suite.

### What is Unit Testing in Python?

**Unit Testing** is a software testing technique in which individual units or components of a program are tested in isolation to ensure that they work as expected. In Python, the `unittest` module is used for writing and running unit tests. It is part of the standard library, which means it comes pre-installed with Python.

---

### Why is Unit Testing Important?

1. **Ensures Code Quality**: Helps catch bugs early in the development cycle.
2. **Facilitates Refactoring**: Confirms that changes in the codebase don’t break existing functionality.
3. **Improves Code Documentation**: Tests often serve as additional documentation for how a function or method should behave.
4. **Encourages Modular Design**: Promotes breaking down code into smaller, testable components.

---

### Key Concepts of Unit Testing

1. **Test Case**: The smallest unit of testing. It checks for a specific response to a particular input.
2. **Test Suite**: A collection of test cases.
3. **Test Runner**: Executes the tests and provides the results.
4. **Assertion**: A statement that checks if a condition is true. If the condition is false, the test fails.

---

### `unittest` Module Overview

The `unittest` module provides tools for creating and running tests. Here are its main components:

1. **TestCase**: Base class for writing new test cases.
2. **setUp() and tearDown()**:
   - `setUp()` is run before each test method to prepare the environment.
   - `tearDown()` is run after each test method to clean up.
3. **assert Methods**:
   - `assertEqual(a, b)`: Checks if `a == b`.
   - `assertNotEqual(a, b)`: Checks if `a != b`.
   - `assertTrue(x)`: Checks if `x` is `True`.
   - `assertFalse(x)`: Checks if `x` is `False`.
   - `assertRaises(exc, func, *args, **kwds)`: Checks if a specific exception is raised.

---

### Writing Unit Tests in Python

Here’s a step-by-step example:

#### 1. Code to Test

```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

#### 2. Writing Tests

```python
# test_math_operations.py
import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertRaises(ValueError, divide, 10, 0)

if __name__ == "__main__":
    unittest.main()
```

#### Explanation of the Code

1. **Import Modules**: Import `unittest` and the module to test.
2. **Create a Test Class**: Inherit from `unittest.TestCase`.
3. **Write Test Methods**: Each method name should start with `test_`.
4. **Use Assertions**: Use `assertEqual`, `assertRaises`, etc., to check the output.

#### 3. Run Tests

To run the tests, use:

```bash
python test_math_operations.py
```

---

### Best Practices for Unit Testing

1. **Test Single Responsibility**: Each test should focus on a single aspect of the functionality.
2. **Use Meaningful Names**: Name your test methods clearly, e.g., `test_add_with_positive_numbers`.
3. **Mock External Dependencies**: Use libraries like `unittest.mock` to mock I/O or API calls.
4. **Keep Tests Independent**: Ensure tests do not rely on the output of others.
5. **Test Edge Cases**: Include tests for invalid inputs and boundary conditions.

---

### Advanced Features

1. **Mocking**:
   - Simulate external dependencies using `unittest.mock`.
   ```python
   from unittest.mock import Mock
   mock_function = Mock(return_value=10)
   assert mock_function() == 10
   ```

2. **Parameterized Tests**:
   - Test the same logic with different inputs using libraries like `pytest` or `unittest`'s `subTest`.
   ```python
   def test_add(self):
       for a, b, expected in [(1, 2, 3), (0, 0, 0), (-1, -1, -2)]:
           with self.subTest(a=a, b=b):
               self.assertEqual(add(a, b), expected)
   ```

3. **Test Coverage**:
   - Measure how much of your code is covered by tests using `coverage.py`.
   ```
   pip install coverage
   coverage run -m unittest discover
   coverage report -m
   ```

---

### Summary

Unit testing ensures that individual components of your code work as intended. Python's `unittest` module provides a structured way to write and execute tests. By following best practices and leveraging advanced features like mocking and test coverage, you can write robust, maintainable tests for your applications.



Exercise 1: Understanding the Importance of Testing

Instruction:

Write a small Python function (e.g., a function to calculate the square of a number) and intentionally introduce a bug (e.g., incorrect calculation logic).
Exercise 2: Writing Basic Unit Tests

Instruction:

Use the unittest module in Python to create a test case for the buggy function from Exercise 1.
Write test methods to check different scenarios (e.g., valid input, invalid input) and verify expected behavior.