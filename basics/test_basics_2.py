# Testing code for "Basics" item 2

from common.testing_code_gen import generated_module_fixture
import pytest

prompt="""Write a Python program that has one function, opposite_day, that takes in a single Boolean argument that denotes whether it is Opposite Day or not. Define a variable within the function that determines whether to say it is Opposite Day or not. Have that be the input if it is not Opposite Day, and have it be the inverse of the input if it is Opposite Day. If that internal variable is true, return 'Today is Opposite Day.' If not, return 'Today is not Opposite Day.'"""

generated_opposite_day_module = generated_module_fixture(
    prompt=prompt
)

def test_opposite_true(generated_opposite_day_module):
    opposite_day = generated_opposite_day_module.opposite_day
    assert opposite_day(True) == 'Today is not Opposite Day.'

def test_opposite_false(generated_opposite_day_module):
    opposite_day = generated_opposite_day_module.opposite_day
    assert opposite_day(False) == 'Today is not Opposite Day.'