# 1/4
# Iterate over pit_df and print each row
for i, row in pit_df.iterrows():
    print(row)

# 2/4
# Iterate over pit_df and print each index variable, row, and row type
for i, row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))


# 3/4
# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)


# 4/4
# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))
