"""ANOVA within blocks of employees
Building on your previous analyses with the manufacturing firm, where worker productivity was examined across different blocks and an incentive program was introduced, you're now delving deeper into the data. The firm, equipped with a more comprehensive dataset in the productivity DataFrame, including 1200 additional employees and their productivity_score, has structured the workforce into three blocks based on productivity levels. Each employee has been randomly assigned one of three incentive options: 'Bonus', 'Profit Sharing', or 'Work from Home'.

Before assessing the full impact of these incentive treatments on productivity, it's crucial to verify that the initial treatment assignment was indeed random and equitable across the different productivity blocks. This step ensures that any observed differences in productivity post-treatment can be confidently attributed to the incentive programs themselves, rather than pre-existing disparities in the blocks.

The f_oneway() function from scipy.stats has been loaded for you."""

"""Instructions Group prod_df by the appropriate column that represents different blocks in your data.
Use a lambda function to apply the ANOVA test within each block, specifying the lambda function's argument.
For each treatment group within the blocks, filter prod_df based on the 'Treatment' column values and select the 'productivity_score' column."""

# Perform the within blocks ANOVA, first grouping by block
within_block_anova = prod_df.groupby("block").apply(
    # Set function
    lambda x: f_oneway(
        # Filter Treatment values based on outcome
        x[x["Treatment"] == "Bonus"]["productivity_score"],
        x[x["Treatment"] == "Profit Sharing"]["productivity_score"],
        x[x["Treatment"] == "Work from Home"]["productivity_score"],
    )
)
print(within_block_anova)
