# 1/3
# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
    print(row)


# 2/3
# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W
    print(i, year, wins)


# 3/3
# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W

    # Check if rangers made Playoffs (1 means yes; 0 means no)
    if row.Playoffs == 1:
        print(i, year, wins)
