# Safely print 'Union Square Park' from the squirrels_by_park dictionary
print(squirrels_by_park.get("Union Square Park"))

# Safely print the type of 'Fort Tryon Park' from the squirrels_by_park dictionary
print(type(squirrels_by_park.get("Fort Tryon Park")))

# Safely print 'Central Park' from the squirrels_by_park dictionary or 'Not Found'
print(squirrels_by_park.get("Central Park", "Not Found"))
