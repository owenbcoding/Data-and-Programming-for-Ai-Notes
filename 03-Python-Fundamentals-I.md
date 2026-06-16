# Python Fundamentals for ML/AI Engineers (Part I)

Part I focuses on core syntax and small programs: how Python represents information, how control flows, and how to package logic in functions.

**Learning path:** This is step 3 in [00-START-HERE.md](00-START-HERE.md). Next: [04-Python-Fundamentals-II.md](04-Python-Fundamentals-II.md).

---

## Codecademy subsections (exact order)

> Course confirmed: **6 subsections** — Welcome · Python Syntax and Variable Types · Python Functions · Python Control Flow · Python Lists · Python Loops

### 1) Welcome to Python Fundamentals for Machine Learning/AI Engineering (Part I)
`1 Informational`

- Key takeaways: Python is the primary language for data science and ML because of its readable syntax, massive ecosystem (NumPy, Pandas, scikit-learn), and interactive notebook support.
- What this unit expects you to know already: basic computer literacy; nothing about programming assumed.

---

### 2) Python Syntax and Variable Types
`1 Lesson · 1 Quiz · 1 Project`

**Core syntax rules:**
- Python uses **indentation** (4 spaces or 1 tab) instead of braces `{}` to define blocks.
- Lines do not end with a semicolon (optional, but not idiomatic).
- Comments start with `#`; multi-line strings `"""..."""` are used as docstrings.
- Python is **case-sensitive**: `Age` and `age` are different variables.

**Variable naming / assignment patterns:**
- Assignment: `variable_name = value` (no type declaration needed).
- Snake_case is the Python convention: `patient_age`, `total_charges`.
- Variables can be reassigned to a different type at any time (dynamic typing).

**Types and conversion notes:**

| Type | Example | `type()` output |
|---|---|---|
| Integer | `42` | `<class 'int'>` |
| Float | `3.14` | `<class 'float'>` |
| String | `"hello"` | `<class 'str'>` |
| Boolean | `True` / `False` | `<class 'bool'>` |

- Convert between types: `int("42")`, `float("3.14")`, `str(99)`, `bool(0)` → `False`.
- `bool(0)` and `bool("")` are both `False` — watch out for accidental falsy values.

**Snippet:**
```python
age = 28
height_cm = 175.5
name = "Alex"
is_smoker = False

print(type(age))       # <class 'int'>
print(type(height_cm)) # <class 'float'>
```

**Mistakes I made and fixes:**
- Mistake: used `=` (assignment) instead of `==` (comparison) inside an `if` condition.
- Fix: `if x == 5:` not `if x = 5:` — Python raises `SyntaxError` for the latter.

#### Quiz: Python Syntax and Variable Types
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

---

### 3) Python Functions
`1 Informational · 1 Lesson · 1 Quiz · 1 Project`

**Function patterns that clicked:**
- Define with `def`, body indented, return value with `return`.
- If no `return` statement, function returns `None`.
- Calling a function: `result = my_function(arg1, arg2)`.

**Parameters, return values, and scope reminders:**
- **Positional arguments** must be passed in order.
- **Default parameters** let callers skip an argument: `def greet(name, greeting="Hello"):`.
- Variables created inside a function are **local** — they don't exist outside it.
- Use `return` to pass data out of a function; `print()` only displays it.

**Snippet:**
```python
def calculate_bmi(weight_kg, height_m):
    """Return BMI rounded to 1 decimal place."""
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

print(calculate_bmi(70, 1.75))  # 22.9
```

**Reusable helper functions from exercises:**
```python
def pct(part, whole):
    """Return percentage, safe against division by zero."""
    if whole == 0:
        return 0
    return round((part / whole) * 100, 2)
```

#### Quiz: Python Functions
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

---

### 4) Python Control Flow
`1 Lesson · 1 Quiz · 1 Project`

**`if` / `elif` / `else` patterns:**
```python
bmi = 27.5

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Healthy"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(category)  # Overweight
```

**Truthy/falsy gotchas:**
- Falsy values: `0`, `0.0`, `""`, `[]`, `{}`, `None`, `False`.
- Everything else is truthy — so `if my_list:` checks whether the list is non-empty.

**Decision logic examples:**
- Use `and` / `or` / `not` to combine conditions.
- `and` requires both sides to be True; `or` requires at least one.
- Short-circuit: `or` stops at the first truthy value; `and` stops at the first falsy one.

#### Quiz: Python Control Flow
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

---

### 5) Python Lists
`2 Lessons · 1 Article · 2 Quizzes · 2 Projects`

**List operations to remember:**
```python
charges = [1200.50, 4500.00, 800.75, 12000.00]

charges.append(2300.00)    # add to end
charges.insert(0, 500.00)  # insert at index
charges.remove(800.75)     # remove first occurrence
popped = charges.pop()     # remove and return last item
charges.sort()             # sort in place (ascending)
total = sum(charges)
avg   = sum(charges) / len(charges)
```

**Slice/index tricks:**
```python
first   = charges[0]    # first item
last    = charges[-1]   # last item
subset  = charges[1:4]  # index 1, 2, 3 (end exclusive)
reverse = charges[::-1] # reversed copy
```

**When list comprehension is clearer:**
```python
# Filter smoker charges over £5,000
high_charges = [c for c in charges if c > 5000]

# Double every charge
doubled = [c * 2 for c in charges]
```

#### Quiz: Python Lists (×2)
- Quiz 1 score:
- Quiz 2 score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

---

### 6) Python Loops

**`for` loop patterns:**
```python
# Iterate over a list
regions = ["northeast", "northwest", "southeast", "southwest"]
for region in regions:
    print(region.upper())

# Iterate with index
for i, region in enumerate(regions):
    print(f"{i}: {region}")

# Range loop
for i in range(5):   # 0, 1, 2, 3, 4
    print(i)
```

**`while` loop patterns:**
```python
count = 0
while count < 3:
    print(f"Pass {count}")
    count += 1
# Always ensure the condition eventually becomes False to avoid infinite loops.
```

**`break` / `continue` use cases:**
- `break` — exit the loop immediately (e.g. found what you were looking for).
- `continue` — skip the rest of this iteration and go to the next one.
```python
for charge in charges:
    if charge < 0:
        continue        # skip invalid negative charges
    if charge > 50000:
        break           # stop if unreasonably large
    print(charge)
```

#### Quiz: Python Loops
- Score:
- Questions missed:
- Why I missed them:
- Correct rule/concept:

---

## Supplemental: Getting Started Off Platform

> This is not an official course section in the current syllabus — kept here as a personal reference for working locally.

**Local environment commands:**
```bash
python3 --version           # confirm Python version
pip install jupyter pandas  # install packages
jupyter notebook            # launch Jupyter in browser
python3 script.py           # run a script
```

**Folder/project setup:**
```
project/
├── data/
│   └── insurance.csv
├── notebooks/
│   └── analysis.ipynb
└── src/
    └── helpers.py
```

**Running scripts and debugging locally:**
- Use `print()` liberally during debugging; remove or replace with logging before sharing.
- `python3 -i script.py` runs the script then drops you into an interactive shell with all variables in scope.
- Virtual environments: `python3 -m venv venv` then `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows).

---

## Quick reference (fill as you go)

| Topic        | Syntax / idiom          | Remember                          |
|-------------|-------------------------|-----------------------------------|
| Type check  | `type(x)`               | Returns the class, not a string   |
| Length      | `len(seq)`              | Works on lists, strings, dicts    |
| Last item   | `seq[-1]`               | Negative index counts from end    |
| Slice copy  | `seq[:]`                | Shallow copy of entire sequence   |
| In check    | `x in seq`              | Returns bool; O(n) for lists      |
| Sort copy   | `sorted(seq)`           | Returns new list; `sort()` is in-place |

---

## Exercises and scratch work

_Paste Codecademy exercises, snippets, and mistakes worth keeping below._

---

## See also

- Previous: [02-Data-Literacy.md](02-Data-Literacy.md)
- Next: [04-Python-Fundamentals-II.md](04-Python-Fundamentals-II.md)
