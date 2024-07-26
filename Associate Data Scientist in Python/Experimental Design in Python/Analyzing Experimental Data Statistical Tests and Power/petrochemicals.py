"""Choosing the right test: petrochemicals
In a chemistry research lab, scientists are examining the efficiency of three well-known catalysts—Palladium (Pd), Platinum (Pt), and Nickel (Ni)—in facilitating a particular reaction. Each catalyst is used in a set of identical reactions under controlled conditions, and the time taken for each reaction to reach completion is meticulously recorded. Your goal is to compare the mean reaction times across the three catalyst groups to identify which catalyst, if any, has a significantly different reaction time.

The data is available in the chemical_reactions DataFrame. pandas as pd, numpy as np, and the following functions have been loaded as well:

from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency"""

# Instructions 1/4
# One-way ANOVA
# Instructions 2/4 Use a list comprehension to filter into groups iterating over the catalyst_types and each of their 'Reaction_Time's.
catalyst_types = ["Palladium", "Platinum", "Nickel"]

# Collect reaction times for each catalyst into a list
groups = [
    chemical_reactions[chemical_reactions["Catalyst"] == catalyst]["Reaction_Time"]
    for catalyst in catalyst_types
]

# Instructions 3/4 Run a one-way ANOVA on the three groups to compare their mean reaction times and print the p-value.
catalyst_types = ["Palladium", "Platinum", "Nickel"]

# Collect reaction times for each catalyst into a list
groups = [
    chemical_reactions[chemical_reactions["Catalyst"] == catalyst]["Reaction_Time"]
    for catalyst in catalyst_types
]

# Perform the one-way ANOVA across the three groups
f_stat, p_val = f_oneway(*groups)
print(p_val)


# Instructions 4/4
# The P-value is substantially smaller than the value, indicating a significant difference in reaction times across the catalysts.
