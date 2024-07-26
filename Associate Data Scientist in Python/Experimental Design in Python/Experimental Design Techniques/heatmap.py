"""Heatmap of campaign interactions
Visualizing data can often reveal patterns that are not immediately obvious. In the context of marketing, understanding how different factors interact and affect the success of a campaign is vital. By creating a heatmap of conversions based on messaging style and time of day, you can quickly identify which combinations perform best and which ones need reevaluation. This visual tool is invaluable for marketing teams looking to optimize their strategies for maximum impact.

The data from the previous exercise has been loaded for you as marketing_pivot, seaborn is loaded as sns, and matplotlib.pyplot as plt."""

# Instructions 1/2
# Visualize interactions between Messaging_Style and Time_of_Day with respect to conversions by creating an annotated cool-warm heatmap of marketing_pivot.

import matplotlib.pyplot as plt
import seaborn as sns

# Visualize interactions with a heatmap
sns.heatmap(
    marketing_pivot, cmap="coolwarm", annot=True, fmt=".1f"
)  # using fmt to format numbers

plt.title("Heatmap of Conversions by Messaging Style and Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Messaging Style")
plt.show()
