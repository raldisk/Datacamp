# 1/4
# Display the first five rows of the DataFrame
print(dbacks_df.head())


# 2/4
# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row["W"], row["G"]), axis=1)
print(win_percs, "\n")


# 3/4
# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row["W"], row["G"]), axis=1)
print(win_percs, "\n")

# Append a new column to dbacks_df
dbacks_df["WP"] = win_percs
print(dbacks_df, "\n")

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df["WP"] >= 0.50])


# 4/4
# The manager who claimed the team has not made the playoffs every year they've had a win percentage of 0.50 or greater.
