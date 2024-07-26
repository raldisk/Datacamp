"""Non-random assignment of subjects
An agricultural firm is conducting an experiment to measure how feeding sheep different types of grass affects their weight. They have asked for your help to properly set up the experiment. One of their managers has said you can perform the subject assignment by taking the top 250 rows from the DataFrame and that should be fine.

Your task is to use your analytical skills to demonstrate why this might not be a good idea. Assign the subjects to two groups using non-random assignment (the first 250 rows) and observe the differences in descriptive statistics.

You have received the DataFrame, weights which has a column containing the weight of the sheep and a unique id column.

numpy and pandas have been imported as np and pd, respectively.

Instructions
Use DataFrame slicing to put the first 250 rows of weights into group1_non_rand and the remaining into group2_non_rand.
Generate descriptive statistics of the two groups and concatenate them into a single DataFrame.
Print out to observe the differences."""

# Non-random assignment
group1_non_rand = weights.iloc[:250]  # First 250 rows
group2_non_rand = weights.iloc[250:]  # Remaining rows

# Compare descriptive statistics of groups
compare_df_non_rand = pd.concat(
    [group1_non_rand["weight"], group2_non_rand["weight"]], axis=1
)
compare_df_non_rand.columns = ["group1", "group2"]

# Print to assess
print(compare_df_non_rand.describe())
