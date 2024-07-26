"""Blocking experimental data
You are working with a manufacturing firm that wants to conduct some experiments on worker productivity. Their dataset only contains 100 rows, so it's important that experimental groups are balanced.

This sounds like a great opportunity to use your knowledge of blocking to assist them. They have provided a productivity_subjects DataFrame. Split the provided dataset into two even groups of 50 entries each.

The libraries numpy and pandas have been imported as np and pd respectively.

Instructions
100 XP
Randomly select 50 subjects from the productivity_subjects DataFrame into a new DataFrame block_1 without replacement.
Set a new column, block to 1 for the block_1 DataFrame.
Assign the remaining subjects to a DataFrame called block_2 and set the block column to 2 for this DataFrame.
Concatenate the blocks together into a single DataFrame, and print the count of each value in the block column to confirm the blocking worked.
"""

# Randomly assign half
block_1 = productivity_subjects.sample(n=50, random_state=42, replace=False)

# Set the block column
block_1["block"] = 1

# Create second assignment and label
block_2 = productivity_subjects[~productivity_subjects.index.isin(block_1.index)].copy()
block_2["block"] = 2

# Concatenate and print
productivity_combined = pd.concat([block_1, block_2], axis=0)
print(productivity_combined["block"].value_counts())
