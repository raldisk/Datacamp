"""Check for heteroscedasticity in shelf life
When examining food preservation methods, it's crucial to understand how the variance of one variable, such as shelf life, might change across the range of another variable like nutrient retention. Identifying such patterns, known as heteroscedasticity, can provide insights into the consistency of preservation effects. The food_preservation dataset encapsulates the outcomes of various preservation methods on different food types, specifically highlighting the balance between nutrient retention and resultant shelf life.

The food_preservation DataFrame, pandas as pd, numpy as np, seaborn as sns, and matplotlib.pyplot as plt have been loaded for you."""

# INSTRUCTIONS Use an appropriate plot to check for heteroscedasticity between 'NutrientRetention' and 'ShelfLife'.

# Check for heteroscedasticity with a residual plot
sns.residplot(x="NutrientRetention", y="ShelfLife", data=food_preservation, lowess=True)
plt.title("Residual Plot of Shelf Life and Nutrient Retention")
plt.xlabel("Nutrient Retention (%)")
plt.ylabel("Residuals")
plt.show()
