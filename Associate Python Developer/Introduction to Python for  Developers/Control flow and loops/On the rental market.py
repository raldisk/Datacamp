# Check the number of beds
if num_beds < min_num_beds:
  print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot:
  print("Too small")

# Check the rent
elif rent > max_rent:
  print("Too expensive")

# If all conditions met
else:
  print("This looks promising!")
