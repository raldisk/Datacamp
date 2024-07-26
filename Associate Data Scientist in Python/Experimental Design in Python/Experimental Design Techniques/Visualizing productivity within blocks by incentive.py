"""Visualizing productivity within blocks by incentive
Continuing with the worker productivity example, you'll explore if the productivity scores are distributed throughout the data as one would expect with random assignment of treatment. Note that this is a precautionary step, and the treatment and follow-up results on the impact of the three treatments is not done yet!

seaborn and matplotlib.pyplot as sns and plt respectively are loaded."""

# Visualize the productivity scores within blocks by treatment using a boxplot with 'block' for x, 'productivity_score' for y, and 'Treatment' for hue.
# Make a plot showing how positivity_score varies within blocks
sns.boxplot(x="block", y="productivity_score", hue="Treatment", data=prod_df)

plt.show()
