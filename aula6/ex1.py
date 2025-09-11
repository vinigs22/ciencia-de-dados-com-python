import numpy as np
import pandas as pd

# === Q1 ===
share_year1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
share_year2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

# === Q2 ===
total_share_year1 = share_year1.values.sum()
total_share_year2 = share_year2.values.sum()

print(f"Total market share in year 1: {total_share_year1:.2f}%")
print(f"Total market share in year 2: {total_share_year2:.2f}%")

# === Q3 ===
variation = share_year1 - share_year2
print("Variation between years:\n", variation)

# === Q4 ===
growth = variation[variation < 0]
print("Languages that increased:\n", growth)

# === Q5 ===
projection_two_years = variation * 2
year4_estimate = share_year2 - projection_two_years

print("Highest market share in year 4 (estimated):")
print(year4_estimate.sort_values(ascending=False).head(1))

# === Q6 ===
np.random.seed(10)
matrix = pd.DataFrame(
    np.random.randint(1, 50, (5, 4)),
    index=list("ABCDE"),
    columns=list("WXYZ")
)

column_x = matrix["X"]
mean_under_30 = column_x[column_x < 30].mean()
print("Mean of values < 30 in X:", mean_under_30)

# === Q7 ===
mean_row_D = matrix.loc["D"].mean()
sum_row_E = matrix.iloc[-1].sum()
print("Mean of row D:", mean_row_D)
print("Sum of row E:", sum_row_E)

# === Q8 ===
subset = matrix.loc[["A", "C", "E"], ["X", "Y"]]
print("Subset:\n", subset)

sum_by_column = subset.sum()
print("Sum by column:\n", sum_by_column)

sum_by_row = subset.sum(axis=1)
print("Sum by row:\n", sum_by_row)
