"""Understanding marketing campaign effectiveness
Imagine you're a digital marketer analyzing data from a recent campaign to understand what messaging style and time of day yield the highest conversions. This analysis is crucial for guiding future marketing strategies, ensuring that your messages reach potential customers when they're most likely to engage. In this exercise, you're working with a dataset giving the outcomes of different messaging styles ('Casual' versus 'Formal') and times of day ('Morning' versus 'Evening') on conversion rates, a common scenario in marketing data analysis.

The data has been loaded for you as a DataFrame named marketing_data, and pandas is loaded as pd."""

# Instructions

"""Create a pivot table with 'Messaging_Style' as the index and 'Time_of_Day' as the columns, computing the mean of Conversions.
Print this pivot table."""


# Create a pivot table for marketing campaign data
marketing_pivot = marketing_data.pivot_table(
    values="Conversions", index="Messaging_Style", columns="Time_of_Day", aggfunc="mean"
)

# View the pivoted results
print(marketing_pivot)
