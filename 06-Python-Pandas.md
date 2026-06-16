# Python Pandas for ML/AI Engineers

This module transitions from plain Python loops to table-native data operations with Pandas.

**Learning path:** This is step 6 in [00-START-HERE.md](00-START-HERE.md). Previous: [05-Portfolio-US-Medical-Insurance.md](05-Portfolio-US-Medical-Insurance.md). Next: [07-Exploratory-Data-Analysis.md](07-Exploratory-Data-Analysis.md).

---

## Codecademy subsections (exact order)

### 1) Introduction to Python Pandas for ML/AI Engineering

**Big ideas:**
- Pandas introduces two core structures: **Series** (1-D labelled array) and **DataFrame** (2-D table with labelled rows and columns).
- A DataFrame is conceptually a dict of Series — each column is a Series sharing the same index.
- Pandas replaces manual loops over lists with vectorised operations that are faster and far more readable.

**What changed from plain Python:**
```python
import pandas as pd

# Plain Python: average of a list
charges = [1200.50, 4500.00, 800.75]
avg = sum(charges) / len(charges)

# Pandas: one method call
df = pd.read_csv("data/insurance.csv")
avg = df["charges"].mean()
```

**Essential first steps with any new DataFrame:**
```python
df = pd.read_csv("data/insurance.csv")

df.shape          # (rows, cols)
df.dtypes         # column types
df.head()         # first 5 rows
df.tail()         # last 5 rows
df.info()         # non-null counts + dtypes
df.describe()     # stats for numeric columns
df.columns        # column names as Index
df.isnull().sum() # missing value counts
```

---

### 2) Lambda Functions for Pandas

**Useful lambda patterns:**
- A **lambda** is an anonymous one-line function: `lambda arguments: expression`.
- Used heavily with `.apply()` to transform a column row-by-row.

```python
# Categorise BMI
df["bmi_category"] = df["bmi"].apply(lambda x:
    "Underweight" if x < 18.5 else
    "Healthy"     if x < 25   else
    "Overweight"  if x < 30   else
    "Obese"
)

# Convert age to decade
df["decade"] = df["age"].apply(lambda x: (x // 10) * 10)

# Apply to multiple columns at once
df["age_bmi"] = df.apply(lambda row: row["age"] * row["bmi"], axis=1)
```

**When not to use lambda:**
- When the logic is more than one expression — write a named function instead (more readable, easier to test).
- For arithmetic on whole columns, vectorised operators are faster: `df["charges"] * 1.1` beats `.apply(lambda x: x * 1.1)`.

---

### 3) Hands-On with Pandas

**DataFrame operations practiced:**

```python
# Select a single column (returns Series)
ages = df["age"]

# Select multiple columns (returns DataFrame)
subset = df[["age", "charges", "smoker"]]

# Filter rows by condition
smokers = df[df["smoker"] == "yes"]
high_bmi = df[df["bmi"] > 30]

# Combine conditions  (use & | ~ not and or not)
smoker_high_bmi = df[(df["smoker"] == "yes") & (df["bmi"] > 30)]

# Add a new column
df["charge_per_year"] = df["charges"] / df["age"]

# Rename columns
df = df.rename(columns={"bmi": "body_mass_index"})

# Drop a column
df = df.drop(columns=["charge_per_year"])

# Sort
df_sorted = df.sort_values("charges", ascending=False)

# Reset index after filtering
smokers = smokers.reset_index(drop=True)
```

**My most useful snippets:**
```python
# Value counts for a categorical column
df["region"].value_counts()

# Unique values
df["smoker"].unique()        # array(['yes', 'no'])
df["smoker"].nunique()       # 2

# Conditional update with np.where
import numpy as np
df["is_smoker"] = np.where(df["smoker"] == "yes", 1, 0)
```

---

### 4) Aggregates in Pandas

**Grouping logic:**
```python
# Group by one column, compute one aggregate
avg_by_region = df.groupby("region")["charges"].mean()

# Group by multiple columns
avg_by_region_smoker = (
    df.groupby(["region", "smoker"])["charges"]
    .mean()
    .reset_index()
)

# Multiple aggregates at once
stats = df.groupby("region")["charges"].agg(["mean", "median", "std", "count"])
```

**Aggregate functions and interpretation:**

| Function | What it tells you |
|---|---|
| `.mean()` | Average; sensitive to outliers |
| `.median()` | Middle value; robust to outliers |
| `.std()` | Spread around the mean |
| `.min()` / `.max()` | Range boundaries |
| `.count()` | Non-null row count per group |
| `.sum()` | Total; useful for counts/amounts |
| `.nunique()` | Number of distinct values |

**Pivot tables:**
```python
pivot = df.pivot_table(
    values="charges",
    index="region",
    columns="smoker",
    aggfunc="mean"
)
```

---

### 5) Multiple Tables in Pandas

**Merge/join patterns:**
```python
# Inner join — keep only rows that match in both tables
merged = pd.merge(df_left, df_right, on="patient_id", how="inner")

# Left join — keep all rows from df_left, NaN where no match on right
merged = pd.merge(df_left, df_right, on="patient_id", how="left")

# Merge on columns with different names
merged = pd.merge(df_left, df_right,
                  left_on="id", right_on="patient_id", how="inner")

# Concatenate rows from two DataFrames with the same columns
combined = pd.concat([df_2022, df_2023], ignore_index=True)
```

**Join keys and data-quality checks:**
- Before merging, check for duplicate keys: `df["patient_id"].duplicated().sum()`.
- Check for NaN keys: `df["patient_id"].isnull().sum()` — NaN keys never match.
- After a left join, the number of NaN values in the right-side columns reveals unmatched rows.
- `how="outer"` keeps all rows from both sides; useful for spotting what's missing from either.

---

### 6) Data Manipulation Challenge Project

**Project goal:** Apply all Pandas skills above to a multi-table dataset; produce a clean summary DataFrame ready for modelling.

**Steps I took:**
1. Loaded two CSVs and inspected shape, dtypes, and null counts.
2. Cleaned types: cast string columns to the correct dtype, standardised category labels.
3. Merged tables on the shared key; verified row counts before and after.
4. Computed grouped aggregates (mean, count, std) per category.
5. Filtered to the relevant subset and reset the index.
6. Exported the clean DataFrame: `df_clean.to_csv("output/clean.csv", index=False)`.

**Final result and reflection:**
- The hardest part was ensuring the merge key had no duplicates or NaN values.
- Using `.agg()` with a dict of functions is much neater than chaining multiple `.mean()` calls.
- Key habit: always check `df.shape` *before and after* every filter or merge.

---

## See also

- Previous: [05-Portfolio-US-Medical-Insurance.md](05-Portfolio-US-Medical-Insurance.md)
- Next: [07-Exploratory-Data-Analysis.md](07-Exploratory-Data-Analysis.md)
