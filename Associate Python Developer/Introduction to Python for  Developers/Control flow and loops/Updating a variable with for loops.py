# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for tickets in range(1, max_capacity + 1):
    # Add one to tickets_sold in each iteration
    tickets_sold += 1

print("Sold out:", tickets_sold, "tickets sold!")
