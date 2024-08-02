# 1/3
def factorial(n):
    if n == 0:
        return 1
    elif type(n) == int:
        return n * factorial(n - 1)
    else:
        return -1


# Test case: expected input
def test_regular():
    assert factorial(5) == 120


# 2/3
def factorial(n):
    if n == 0:
        return 1
    elif type(n) == int:
        return n * factorial(n - 1)
    else:
        return -1


# Test case: input 0
def test_zero():
    assert factorial(0) == 1


# 3/3
def factorial(n):
    if n == 0:
        return 1
    elif type(n) == int:
        return n * factorial(n - 1)
    else:
        return -1


# Test case: string input '5'
def test_str():
    assert factorial("5") == -1
