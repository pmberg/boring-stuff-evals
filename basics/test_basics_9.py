# Testing code for "Basics" item 9

from common.testing_code_gen import generated_module_fixture
import pytest
import re

prompt="""
Write a Python program that has one function, collatz, that takes in a positive integer as its argument and prints the Collatz sequence starting at that integer until it reaches 1. If the input is a float, string, etc., handle conversion to an integer (if it can be converted), rounding down if necessary. However, if the input is the string "squirrel," raise a TypeError with the error message "Squirrels can't go out in the hail!"
"""

generated_item_9_module = generated_module_fixture(
    prompt=prompt
)

def _parse_printed_ints(s: str):
    """Extract integers from arbitrary printed formatting (spaces/newlines/commas)."""
    return [int(x) for x in re.findall(r"-?\d+", s)]

def test_collatz_exists_and_is_callable(generated_item_9_module):
    assert hasattr(generated_item_9_module, "collatz")
    assert callable(generated_item_9_module.collatz)

def test_collatz_basic_even(capsys, generated_item_9_module):
    collatz = generated_item_9_module.collatz
    # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    expected = [6, 3, 10, 5, 16, 8, 4, 2, 1]
    ret = collatz(6)
    captured = capsys.readouterr().out
    printed = _parse_printed_ints(captured)
    assert printed == expected

def test_collatz_basic_odd(capsys, generated_item_9_module):
    collatz = generated_item_9_module.collatz
    # 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    expected = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    collatz(7)
    captured = capsys.readouterr().out
    printed = _parse_printed_ints(captured)
    assert printed == expected

def test_collatz_starting_at_one(capsys, generated_item_9_module):
    collatz = generated_item_9_module.collatz
    collatz(1)
    captured = capsys.readouterr().out
    printed = _parse_printed_ints(captured)
    assert printed == [1]

def test_collatz_sequence_termination(capsys, generated_item_9_module):
    collatz = generated_item_9_module.collatz
    # For a larger start, ensure the final value is 1.
    collatz(27)
    captured = capsys.readouterr().out
    printed = _parse_printed_ints(captured)
    assert printed[-1] == 1
    # Ensure the sequence starts with the input.
    assert printed[0] == 27

def test_collatz_basic_float(capsys, generated_item_9_module):
    collatz = generated_item_9_module.collatz
    # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    expected = [6, 3, 10, 5, 16, 8, 4, 2, 1]
    ret = collatz('6.1')
    captured = capsys.readouterr().out
    printed = _parse_printed_ints(captured)
    assert printed == expected
    ret = collatz('6.9')
    captured = capsys.readouterr().out
    printed = _parse_printed_ints(captured)
    assert printed == expected

def test_collatz_basic_string(capsys, generated_item_9_module):
    collatz = generated_item_9_module.collatz
    # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    expected = [6, 3, 10, 5, 16, 8, 4, 2, 1]
    ret = collatz('6')
    captured = capsys.readouterr().out
    printed = _parse_printed_ints(captured)
    assert printed == expected

def test_collatz_basic_squirrel(capsys, generated_item_9_module):
    collatz = generated_item_9_module.collatz
    # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    expected = "Squirrels can't go out in the hail!"
    with pytest.raises(TypeError, match=expected):
        ret = collatz('squirrel')