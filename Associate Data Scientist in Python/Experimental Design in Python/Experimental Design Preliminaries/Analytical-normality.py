"""Analytical normality in an agricultural experiment
Carrying on from your previous work, your visual inspections of the data indicate it may not be a normal dataset overall, but that the initial time point may be.

Build on your previous work by using analytical methods to determine the normality of the dataset.

The DataFrame chicken_data has been read in for you, and the following package imports have been run already:

import pandas as pd
from scipy.stats import shapiro
from scipy.stats import anderson"""

# Instruction 1/4 Run a Shapiro-Wilk test of normality on the 'weight' column and print the test statistic and p-value.
from scipy.stats import shapiro

# Run a Shapiro-Wilk normality test on the weight column
test_statistic, p_value = shapiro(chicken_data["weight"])

print(f"p: {round(p_value, 4)} test stat: {round(test_statistic, 4)}")

# Instruction 2/4
# At a significance level of 0.05, does the Shapiro-Wilk test indicate the data is normally distributed?
# NO

# Instruction 3/4 Run an Anderson-Darling test for normality and print out the test statistic, significance levels, and critical values from the returned object.
from scipy.stats import anderson

# Run the Anderson-Darling test
result = anderson(chicken_data["weight"], dist="norm")

print(f"Test statistic: {round(result.statistic, 4)}")
print(f"Significance Levels: {result.significance_level}")
print(f"Critical Values: {result.critical_values}")

# Instruction 4/4
# Given the returned Anderson-Darling test result, what could you conclude at the 5% significance level?
# The data does not come from a Normal distribution.
