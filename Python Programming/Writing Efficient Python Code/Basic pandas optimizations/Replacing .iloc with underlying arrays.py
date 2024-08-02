# 1/3
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df["W"].values, baseball_df["G"].values)


# 2/3
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df["W"].values, baseball_df["G"].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df["WP"] = win_percs_np

print(baseball_df.head())


# 3/3
# The NumPy array approach is faster than the .iloc approach.
