"""Anxiety treatments ANOVA
Psychologists conducted a study to compare the effectiveness of three types of therapy on reducing anxiety levels: Cognitive Behavioral Therapy (CBT), Dialectical Behavior Therapy (DBT), and Acceptance and Commitment Therapy (ACT). Participants were randomly assigned to one of the three therapy groups, and their anxiety levels were measured before and after the therapy sessions. The psychologists have asked you to determine if there are any significant differences in the effectiveness of these therapies.

The therapy_outcomes DataFrame containing this experiment data has been loaded along with pandas as pd and from scipy.stats import f_oneway."""

# Instructions 1/ Create a pivot table to calculate the mean 'Anxiety_Reduction' value across groups of 'Therapy_Type' in this data.
# Pivot to view the mean anxiety reduction for each therapy
pivot_table = therapy_outcomes.pivot_table(
    values="Anxiety_Reduction", index="Therapy_Type", aggfunc="mean"
)
print(pivot_table)

# Instructions 2/3 Filter groups of therapy types and their 'Anxiety_Reduction' values by first creating a list of the three therapy types: 'CBT', 'DBT', and 'ACT'.
# Pivot to view the mean anxiety reduction for each therapy
pivot_table = therapy_outcomes.pivot_table(
    values="Anxiety_Reduction", index="Therapy_Type", aggfunc="mean"
)
print(pivot_table)

# Create groups to prepare the data for ANOVA
therapy_types = ["CBT", "DBT", "ACT"]
groups = [
    therapy_outcomes[therapy_outcomes["Therapy_Type"] == therapy]["Anxiety_Reduction"]
    for therapy in therapy_types
]

# Instructions 3/3 Perform a one-way ANOVA.
# Pivot to view the mean anxiety reduction for each therapy
pivot_table = therapy_outcomes.pivot_table(
    values="Anxiety_Reduction", index="Therapy_Type", aggfunc="mean"
)
print(pivot_table)

# Create groups to prepare the data for ANOVA
therapy_types = ["CBT", "DBT", "ACT"]
groups = [
    therapy_outcomes[therapy_outcomes["Therapy_Type"] == therapy]["Anxiety_Reduction"]
    for therapy in therapy_types
]

# Conduct ANOVA
f_stat, p_val = f_oneway(*groups)
print(p_val)
