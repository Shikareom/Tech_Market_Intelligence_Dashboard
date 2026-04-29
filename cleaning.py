import pandas as pd

df = pd.read_csv("pune_jobs_raw.csv")

# Problem: One cell has "Python, SQL, AWS". Power BI sees this as ONE thing.
# Solution: We 'explode' the data so each skill gets its own row.

# 1. Split the string into a list
df['Skills'] = df['Skills'].str.split(', ')

# 2. Explode the list (Create a row for every skill)
df_clean = df.explode('Skills')

# 3. Save the 'Golden File' for Power BI
df_clean.to_csv("pune_jobs_cleaned.csv", index=False)
print("Step 2 Complete: Clean data ready for Power BI!")