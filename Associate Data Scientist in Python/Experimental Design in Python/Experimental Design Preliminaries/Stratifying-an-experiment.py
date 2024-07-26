"""Stratifying an experiment
You are working with a government organization that wants to undertake an experiment around how some particular government policies impact the net wealth of individuals in a number of areas.

They have approached you to help set up the experimental design. They have warned you that there is likely to be a small group of users who already have high net wealth and are concerned that this group might overshadow any experimental outcome observed. You know just what to do!

Use your knowledge of experimental design to undertake block randomization, stratifying by the high_wealth column in the provided wealth_data DataFrame. There are 2000 rows in the DataFrame with 200 high net wealth subjects (high_wealth is 1).

Instructions 1/3
35 XP
1
2
3
Create the first block which contains all the high_wealth subjects and set the Block column to 1.
Create two groups from this block randomly assigning the high_wealth subjects to the Treatment (T) or control (C) group."""

# 1
# Create the first block
strata_1 = wealth_data[wealth_data["high_wealth"] == 1]
strata_1["Block"] = 1

# Create two groups assigning to Treatment or Control
strata_1_g1 = strata_1.sample(n=len(strata_1) // 2, replace=False)
strata_1_g1["T_C"] = "T"  # Assign Treatment group
strata_1_g2 = strata_1.drop(strata_1_g1.index)
strata_1_g2["T_C"] = "C"  # Assign Control group

# 2
# Create the first block
strata_1 = wealth_data[wealth_data["high_wealth"] == 1]
strata_1["Block"] = 1

# Create two groups assigning to Treatment or Control
strata_1_g1 = strata_1.sample(n=100, replace=False)
strata_1_g1["T_C"] = "T"
strata_1_g2 = strata_1.drop(strata_1_g1.index)
strata_1_g2["T_C"] = "C"

# Create the second block and assign groups
strata_2 = wealth_data[wealth_data["high_wealth"] == 0]
strata_2["Block"] = 2
strata_2_g1 = strata_2.sample(
    n=len(strata_2) // 2, replace=False
)  # Randomly select half
strata_2_g1["T_C"] = "T"  # Treatment group
strata_2_g2 = strata_2.drop(strata_2_g1.index)
strata_2_g2["T_C"] = "C"  # Control group


# 3
# Create the first block
strata_1 = wealth_data[wealth_data["high_wealth"] == 1]
strata_1["Block"] = 1

# Create two groups assigning to Treatment or Control
strata_1_g1 = strata_1.sample(100, replace=False)
strata_1_g1["T_C"] = "T"
strata_1_g2 = strata_1.drop(strata_1_g1.index)
strata_1_g2["T_C"] = "C"

# Create the second block and assign groups
strata_2 = wealth_data[wealth_data["high_wealth"] == 0]
strata_2["Block"] = 2

strata_2_g1 = strata_2.sample(900, replace=False)
strata_2_g1["T_C"] = "T"
strata_2_g2 = strata_2.drop(strata_2_g1.index)
strata_2_g2["T_C"] = "C"

# Concatenate the grouping work
wealth_data_stratified = pd.concat([strata_1_g1, strata_1_g2, strata_2_g1, strata_2_g2])
print(wealth_data_stratified.groupby(["Block", "T_C", "high_wealth"]).size())
