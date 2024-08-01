# 1/2
def multiple_of_two(num):
    if num == 0:
        raise (ValueError)
    return num % 2 == 0


def test_numbers():
    # Write the "True" test below
    assert multiple_of_two(3) == True


# 2/2
def multiple_of_two(num):
    if num == 0:
        raise (ValueError)
    return num % 2 == 0


def test_numbers():
    assert multiple_of_two(2) == True
    # Write the "False" test below
    assert multiple_of_two(3) == False
