# 1/3
# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
    print(a + b)


print_sum(15, 20)

# 2/3
# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)


@run_five_times
def print_sum(a, b):
    print(a + b)


print_sum(4, 100)


# 3/3
# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print("What is happening?!?!")
