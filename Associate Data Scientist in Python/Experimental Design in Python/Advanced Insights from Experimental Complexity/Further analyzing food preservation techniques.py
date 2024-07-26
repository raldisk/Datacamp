"""Further analyzing food preservation techniques
In your role as a food scientist, you're exploring into the comparative effects of various food preservation methods on nutrient retention, utilizing a food_preservation dataset that includes measurements from freezing, canning, and drying methods. This dataset has been crafted to incorporate variations in shelf life that depend on the nutrient retention values, reflecting real-world scenarios where preservation efficacy varies significantly. Your analysis will involve visually exploring these differences using advanced plotting techniques and nonparametric tests.

The following imports have been loaded for you in addition to food_preservation:

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kruskal"""

# INSTRUCTIONS 1/2 Create a boxen plot to explore the distribution of nutrient retention across the three different preservation methods.

# Create a boxen plot for nutrient retention by preservation method
sns.boxenplot(data=food_preservation, x="PreservationMethod", y="NutrientRetention")
plt.show()

# INSTRUCTIONS 2/2 Separate nutrient retention for each preservation method. Perform a Kruskal-Wallis test to compare nutrient retention across all preservation methods.
# Create a boxen plot for nutrient retention by preservation method
sns.boxenplot(data=food_preservation, x="PreservationMethod", y="NutrientRetention")
plt.show()

# Separate nutrient retention for each preservation method
freezing = food_preservation[food_preservation["PreservationMethod"] == "Freezing"][
    "NutrientRetention"
]
canning = food_preservation[food_preservation["PreservationMethod"] == "Canning"][
    "NutrientRetention"
]
drying = food_preservation[food_preservation["PreservationMethod"] == "Drying"][
    "NutrientRetention"
]


# Perform Kruskal-Wallis test
k_stat, k_pval = kruskal(freezing, canning, drying)
print("Kruskal-Wallis test p-value:", k_pval)
