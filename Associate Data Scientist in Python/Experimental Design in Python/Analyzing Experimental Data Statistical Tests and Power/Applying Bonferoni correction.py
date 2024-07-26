"""Applying Bonferoni correction
After identifying significant differences between therapy groups with Tukey's HSD, we want to confirm our findings with the Bonferroni correction. The Bonferroni correction is a conservative statistical adjustment used to counteract the problem of multiple comparisons. It reduces the chance of obtaining false-positive results by adjusting the significance level. In the context of your study on the effectiveness of CBT, DBT, and ACT, applying the Bonferroni correction will help ensure that the significant differences you observe between therapy groups are not due to chance.

The therapy_outcomes DataFrame has again been loaded along with pandas as pd, from scipy.stats import ttest_ind, and from statsmodels.sandbox.stats.multicomp import multipletests."""

# INSTRUCTIONS Create a list of P-values from independent t-tests between all pairs of therapy groups. Apply the Bonferroni correction to adjust the P-values and print them.
p_values = []

therapy_pairs = [("CBT", "DBT"), ("CBT", "ACT"), ("DBT", "ACT")]

# Conduct t-tests and collect P-values
for pair in therapy_pairs:
    group1 = therapy_outcomes[therapy_outcomes["Therapy_Type"] == pair[0]][
        "Anxiety_Reduction"
    ]
    group2 = therapy_outcomes[therapy_outcomes["Therapy_Type"] == pair[1]][
        "Anxiety_Reduction"
    ]
    t_stat, p_val = ttest_ind(group1, group2)
    p_values.append(p_val)

# Apply Bonferroni correction
print(multipletests(p_values, alpha=0.05, method="bonferroni")[1])
