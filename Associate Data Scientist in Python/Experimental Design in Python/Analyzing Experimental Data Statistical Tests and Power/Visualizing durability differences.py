"""Visualizing durability differences
Following the analysis of toy durability, the research team is interested in you visualizing the distribution of durability scores for both Educational and Recreational toys. Such visualizations can offer intuitive insights into the data, potentially highlighting the range and variability of scores within each category. This step is essential for presenting findings to non-technical stakeholders and guiding further product development decisions.

The data is available in the toy_durability DataFrame, and seaborn and matplotlib.pyplot as sns and plt respectively are loaded."""

# INSTRUCTIONS: Visualize the distribution of 'Durability_Score' for Educational and Recreational toys using a Kernel Density Estimate (KDE) plot, highlighting differences by using the 'Toy_Type' column to color the distributions differently.

# Visualize the distribution of Durability_Score for each Toy_Type
sns.displot(data=toy_durability, x="Durability_Score", hue="Toy_Type", kind="kde")
plt.title("Durability Score Distribution by Toy Type")
plt.xlabel("Durability Score")
plt.ylabel("Density")
plt.show()
