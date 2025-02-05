# 1/2
# Fibonacci sequence
def fibonacci(n):
    # Define the base case
    if n <= 1:
        return n
    else:
        # Call recursively to fibonacci
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))


# 2/2
cache = [None] * (100)


def fibonacci(n):
    if n <= 1:
        return n

    # Check if the value exists
    if not cache[n]:
        # Save the result in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]


print(fibonacci(6))
