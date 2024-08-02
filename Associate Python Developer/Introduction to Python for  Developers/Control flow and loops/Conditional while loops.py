release_date = 26
current_date = 19

# Create a condition where current_date is less than or equal to the release_date
while current_date <= release_date:
    # Increment current_date by one
    current_date += 1

    # Promote purchases
    if current_date < 21:
        print("Purchase before the 21st for early access")

    # Check if the date is less than or equal to the 25th
    elif current_date <= 25:
        print("Coming soon!")
    else:
        print("Available now!")
