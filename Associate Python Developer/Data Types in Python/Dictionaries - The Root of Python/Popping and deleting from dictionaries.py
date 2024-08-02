# Remove "Madison Square Park" from squirrels_by_park and store it
squirrels_madison = squirrels_by_park.pop("Madison Square Park")

# Safely remove "City Hall Park" from squirrels_by_park with an empty dictionary as the default
squirrels_city_hall = squirrels_by_park.pop("City Hall Park", {})

# Delete "Union Square Park" from squirrels_by_park
del squirrels_by_park["Union Square Park"]

# Print squirrels_by_park
print(squirrels_by_park)
