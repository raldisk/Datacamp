def clean_string(text):
    # Add a single-line docstring
    """Clean text by swapping spaces to underscores and converting to lowercase."""

    no_spaces = text.replace(" ", "_")
    clean_text = no_spaces.lower()
    return clean_text


# Access the docstring
print(clean_string.__doc__)
