# Iterate over the first twenty entries in labeled_entries
for entry in labeled_entries[:20]:
    # if the entry's species equals Chinstrap
    if entry.species == "Chinstrap":
        # Print each entry's sex and body_mass seperated by a colon
        print(f"{entry.sex}:{entry.body_mass}")
