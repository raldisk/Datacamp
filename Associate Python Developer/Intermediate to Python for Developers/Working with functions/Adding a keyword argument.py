# 1/2
# Define clean_text
def clean_text(text, lower=True):
    if lower == False:
        clean_text = text.replace(" ", "_")
        return clean_text
    else:
        clean_text = text.replace(" ", "_")
        clean_text = clean_text.lower()
        return clean_text


# 2/2
# Define clean_text
def clean_text(text, remove=None):
    if remove != None:
        clean_text = text.replace(remove, "")
        clean_text = clean_text.lower()
        return clean_text
    else:
        clean_text = text.lower()
        return clean_text
