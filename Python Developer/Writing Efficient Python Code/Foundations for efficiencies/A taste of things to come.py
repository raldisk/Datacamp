# 1/2
# Print the list created using the Non-Pythonic approach
i = 0
new_list = []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# 2/2
# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# 3/3
# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)
