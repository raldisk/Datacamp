# 1/3
# Import needed functionality
from collections import Counter


def plot_counter(counter, n_most_common=5):
    # Subset the n_most_common items from the input counter
    top_items = counter.most_common(n_most_common)
    # Plot `top_items`
    plot_counter_most_common(top_items)


# 2/3
# Import needed functionality
from collections import Counter


def sum_counters(counters):
    # Sum the inputted counters
    return sum(counters, Counter())


# 3/3
# from .counter_utils import plot_counter, sum_counters
