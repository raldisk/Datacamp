def returns_dict(func):
    # Complete the returns_dict() decorator
    def wrapper(____):
        result = ____
        assert type(result) == dict
        return result

    return wrapper


@returns_dict
def foo(value):
    return value


try:
    print(foo([1, 2, 3]))
except AssertionError:
    print("foo() did not return a dict!")
