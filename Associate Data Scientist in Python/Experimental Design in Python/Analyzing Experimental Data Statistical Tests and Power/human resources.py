"""Choosing the right test: human resources
In human resources, it's essential to understand the relationships between different variables that might influence employee satisfaction or turnover. Consider a scenario where an HR department is interested in understanding the association between the department in which employees work and their participation in a new workplace wellness program. The HR team has compiled this data over the past two years and has asked you if there's any significant association between an employee's department and their enrolling in the wellness program.

The data is available in the hr_wellness DataFrame. pandas as pd, numpy as np, and the following functions have been loaded:

from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency"""

# Instructions 1/4 What type of hypothesis test should be performed in this scenario?
# Chi-square test of association


# Instructions 2/4 Create a contingency table comparing 'Department' and 'Wellness_Program_Status'.

# Create a contingency table
contingency_table = pd.crosstab(
    hr_wellness["Department"], hr_wellness["Wellness_Program_Status"]
)


# Instructions 3/4 Perform a chi-square test of association on the contingency table and print the p-value.

# Create a contingency table
contingency_table = pd.crosstab(
    hr_wellness["Department"], hr_wellness["Wellness_Program_Status"]
)

# Perform the chi-square test of association
chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)
print(p_val)

# Instructions 4/4 Assume a significance level of 0.05. Given the P-value, what is the appropriate conclusion?
# There's no significant association between department and enrollment in the wellness program, as the P-value is larger than 0.05.
