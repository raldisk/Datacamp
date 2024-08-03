# 1/3
# Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals")

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(
    ["region", "family_members"], ascending=[True, False]
)

print(homelessness_ind.head())


# 2/3
# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Print the top few rows
print(homelessness_fam.head())

# 3/3
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(
    ["region", "family_members"], ascending=[True, False]
)

# Print the top few rows
print(homelessness_reg_fam.head())
