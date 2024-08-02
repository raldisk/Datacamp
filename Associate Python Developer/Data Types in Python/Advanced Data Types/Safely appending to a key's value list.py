# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: male_penguin_weights
male_penguin_weights = defaultdict(list)

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Use the species as the key, and append the body_mass to it
    male_penguin_weights[species].append(body_mass)

# Print the first 2 items of the ridership dictionary
print(list(male_penguin_weights.items())[:2])
