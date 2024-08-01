# 1/2
# Print mean weekly_sales by department and type; fill missing values with 0
import numpy as np

print(
    sales.pivot_table(
        values="weekly_sales",
        index="department",
        columns="type",
        aggfunc=np.mean,
        fill_value=0,
    )
)

# 2/2
# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(
    sales.pivot_table(
        values="weekly_sales",
        index="department",
        columns="type",
        fill_value=0,
        margins=True,
    )
)
