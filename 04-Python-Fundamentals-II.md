# Python Fundamentals for ML/AI Engineers (Part II)

Part II extends your Python base into data acquisition, strings, dictionaries, and file handling.

**Learning path:** This is step 4 in [00-START-HERE.md](00-START-HERE.md). Previous: [03-Python-Fundamentals-I.md](03-Python-Fundamentals-I.md). Next: [05-Portfolio-US-Medical-Insurance.md](05-Portfolio-US-Medical-Insurance.md).

---

## Codecademy subsections (exact order)

### 1) Welcome to Python Fundamentals for Machine Learning/AI Engineering Part II

- Key expectations: by the end of Part II you can load data from a CSV, clean strings, build lookup structures with dicts, and write analysis output to a file.
- How this connects to Part I: Part I gave you the building blocks (variables, functions, loops, lists); Part II shows you how those blocks combine to do real data work before introducing Pandas in module 06.

---

### 2) Data Acquisition

**Where data comes from:**
- Local files: CSV, JSON, TXT, Excel.
- Public APIs: return JSON; use the `requests` library.
- Databases: SQL queries via `sqlite3` or `psycopg2`.
- Web scraping: `BeautifulSoup` / `requests` (last resort; check terms of service).

**How to load data (plain Python, before Pandas):**
```python
import csv

rows = []
with open("data/insurance.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)   # each row is a dict keyed by header
    for row in reader:
        rows.append(row)

print(rows[0])
# {'age': '19', 'sex': 'female', 'bmi': '27.9', 'children': '0',
#  'smoker': 'yes', 'region': 'southwest', 'charges': '16884.924'}
```

**Data format notes:**
- `csv.DictReader` gives a dict per row but **all values are strings** — cast manually.
- JSON: `import json; data = json.load(f)` inside a `with open(...)` block.
- Common pitfall: forgetting `newline=""` in `open()` for CSV on Windows causes blank rows.

---

### 3) Python Strings

**String methods used:**
```python
s = "  Hello, World!  "

s.strip()          # "Hello, World!"   — remove leading/trailing whitespace
s.lower()          # "  hello, world!  "
s.upper()          # "  HELLO, WORLD!  "
s.replace(",", "") # "  Hello World!  "
s.split(", ")      # ["  Hello", "World!  "]
"World" in s       # True
s.startswith("  H")# True
s.count("l")       # 3
```

**Parsing / cleanup patterns:**
```python
# Normalise a categorical column read from CSV
def clean_sex(raw):
    val = raw.strip().lower()
    if val in ("m", "male"):
        return "male"
    elif val in ("f", "female"):
        return "female"
    return "unknown"

# f-string formatting (Python 3.6+)
name = "Alex"
score = 94.567
print(f"Student: {name}, Score: {score:.1f}%")
# Student: Alex, Score: 94.6%
```

**Common string pitfalls:**
- Strings are **immutable** — `s.strip()` returns a new string; it does not change `s` in place.
- `"3" + 3` raises `TypeError`; must cast: `int("3") + 3`.
- Use f-strings (`f"..."`) for formatting; avoid `%` formatting and `.format()` in new code.

---

### 4) Python Dictionaries

**Dictionary access/update patterns:**
```python
patient = {"age": 35, "smoker": "yes", "charges": 12000.50}

# Access
age = patient["age"]           # KeyError if key missing
age = patient.get("age", 0)    # safe — returns 0 if missing

# Update / add
patient["region"] = "southwest"
patient["charges"] = 13500.00

# Remove
del patient["smoker"]
removed = patient.pop("region", None)  # safe pop

# Iterate
for key, value in patient.items():
    print(f"{key}: {value}")

# Check membership
"age" in patient   # True
```

**Nested dictionary notes:**
```python
# Build a summary dict from a list of rows
summary = {}
for row in rows:
    region = row["region"]
    charge = float(row["charges"])
    if region not in summary:
        summary[region] = {"total": 0, "count": 0}
    summary[region]["total"] += charge
    summary[region]["count"] += 1

# Compute averages
for region, data in summary.items():
    avg = data["total"] / data["count"]
    print(f"{region}: avg charge = {avg:.2f}")
```

**When dict is better than list:**
- When you need **O(1) key-based lookup** instead of O(n) search.
- When data has named fields (use dict) rather than ordered positions (use list).
- When counting occurrences: `counts = {}; counts[key] = counts.get(key, 0) + 1`.

---

### 5) Python Files

**Reading files:**
```python
# Read entire file as a string
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Read line by line (memory-efficient for large files)
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

**Writing files:**
```python
results = [("northeast", 13406.38), ("southwest", 12346.94)]

with open("output/avg_charges.txt", "w", encoding="utf-8") as f:
    f.write("Region,Avg Charge\n")
    for region, avg in results:
        f.write(f"{region},{avg:.2f}\n")
```

**File path and encoding gotchas:**
- Always use `encoding="utf-8"` to avoid platform-specific surprises.
- Use `pathlib.Path` for cross-platform paths: `from pathlib import Path; path = Path("data") / "insurance.csv"`.
- `"w"` mode **overwrites** existing files. Use `"a"` to append.
- The `with` statement automatically closes the file — prefer it over manual `f.close()`.

---

### 6) Reggie's Linear Regression Cumulative Project

**Project objective:**
- Implement a simple linear regression from scratch (no libraries) to find the best-fit line through a set of 2D data points.
- This exercises: functions, loops, lists, and basic maths — all from Part I and II.

**My approach:**
1. Represent the line as `y = m * x + b` where `m` is slope and `b` is intercept.
2. Write a function to compute the error (sum of squared residuals) for any `(m, b)` pair.
3. Step through candidate `m` and `b` values to find the minimum error (brute-force gradient search).

**Key code blocks:**
```python
def get_y(m, b, x):
    return m * x + b

def calculate_error(m, b, point):
    x, y = point
    predicted = get_y(m, b, x)
    return abs(predicted - y)

def calculate_all_error(m, b, points):
    total = 0
    for point in points:
        total += calculate_error(m, b, point)
    return total

# Find best m and b by brute-force search
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
best_m, best_b, best_error = 0, 0, float("inf")

for m in [i * 0.1 for i in range(-100, 100)]:
    for b in [i * 0.1 for i in range(-100, 100)]:
        error = calculate_all_error(m, b, datapoints)
        if error < best_error:
            best_error = error
            best_m, best_b = m, b

print(f"Best m={best_m}, b={best_b}, error={best_error}")
```

**Final takeaway:**
- Linear regression minimises the distance between predicted and actual values.
- In practice, gradient descent does this efficiently instead of brute-force search.
- This project is the conceptual bridge to the ML maths in module 08.

---

## See also

- Previous: [03-Python-Fundamentals-I.md](03-Python-Fundamentals-I.md)
- Next: [05-Portfolio-US-Medical-Insurance.md](05-Portfolio-US-Medical-Insurance.md)
