import pytest
from docker_file_test import factorial

def test_factorial():
    # Normal cases
    assert factorial(0) == 1
    assert factorial(1.0) == 1
    assert factorial(6) == 720
    assert factorial(6.0) == 720

    # Error cases
    with pytest.raises(ValueError):
        factorial(1.1)
    with pytest.raises(ValueError):
        factorial(-2)
    with pytest.raises(TypeError):
        factorial("pangolin")