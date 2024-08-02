import pytest


@pytest.fixture
def init_list():
    return []


# Declare the fixture with autouse
@pytest.fixture(autouse=True)
def add_numbers_to_list(init_list):
    init_list.extend([i for i in range(10)])


# Complete the tests
def test_elements(init_list):
    assert len(init_list) == 10
    assert init_list == [i for i in range(10)]


# pytest auto_ad_numbers.py
