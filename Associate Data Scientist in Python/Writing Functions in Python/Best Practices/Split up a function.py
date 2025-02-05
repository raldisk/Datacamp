# 1/2
def mean(values):
    """Get the mean of a sorted list of values

    Args:
      values (iterable of float): A list of numbers

    Returns:
      float
    """
    # Write the mean() function
    mean = sum(values) / len(values)

    return mean


# 2/2
def median(values):
    """Get the median of a sorted list of values

    Args:
      values (iterable of float): A list of numbers

    Returns:
      float
    """
    # Write the median() function
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]
    return median
