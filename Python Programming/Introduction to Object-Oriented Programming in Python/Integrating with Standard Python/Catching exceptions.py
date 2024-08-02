# Modify the function to catch exceptions
def invert_at_index(x, ind):
    try:
        return 1 / x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")


a_list = [5, 6, 0, 7]

# Works okay
print(invert_at_index(a_list, 1))

# Potential ZeroDivisionError
print(invert_at_index(a_list, 2))

# Potential IndexError
print(invert_at_index(a_list, 5))
