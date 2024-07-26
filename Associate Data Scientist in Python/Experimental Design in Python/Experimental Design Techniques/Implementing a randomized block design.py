"""Implementing a randomized block design
The manufacturing firm you worked with earlier is still interested in conducting some experiments on worker productivity. Previously, the two blocks were set randomly. While this can work, it can be better to group subjects based on similar characteristics.

The same employees are again loaded but this time in a DataFrame called productivity including 1200 other colleagues. It also includes a worker 'productivity_score' column based on units produced per hour. This column was binned into three groups to generate blocks based on similar productivity values. The firm would like to apply a new incentive program with three options ('Bonus', 'Profit Sharing' and 'Work from Home') throughout the firm with treatment applied randomly.

numpy and pandas as np and pd respectively are loaded."""

"""Instructions
100 XP
Shuffle the blocks to create a new DataFrame called prod_df.
Reset the index so that block is not both an index and a column.
Randomly assign the three treatment values in the 'Treatment' column."""


# Randomly assign workers to blocks
prod_df = productivity.groupby('block').apply(
  lambda x: x.sample(frac=1)
)

# Reset the index
prod_df = prod_df.reset_index(drop=True)

# Assign treatment randomly
prod_df['Treatment'] = np.random.choice(
  ['Bonus', 'Profit Sharing', 'Work from Home'],
  size=len(prod_df)
)
