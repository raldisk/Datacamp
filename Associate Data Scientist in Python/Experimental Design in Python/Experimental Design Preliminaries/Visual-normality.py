"""Visual normality in an agricultural experiment
You have been contracted by an agricultural firm conducting an experiment on 50 chickens, divided into four groups, each fed a different diet. Weight measurements were taken every second day for 20 days.

You'll analyze chicken_data to assess normality, which will determine the suitability of parametric statistical tests, beginning with a visual examination of the data distribution. The necessary packages for analysis have been imported for you:

import seaborn as sns
import pandas as pd
from statsmodels.graphics.gofplots import qqplot"""

# Instructions 1
"""Plot the distributions of the chickens' weight using the kernel density estimation method to visualize for normality."""

import matplotlib.pyplot as plt
import seaborn as sns

# Plot the distribution of the chickens' weight using displot
sns.displot(data=chicken_data, x="weight", kind="kde", fill=True)
plt.title("Kernel Density Estimation of Chickens' Weights")
plt.xlabel("Weight")
plt.ylabel("Density")
plt.show()

# Instructio 2
"""Create the qq plot of the chickens' weight to assess normality visually."""
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot

# Plot the QQ plot of the chickens' weight
qqplot(chicken_data["weight"], line="s")
plt.title("QQ Plot of Chickens' Weights")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.show()

# Instruction 3
"""Subset the DataFrame for 'Time' as 2 and repeat the KDE plot task to check if data at different time periods is normal."""
import matplotlib.pyplot as plt
import seaborn as sns

# Subset the data
subset_data = chicken_data[chicken_data["Time"] == 2]

# Repeat the plotting
sns.displot(data=subset_data, x="weight", kind="kde")
plt.title("KDE Plot of Chickens' Weights at Time = 2")
plt.xlabel("Weight")
plt.ylabel("Density")
plt.show()
