"""Choosing the right test: finance
In the realm of finance, investment strategists are continually evaluating different approaches to maximize returns. Consider a scenario where a financial firm wishes to assess the effectiveness of two investment strategies: "Quantitative Analysis" and "Fundamental Analysis". The firm has applied each strategy to a separate set of investment portfolios for a year and now asks you to compare the annual returns to determine if there is any difference in strategy returns by comparing the mean returns of the two groups.

The data is available in the investment_returns DataFrame. pandas as pd, numpy as np, and the following functions have been loaded as well:

from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency"""


# Instructions 1/4 What type of hypothesis test should be performed in this scenario?
# Independent samples t-test

# Instructions 2/4 Filter 'Strategy_Type' on 'Quantitative' to retrieve their 'Annual_Return' and do the same for 'Fundamental' strategies.
# Separate the annual returns by strategy type
quantitative_returns = investment_returns[
    investment_returns["Strategy_Type"] == "Quantitative"
]["Annual_Return"]
fundamental_returns = investment_returns[
    investment_returns["Strategy_Type"] == "Fundamental"
]["Annual_Return"]

# Instruction 3/4 Complete for the two groups an independent samples t-test and print the p-value.

# Separate the annual returns by strategy type
quantitative_returns = investment_returns[
    investment_returns["Strategy_Type"] == "Quantitative"
]["Annual_Return"]
fundamental_returns = investment_returns[
    investment_returns["Strategy_Type"] == "Fundamental"
]["Annual_Return"]

# Perform the independent samples t-test between the two groups
t_stat, p_val = ttest_ind(quantitative_returns, fundamental_returns)
print(p_val)

# Assume a significance level of 0.1. What is the appropriate conclusion to glean from the P-value in comparison with this value?
# The P-value is much smaller than, suggesting a significant difference in returns between the two strategies.
