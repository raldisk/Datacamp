"""Exploring customer satisfaction
Merging datasets is a crucial skill in data analysis, especially when dealing with related data from different sources. You're working on a project for a financial institution to understand the relationship between loan approval rates and customer satisfaction. Two separate studies have been conducted: one focusing on loan approval yield based on various factors, and another on customer satisfaction under different conditions. Your task is to analyze how approval yield correlates with customer satisfaction, considering another variable such as interest rates.

The loan_approval_yield and customer_satisfaction DataFrames, pandas as pd, numpy as np, seaborn as sns, and matplotlib.pyplot as plt have been loaded for you."""

# INSTRUCTIONS 1/3 Merge loan_approval_yield with customer_satisfaction.
# Merge the two datasets
merged_data = pd.merge(loan_approval_yield, customer_satisfaction, on="ApplicationID")

# INSTRUCTIONS 2/3 Create a scatter plot to compare 'SatisfactionQuality' versus 'ApprovalYield', coloring the points by 'InterestRate'.
# Merge the two datasets
merged_data = pd.merge(loan_approval_yield, customer_satisfaction, on="ApplicationID")

# Use Seaborn to create the scatter plot
sns.relplot(
    x="ApprovalYield",
    y="SatisfactionQuality",
    hue="InterestRate",
    kind="scatter",
    data=merged_data,
)
plt.title("Satisfaction Quality by Approval Yield and Interest Rate")
plt.show()

# INSTRUCTIONS 3/3
# There isn't a strong relationship between Customer Satisfaction and Approval Yield in this experimental data. The resulting scatterplot looks similar to white noise scattered all about even when including Interest Rate.
