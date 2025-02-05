# 1/3
# Get the "count_letter" docstring by using an attribute of the function
docstring = count_letter.__doc__

border = "#" * 28
print("{}\n{}\n{}".format(border, docstring, border))

# 2/3
import inspect

# Inspect the count_letter() function to get its docstring
docstring = inspect.getdoc(count_letter)

border = "#" * 28
print("{}\n{}\n{}".format(border, docstring, border))


# 3/3
import inspect


def build_tooltip(function):
    """Create a tooltip for any function that shows the
    function's docstring.

    Args:
      function (callable): The function we want a tooltip for.

    Returns:
      str
    """
    # Get the docstring for the "function" argument by using inspect
    docstring = inspect.getdoc(function)
    border = "#" * 28
    return "{}\n{}\n{}".format(border, docstring, border)


print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
