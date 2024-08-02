# Import the pytest library
import pytest


def multiple_of_two(num):
    if num == 0:
        raise (ValueError)
    return num % 2 == 0


def test_numbers():
    assert multiple_of_two(2) == True
    assert multiple_of_two(3) == False


def test_zero():
    with pytest.raises(ValueError):
        multiple_of_two(0)
