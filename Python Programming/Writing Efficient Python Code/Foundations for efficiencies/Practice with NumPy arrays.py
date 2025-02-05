# 1/2

## Practice with NumPy arrays

# Print second row of nums
print(nums[1, :])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:, 2] = nums[:, 2] + 1
print(nums)


# 2/2
# A numpy array contains homogeneous data types (which reduces memory consumption) and provides the ability to apply operations on all elements through broadcasting.
