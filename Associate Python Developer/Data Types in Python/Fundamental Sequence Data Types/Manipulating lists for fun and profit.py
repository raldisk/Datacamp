# Create a list containing the names: baby_names
baby_names = ["Ximena", "Aliza", "Ayden", "Calvin"]

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(["Rowen", "Sandeep"])

# Find the position of 'Rowen': position
position = baby_names.index("Rowen")

# Remove 'Rowen' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)
