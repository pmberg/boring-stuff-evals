# Testing code for "Basics" item 3

from common.testing_code_gen import generated_module_fixture
import pytest

prompt="""Write a Python program has one function, storage, that computes the discrepancy between advertised and actual storage capacities for computer storage devices. It takes in two arguments: unit and ad_capacity. Unit can be kb, mb, gb, or tb, all as strings. If kb, multiply ad_capabity by 10^3/2^10, if mb, multiply by 10^6/2^20, and so on. Return the actual capacity as computed here."""

generated_storage_module = generated_module_fixture(
    prompt=prompt
)

def test_storage_kb(generated_storage_module):
    storage = generated_storage_module.storage
    true_ratio = (10**3)/(2**10)
    assert storage('kb', 100) == 100*true_ratio
    assert storage('kb', 1) == 1*true_ratio
    assert storage('kb', 0.02) == 0.02*true_ratio
    assert storage('kb', 52000) == 52000*true_ratio
    assert storage('kb', 7) == 7*true_ratio

def test_storage_mb(generated_storage_module):
    storage = generated_storage_module.storage
    true_ratio = (10**6)/(2**20)
    assert storage('mb', 100) == 100*true_ratio
    assert storage('mb', 1) == 1*true_ratio
    assert storage('mb', 0.02) == 0.02*true_ratio
    assert storage('mb', 52000) == 52000*true_ratio
    assert storage('mb', 7) == 7*true_ratio

def test_storage_gb(generated_storage_module):
    storage = generated_storage_module.storage
    true_ratio = (10**9)/(2**30)
    assert storage('gb', 100) == 100*true_ratio
    assert storage('gb', 1) == 1*true_ratio
    assert storage('gb', 0.02) == 0.02*true_ratio
    assert storage('gb', 52000) == 52000*true_ratio
    assert storage('gb', 7) == 7*true_ratio

def test_storage_tb(generated_storage_module):
    storage = generated_storage_module.storage
    true_ratio = (10**12)/(2**40)
    assert storage('tb', 100) == 100*true_ratio
    assert storage('tb', 1) == 1*true_ratio
    assert storage('tb', 0.02) == 0.02*true_ratio
    assert storage('tb', 52000) == 52000*true_ratio
    assert storage('tb', 7) == 7*true_ratio