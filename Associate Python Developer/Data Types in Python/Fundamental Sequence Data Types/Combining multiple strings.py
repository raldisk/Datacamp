# The top ten boy names are: as preamble
preamble = "The top ten boy names are: "

# , and as conjunction
conjunction = ", and"

# Combines the first 9 names in boy_names with a comma and space as first_nine_names
first_nine_names = ", ".join(boy_names[0:9])

# Print f-string preamble, first_nine_names, conjunction, the final item in boy_names and a period
print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.")
