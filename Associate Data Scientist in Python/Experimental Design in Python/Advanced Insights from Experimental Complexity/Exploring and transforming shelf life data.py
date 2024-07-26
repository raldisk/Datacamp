"""Exercise
Exercise
Exploring and transforming shelf life data
Understanding the distribution of different variables in our data is a key aspect of any data work including experimental analysis. The food_preservation dataset captures various food preservation methods and their impact on nutrient retention and shelf life. A crucial aspect of this data involves the shelf life of preserved foods, which can vary significantly across different preservation methods and food types.

The food_preservation DataFrame, from scipy.stats import boxcox, pandas as pd, numpy as np, seaborn as sns, and matplotlib.pyplot as plt have been loaded for you."""

# INSTRUCTIONS 1/3 Visualize the original distribution of the 'ShelfLife' column.
# Visualize the original ShelfLife distribution
sns.displot(food_preservation["ShelfLife"])
plt.title("Original Shelf Life Distribution")
plt.show()

# INSTRUCTIONS 2/3 Apply a Box-Cox transformation to the 'ShelfLife' column.
# Visualize the original ShelfLife distribution
sns.displot(food_preservation["ShelfLife"])
plt.title("Original Shelf Life Distribution")
plt.show()

# Create a Box-Cox transformation
ShelfLifeTransformed, _ = boxcox(food_preservation["ShelfLife"])

# INSTRUCTIONS 3/3 Visualize the distribution of the 'ShelfLifeTransformed'.
# Visualize the original ShelfLife distribution
sns.displot(food_preservation["ShelfLife"])
plt.title("Original Shelf Life Distribution")
plt.show()

# Create a Box-Cox transformation
ShelfLifeTransformed, _ = boxcox(food_preservation["ShelfLife"])

# Visualize the transformed ShelfLife distribution
plt.clf()
sns.displot(ShelfLifeTransformed)
plt.title("Transformed Shelf Life Distribution")
plt.show()
