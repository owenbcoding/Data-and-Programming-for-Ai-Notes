# Exploratory Data Analysis in Python

EDA is where you profile data quality, discover patterns, and decide what deserves deeper modelling.

**Learning path:** This is step 7 in [00-START-HERE.md](00-START-HERE.md). Previous: [06-Python-Pandas.md](06-Python-Pandas.md). Next: [08-Math-Statistics.md](08-Math-Statistics.md).

---

## Codecademy subsections (exact order)

> Course confirmed: **5 subsections** — Introduction to EDA · Variable Types · Inspect, Clean, and Validate a Dataset · Summarizing a Single Feature · Summarizing the Relationship between Two Features

### 1) Introduction to EDA
`1 Informational · 1 Article`

**What EDA is for:**
- Understand the data *before* fitting any model.
- Catch data quality problems early (missing values, wrong types, outliers).
- Identify which features might be informative for modelling.
- Generate hypotheses that are worth testing rigorously later.

**Questions to answer before modelling:**
1. How many rows and columns do I have?
2. What is the data type of each column?
3. How much data is missing, and where?
4. What is the distribution of each feature (shape, centre, spread)?
5. Are there obvious outliers or impossible values?
6. How do features relate to each other and to the target?
7. Are there class imbalances (for classification tasks)?

**EDA workflow:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/insurance.csv")
print(df.shape)          # (1338, 7)
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())
```

---

### 2) Variable Types
`1 Lesson · 1 Quiz · 1 Project`

**Numeric vs categorical:**

| Type | Subtype | Python dtype | Typical chart |
|---|---|---|---|
| Numeric | Continuous | `float64` | Histogram, KDE, box plot |
| Numeric | Discrete | `int64` | Bar chart, histogram |
| Categorical | Nominal | `object` | Bar chart, count plot |
| Categorical | Ordinal | `object` / `category` | Ordered bar chart |

**Type conversion decisions:**
```python
# Ordinal encoding — preserve order
from pandas.api.types import CategoricalDtype

edu_order = CategoricalDtype(
    categories=["high_school", "bachelor", "master", "phd"],
    ordered=True
)
df["education"] = df["education"].astype(edu_order)

# One-hot encode nominal categories for ML
df = pd.get_dummies(df, columns=["region", "sex"], drop_first=True)

# Cast to numeric (coerce makes invalid values NaN)
df["charges"] = pd.to_numeric(df["charges"], errors="coerce")
```

**Type-related pitfalls:**
- Pandas reads numeric-looking strings as `object` if the column has *any* non-numeric entry — always check with `df.dtypes`.
- Encoding ordinal variables as plain integers (1, 2, 3, 4) implies equal spacing; use `CategoricalDtype` to be explicit.
- `pd.get_dummies` with `drop_first=True` avoids the dummy variable trap (multicollinearity).

#### Quiz: Variable Types
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

---

### 3) Inspect, Clean, and Validate a Dataset
`1 Article · 1 Project`

**Missing values:**
```python
# Count and percentage
missing = df.isnull().sum()
missing_pct = (df.isnull().mean() * 100).round(2)
print(pd.concat([missing, missing_pct], axis=1,
                keys=["count", "pct"]))

# Drop rows where target is missing
df = df.dropna(subset=["charges"])

# Impute numeric with median (more robust than mean)
df["bmi"] = df["bmi"].fillna(df["bmi"].median())

# Impute categorical with mode
df["smoker"] = df["smoker"].fillna(df["smoker"].mode()[0])
```

**Outliers and invalid values:**
```python
# IQR method
Q1 = df["charges"].quantile(0.25)
Q3 = df["charges"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["charges"] < lower) | (df["charges"] > upper)]
print(f"{len(outliers)} outlier rows")

# Z-score method (flag values > 3 standard deviations from mean)
from scipy import stats
z_scores = stats.zscore(df["charges"])
df["charges_outlier"] = (abs(z_scores) > 3)
```

**Validation checks performed:**
```python
# Age must be between 18 and 100
assert df["age"].between(18, 100).all(), "Age out of range"

# BMI must be positive
assert (df["bmi"] > 0).all(), "Negative BMI found"

# Allowed categories
assert df["smoker"].isin(["yes", "no"]).all(), "Unexpected smoker value"
```

---

### 4) Summarizing a Single Feature
`1 Article · 1 Lesson · 1 Quiz · 1 Project`

**Distribution notes:**
- **Symmetric / normal:** mean ≈ median; histogram is bell-shaped.
- **Right-skewed (positive skew):** long tail on the right; mean > median (common in income/charges data).
- **Left-skewed (negative skew):** long tail on the left; mean < median.
- Skewed data often benefits from a log transform before modelling: `df["log_charges"] = np.log1p(df["charges"])`.

**Centre / spread takeaways:**

| Statistic | Use when |
|---|---|
| Mean | Symmetric distributions without extreme outliers |
| Median | Skewed distributions or data with outliers |
| Mode | Categorical data or discrete counts |
| Std dev | Symmetric distributions |
| IQR (Q3 − Q1) | Skewed distributions; robust spread measure |

**Visualisations used:**
```python
# Histogram + KDE
df["charges"].hist(bins=30, edgecolor="black")
plt.title("Distribution of Insurance Charges")
plt.xlabel("Charges (USD)")
plt.show()

# Box plot — shows median, IQR, and outliers
df.boxplot(column="charges")
plt.show()

# Seaborn displot (histogram + KDE together)
sns.displot(df, x="charges", kde=True, bins=30)
plt.show()
```

#### Quiz: Summarizing a Single Feature
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

---

### 5) Summarizing the Relationship between Two Features
`3 Lessons · 1 Quiz · 1 Project`

**Feature pairs analysed:**
- `charges` vs `smoker` (continuous vs categorical)
- `charges` vs `age` (continuous vs continuous)
- `region` vs `bmi` (categorical vs continuous)

**Relationship patterns observed:**
```python
# Categorical vs continuous — grouped box plots
sns.boxplot(data=df, x="smoker", y="charges")
plt.title("Charges by Smoking Status")
plt.show()

# Continuous vs continuous — scatter plot
sns.scatterplot(data=df, x="age", y="charges", hue="smoker", alpha=0.6)
plt.title("Age vs Charges (coloured by smoker status)")
plt.show()

# Correlation matrix
corr = df[["age", "bmi", "children", "charges"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()

# Pairplot — all numeric columns at once
sns.pairplot(df, hue="smoker", diag_kind="kde")
plt.show()
```

**Why this matters for modelling:**
- A strong correlation between a feature and the target (e.g. `smoker` and `charges`) suggests that feature will be useful in a model.
- Correlations *between features* (multicollinearity) can destabilise linear models — check the heatmap.
- EDA findings determine which features to include, transform, or engineer before training.

#### Quiz: Summarizing the Relationship between Two Features
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

---

## Quick EDA checklist

- [ ] Check `.shape`, `.dtypes`, `.isnull().sum()`, `.describe()`.
- [ ] Fix data types (cast strings to numerics, encode categoricals).
- [ ] Handle missing values (drop or impute with justification).
- [ ] Plot distribution of every numeric feature (histogram + box plot).
- [ ] Plot counts of every categorical feature (bar chart).
- [ ] Plot each feature against the target (scatter / grouped box plot).
- [ ] Inspect the correlation matrix for surprises.

---

## See also

- Previous: [06-Python-Pandas.md](06-Python-Pandas.md)
- Next: [08-Math-Statistics.md](08-Math-Statistics.md)
