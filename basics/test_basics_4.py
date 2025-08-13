# Testing code for "Basics" item 4

from common.testing_code_gen import generated_module_fixture
import pytest

prompt="Write a program that has a function called factorial() that computes the factorial of any integer."

generated_factorial_module = generated_module_fixture(
    prompt=prompt
)

def test_factorial_basic(generated_factorial_module):
    factorial = generated_factorial_module.factorial
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_negative_input(generated_factorial_module):
    factorial = generated_factorial_module.factorial
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(-2)

def test_factorial_large_number(generated_factorial_module):
    factorial = generated_factorial_module.factorial
    assert factorial(10) == 3628800