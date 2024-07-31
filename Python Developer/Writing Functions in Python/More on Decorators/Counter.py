def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return wrapper

    # Set count to 0 to initialize call count for each new decorated function
    wrapper.count = 0
    # Return the new decorated function
    return wrapper


# Decorate foo() with the counter() decorator
@counter
def foo():
    print("calling foo()")


foo()
foo()

print("foo() was called {} times.".format(foo.count))
