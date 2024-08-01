# Import cars data
import pandas as pd

cars = pd.read_csv("cars.csv", index_col=0)

# Import numpy, you'll need this

# Create medium: observations with cars_per_cap between 100 and 500

medium = cars[(cars["cars_per_cap"] >= 100) & (cars["cars_per_cap"] <= 500)]


# Print medium
print(medium)
