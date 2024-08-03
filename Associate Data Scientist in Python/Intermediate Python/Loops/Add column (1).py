# Import cars data
import pandas as pd

cars = pd.read_csv("cars.csv", index_col=0)

# Code for loop that adds COUNTRY column
cars["COUNTRY"] = [country.upper() for country in cars["country"]]


# Print cars
print(cars)
