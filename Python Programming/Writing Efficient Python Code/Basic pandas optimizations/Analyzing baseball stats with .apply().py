# 1/3

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)


# 2/3
# Gather total runs scored in all games per year
total_runs_scored = rays_df[["RS", "RA"]].apply(sum, axis=1)
print(total_runs_scored)


# 3/3
# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row["Playoffs"]), axis=1)
print(textual_playoffs)
