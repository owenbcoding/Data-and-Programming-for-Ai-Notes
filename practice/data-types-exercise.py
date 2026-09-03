# Data Types and Structures Practice
# Exercises for understanding different data types

print("=== DATA TYPES PRACTICE ===")

# Exercise 1: Identify Data Types
print("\nExercise 1: Categorize these as structured or unstructured data:")
print("1. Excel spreadsheet with customer information -> Structured")
print("2. Email messages -> Unstructured")
print("3. Database table with product inventory -> Structured")
print("4. Social media posts -> Unstructured")
print("5. Customer survey responses (rating scale 1-5) -> Structured")
print("6. Audio recordings of customer calls -> Unstructured")
print("7. Server log files -> Semi-structured")
print("8. Product reviews with star ratings -> Semi-structured")

# Exercise 2: Numerical vs Categorical Data
print("\nExercise 2: Categorize these as numerical or categorical:")
data_examples = {
    "Customer age": "Numerical (discrete)",
    "Product rating (1-5 stars)": "Categorical (ordinal)",
    "Annual income": "Numerical (continuous)",
    "Gender": "Categorical (nominal)",
    "Number of purchases": "Numerical (discrete)",
    "Country of residence": "Categorical (nominal)",
    "Temperature": "Numerical (continuous)",
    "Education level": "Categorical (ordinal)"
}

for example, answer in data_examples.items():
    print(f"{example}: {answer}")

# Exercise 3: Data Type Conversion Scenarios
print("\nExercise 3: Common conversion scenarios and challenges:")

conversions = [
    {
        "scenario": "Converting 'age' stored as string '28' to integer",
        "method": "int('28')",
        "challenge": "Non-numeric characters, missing values"
    },
    {
        "scenario": "Converting 'price' with currency symbols '$29.99' to float",
        "method": "float('$29.99'.replace('$', '').replace(',', ''))",
        "challenge": "Multiple currency formats, missing symbols"
    },
    {
        "scenario": "Converting 'yes/no' to boolean",
        "method": "boolean_map = {'yes': True, 'no': False}",
        "challenge": "Inconsistent values ('Y', 'N', '1', '0')"
    },
    {
        "scenario": "Converting date strings to datetime objects",
        "method": "pd.to_datetime() or datetime.strptime()",
        "challenge": "Multiple date formats, time zones"
    }
]

for i, conversion in enumerate(conversions, 1):
    print(f"\n{i}. {conversion['scenario']}")
    print(f"   Method: {conversion['method']}")
    print(f"   Challenge: {conversion['challenge']}")

# Exercise 4: Data Structure Identification
print("\nExercise 4: Identify the best data structure for each scenario:")

scenarios = [
    {
        "scenario": "Storing customer information where each customer has unique ID",
        "best_structure": "Dictionary/Hash Map",
        "reason": "O(1) lookup by customer ID"
    },
    {
        "scenario": "Maintaining order of customer service tickets",
        "best_structure": "Queue/List",
        "reason": "FIFO order preservation"
    },
    {
        "scenario": "Storing hierarchical product categories",
        "best_structure": "Tree/JSON",
        "reason": "Natural parent-child relationships"
    },
    {
        "scenario": "Quickly finding if a customer ID exists in a blacklist",
        "best_structure": "Set",
        "reason": "O(1) membership testing"
    }
]

for i, scenario in enumerate(scenarios, 1):
    print(f"\n{i}. {scenario['scenario']}")
    print(f"   Best structure: {scenario['best_structure']}")
    print(f"   Reason: {scenario['reason']}")

# Exercise 5: Data Quality by Type
print("\nExercise 5: Common quality issues by data type:")

quality_issues = {
    "Numerical": [
        "Outliers (extreme values)",
        "Missing values",
        "Wrong units (kg vs lbs)",
        "Precision issues (rounding errors)"
    ],
    "Categorical": [
        "Inconsistent categories (US vs USA)",
        "Too many categories (high cardinality)",
        "Missing categories",
        "Spelling variations"
    ],
    "Text": [
        "Inconsistent formatting",
        "Encoding issues",
        "Special characters",
        "Language mixing"
    ],
    "DateTime": [
        "Format inconsistencies",
        "Time zone issues",
        "Missing components",
        "Invalid dates (Feb 30)"
    ]
}

for data_type, issues in quality_issues.items():
    print(f"\n{data_type}:")
    for issue in issues:
        print(f"  - {issue}")

# Practice Exercise Template
print("\n=== PRACTICE EXERCISE TEMPLATE ===")
print("""
Choose a dataset you have access to and:

1. **Data Type Inventory**
   - List all columns/fields
   - Categorize each as numerical/categorical/text/datetime
   - Identify subtypes (continuous vs discrete, nominal vs ordinal)

2. **Conversion Challenges**
   - Identify fields that need type conversion
   - Document current format vs target format
   - List potential conversion issues

3. **Structure Analysis**
   - Determine if data is structured/unstructured/semi-structured
   - Assess if current structure is optimal for intended use
   - Suggest structural improvements if needed

4. **Quality Assessment**
   - Check for common issues identified above
   - Document any type-specific quality problems
   - Prioritize issues by impact on analysis
""")

print("\n=== REAL-WORLD APPLICATION ===")
print("""
Think about these questions:

1. What data types do you encounter most in your work/studies?
2. Which type conversions do you find most challenging?
3. What quality issues do you see most frequently?
4. How do you decide between different data structures?
5. What tools do you use for data type validation?
""")
