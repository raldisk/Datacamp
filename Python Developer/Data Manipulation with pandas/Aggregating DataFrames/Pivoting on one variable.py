# 1/3
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# 2/3
# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(
    values="weekly_sales", index="type", aggfunc=[np.mean, np.median]
)

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# 3/3

# Pivot for mean weekly_sales by store type and holiday
import numpy as np

mean_sales_by_type_holiday = sales.pivot_table(
    values="weekly_sales", index="type", columns="is_holiday", aggfunc=np.mean
)
