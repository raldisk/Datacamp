"""Applying Tukey's HSD
Following the ANOVA analysis which suggested significant differences in the effectiveness of the three types of therapy, the psychologists are keen to delve deeper. They wish for you to explain exactly which therapy types differ from each other in terms of reducing anxiety levels. This is where Tukey's Honest Significant Difference (HSD) test comes into play. It's a post-hoc test used to make pairwise comparisons between group means after an ANOVA has shown a significant difference. Tukey's HSD test helps in identifying specific pairs of groups that have significant differences in their means.

The therapy_outcomes DataFrame containing this experiment data has again been loaded along with pandas as pd and from statsmodels.stats.multicomp import pairwise_tukeyhsd."""

# At a significance level of 0.05, perform Tukey's HSD test to compare the mean anxiety reduction across the three therapy groups.

# Perform Tukey's HSD test
tukey_results = pairwise_tukeyhsd(
    therapy_outcomes["Anxiety_Reduction"], therapy_outcomes["Therapy_Type"], alpha=0.05
)

print(tukey_results)
