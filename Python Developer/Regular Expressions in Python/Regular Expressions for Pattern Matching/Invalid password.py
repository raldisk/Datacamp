# Write a regex to check if the password is valid
regex = r"[A-Za-z0-9!#%&*\$\.]{8,20}"

for example in passwords:
    # Scan the strings to find a match
    if re.search(regex, example):
        # Complete the format method to print out the result
        print(
            "The password {pass_example} is a valid password".format(
                pass_example=example
            )
        )
    else:
        print("The password {pass_example} is invalid".format(pass_example=example))
