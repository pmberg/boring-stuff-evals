# Testing code for "Basics" item 1

from common.testing_code_gen import generated_module_fixture
import pytest

prompt=("Write a Python program that has one function, spam_greeter, that takes in one argument called spam, "
"returns 'Hello' if 1 is stored in spam, 'Howdy' if 2 is stored in spam, " 
"and 'Greetings!' if anything else is stored in spam.")

generated_spam_module = generated_module_fixture(
    prompt=prompt
)

def test_spam_hello(generated_spam_module):
    spam = generated_spam_module.spam_greeter
    assert spam(1) == 'Hello'

def test_spam_howdy(generated_spam_module):
    spam = generated_spam_module.spam_greeter
    assert spam(2) == 'Howdy'

def test_spam_greetings(generated_spam_module):
    spam = generated_spam_module.spam_greeter
    assert spam(10) == 'Greetings!'
    assert spam(-1) == 'Greetings!'
    assert spam('spam') == 'Greetings!'