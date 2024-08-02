# 1/4
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA


# 2/4
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)

    run_diffs.append(run_diff)


# 3/4
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)

    run_diffs.append(run_diff)

# Append new column
yankees_df["RD"] = run_diffs
print(yankees_df)


# 4/4
# In 1998 (with a Run Differential of 309)
