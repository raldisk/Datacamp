# Use a for loop to iterate over the squirrels in Tompkins Square Park:
for squirrel in squirrels_by_park["Tompkins Square Park"]:
    # Safely print the activities of each squirrel or None
    print(squirrel.get("activities"))

# Print the list of 'Cinnamon' primary_fur_color squirrels in Union Square Park
print(
    [
        squirrel
        for squirrel in squirrels_by_park["Union Square Park"]
        if "Cinnamon" in squirrel["primary_fur_color"]
    ]
)
