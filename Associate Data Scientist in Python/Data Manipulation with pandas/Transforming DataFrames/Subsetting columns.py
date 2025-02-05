# 1/3
# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())


# 2/3
# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

# Print the head of the result
print(state_fam.head())

# 3/3
# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())
