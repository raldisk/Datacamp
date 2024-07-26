"""Analyzing toy durability
In product development within the toy industry, it's crucial to understand the durability of toys, particularly when comparing educational toys to recreational ones. Durability can significantly impact customer satisfaction and repeat business. Researchers in a toy manufacturing company have asked you to conduct the analysis of a study comparing the durability of educational toys versus recreational toys. The toy_durability DataFrame contains the results of these tests, with durability scores assigned based on rigorous testing protocols.

The data is available in the toy_durability DataFrame. pandas as pd and from scipy.stats import ttest_ind have been loaded."""

# INSTRUCTIONS Calculate the mean 'Durability_Score' for both 'Educational' and 'Recreational' toys using a pivot table. Perform an independent samples t-test to compare the durability of 'Educational' and 'Recreational' toys by first separating durability scores by Toy_Type.

# Calculate mean Durability_Score for each Toy_Type
mean_durability = toy_durability.pivot_table(
    values="Durability_Score", index="Toy_Type", aggfunc=np.mean
)
print(mean_durability)

# Perform t-test
educational_durability = toy_durability[toy_durability["Toy_Type"] == "Educational"][
    "Durability_Score"
]
recreational_durability = toy_durability[toy_durability["Toy_Type"] == "Recreational"][
    "Durability_Score"
]
t_stat, p_val = ttest_ind(educational_durability, recreational_durability)

print(p_val)
