"""Random assignment of subjects
Having built trust from your last work with the agricultural firm, you have been given the task of properly setting up the experiment.

Use your knowledge of best practice experimental design set up to assign the sheep to two even groups of 250 each.

The weights DataFrame is available for you to use. Additionally, numpy and pandas have been imported as np and pd respectively.

Instructions
100 XP
Randomly select 250 subjects from the weights DataFrame into a new DataFrame group1 without replacement.
Put the remaining 250 subjects into group2.
Concatenate the descriptive statistics of your two newly created DataFrames."""

# Randomly assign half
group1_random = weights.sample(
    n=250, random_state=42, replace=False
)  # Randomly select 250 subjects

# Create second assignment
group2_random = weights[
    ~weights["id"].isin(group1_random["id"])
]  # Select remaining subjects

# Compare assignments
compare_df_random = pd.concat(
    [group1_random["weight"], group2_random["weight"]], axis=1
)
compare_df_random.columns = ["group1", "group2"]
print(compare_df_random.describe())
