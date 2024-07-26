"""Visualizing and testing preservation methods
As a food scientist, you're tasked with evaluating the effectiveness of different preservation methods on nutrient retention and how these methods impact shelf life. You have been provided with a dataset, food_preservation, that includes various types of food preserved by methods such as freezing and canning. Each entry in the dataset captures the nutrient retention and calculated shelf life for these foods, providing a unique opportunity to analyze the impacts of preservation techniques on food quality.

The following imports have been loaded for you in addition to food_preservation:

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu"""

# INSTRUCTIONS 1/2 Filter the DataFrame to include only Freezing and Canning rows. Create a violin plot to visualize the distribution of nutrient retention for different preservation methods.

# Filter to Freezing and Canning data
condensed_food_data = food_preservation[
    food_preservation["PreservationMethod"].isin(["Freezing", "Canning"])
]

# Create a violin plot for nutrient retention by preservation method
sns.violinplot(data=condensed_food_data, x="PreservationMethod", y="NutrientRetention")
plt.show()

# INSTRUCTIONS 2/2 Extract the nutrient retention values for both Freezing and Canning entries. Perform a Mann Whitney U test to compare nutrient retention between Freezing and Canning methods.

# Filter to Freezing and Canning data
condensed_food_data = food_preservation[
    food_preservation["PreservationMethod"].isin(["Freezing", "Canning"])
]

# Create a violin plot for nutrient retention by preservation method
sns.violinplot(data=condensed_food_data, x="PreservationMethod", y="NutrientRetention")
plt.show()

# Separate nutrient retention for Freezing and Canning methods
freezing = food_preservation[food_preservation["PreservationMethod"] == "Freezing"][
    "NutrientRetention"
]
canning = food_preservation[food_preservation["PreservationMethod"] == "Canning"][
    "NutrientRetention"
]

# Perform Mann Whitney U test
u_stat, p_val = mannwhitneyu(freezing, canning)

# Print the p-value
print("Mann Whitney U test p-value:", p_val)
