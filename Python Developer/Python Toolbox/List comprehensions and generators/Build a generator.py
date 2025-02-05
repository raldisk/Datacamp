# Create a list of strings
lannister = ["cersei", "jaime", "tywin", "tyrion", "joffrey"]


# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)


# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)
