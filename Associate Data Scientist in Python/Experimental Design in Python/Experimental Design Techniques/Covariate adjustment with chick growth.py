"""Covariate adjustment with chick growth
Imagine studying in agricultural science the growth patterns of chicks under various dietary regimens. The data from this study sheds light on the intricate relationship between their respective diets and the consequent impact on their weight. This data includes weight measurements of chicks at different ages, allowing for an exploration of covariate adjustment. age serves as a covariate, potentially influencing the outcome variable: the weight of the chicks.

DataFrames exp_chick_data, the experimental data, and cov_chick_data, the covariate data, have been loaded, along with the following libraries:

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt"""

# Instructions 1/3 Join the experimental and covariate data based on common column(s), and print this merged data.

# Join experimental and covariate data
merged_chick_data = pd.merge(exp_chick_data, cov_chick_data, on="Chick")

# Print the merged data
print(merged_chick_data)

# Instructions 2/3 Produce an ANCOVA predicting 'weight' based on 'Diet' and 'Time'.Print a summary of the ANCOVA mode

# Join experimental and covariate data
merged_chick_data = pd.merge(exp_chick_data, cov_chick_data, on="Chick")

# Perform ANCOVA with Diet and Time as predictors
model = ols("weight ~ Diet + Time", data=merged_chick_data).fit()

# Print a summary of the model
print(model.summary())

# Instructions 3 Design an lmplot to see hue='Diet' effects on y='weight' adjusted for x='Time'.

# Join experimental and covariate data
merged_chick_data = pd.merge(exp_chick_data, cov_chick_data, on="Chick")

# Perform ANCOVA with Diet and Time as predictors
model = ols("weight ~ Diet + Time", data=merged_chick_data).fit()

# Print a summary of the model
print(model.summary())

# Visualize Diet effects with Time adjustment
sns.lmplot(x="Time", y="weight", hue="Diet", data=merged_chick_data)
plt.show()
