# Assign squirrels_madison as the value to the 'Madison Square Park' key
squirrels_by_park["Madison Square Park"] = squirrels_madison

# Update squirrels_by_park with the squirrels_union tuple
squirrels_by_park.update([squirrels_union])

# Loop over the park_name in the squirrels_by_park dictionary
for park_name in squirrels_by_park:
    # Safely print a list of the primary_fur_color for each squirrel in park_name
    print(
        park_name,
        [
            squirrel.get("primary_fur_color", "N/A")
            for squirrel in squirrels_by_park[park_name]
        ],
    )
