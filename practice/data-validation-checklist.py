# Data Validation Checklist
# Practice file for data quality assessment

def validate_data_quality(data):
    """
    Basic data quality validation checklist
    Returns a dictionary of validation results
    """
    results = {
        'completeness': {},
        'accuracy': {},
        'consistency': {},
        'timeliness': {},
        'uniqueness': {},
        'validity': {}
    }
    
    # 1. Completeness Check
    # Check for missing values
    missing_counts = data.isnull().sum()
    missing_percentage = (missing_counts / len(data)) * 100
    results['completeness'] = {
        'missing_counts': missing_counts.to_dict(),
        'missing_percentage': missing_percentage.to_dict()
    }
    
    # 2. Accuracy Check
    # Check for values outside expected ranges
    # (This would be customized based on your data)
    
    # 3. Consistency Check
    # Check for inconsistent formats or units
    
    # 4. Timeliness Check
    # Check if data is up to date
    
    # 5. Uniqueness Check
    # Check for duplicate records
    duplicate_count = data.duplicated().sum()
    results['uniqueness'] = {
        'duplicate_count': duplicate_count,
        'duplicate_percentage': (duplicate_count / len(data)) * 100
    }
    
    # 6. Validity Check
    # Check if values conform to expected data types and formats
    
    return results

# Example usage (commented out since we don't have pandas available yet)
# import pandas as pd
# df = pd.read_csv('data-quality-sample.csv')
# validation_results = validate_data_quality(df)
# print(validation_results)

# Manual validation exercises to practice:

print("=== DATA VALIDATION EXERCISES ===")
print("\nExercise 1: Identify Missing Data")
print("Look at the CSV file and identify:")
print("- Which columns have missing values?")
print("- What percentage of data is missing in each column?")
print("- How might missing data impact analysis?")

print("\nExercise 2: Identify Invalid Data")
print("Look for values that don't make sense:")
print("- Negative values where only positive expected")
print("- Text in numeric fields")
print("- Dates in wrong format")
print("- Values outside reasonable ranges")

print("\nExercise 3: Identify Duplicate Data")
print("Check for:")
print("- Complete duplicate rows")
print("- Duplicate IDs with different other values")
print("- Near-duplicates (same person, slight variations)")

print("\nExercise 4: Identify Inconsistent Data")
print("Look for:")
print("- Inconsistent formats (MM/DD/YYYY vs DD/MM/YYYY)")
print("- Inconsistent categories (US vs USA vs United States)")
print("- Inconsistent units (kg vs lbs)")

print("\nExercise 5: Data Quality Score")
print("Create a simple scoring system:")
print("- 0-25% missing: Excellent")
print("- 26-50% missing: Good")
print("- 51-75% missing: Fair")
print("- 76-100% missing: Poor")

# Practice template
validation_template = """
## Data Validation Report

### Dataset: [Name]
### Date: [Date]
### Validator: [Your Name]

#### Completeness
- Overall completeness: [X]%
- Most complete field: [Field name] ([X]%)
- Least complete field: [Field name] ([X]%)

#### Accuracy
- Invalid values found: [X]
- Most common issue: [Description]

#### Consistency
- Inconsistent formats found: [X]
- Fields affected: [List]

#### Timeliness
- Data currency: [Date range]
- Staleness assessment: [Fresh/Stale]

#### Uniqueness
- Duplicate records: [X]
- Duplicate percentage: [X]%

#### Validity
- Data type violations: [X]
- Format violations: [X]

#### Overall Quality Score: [X/10]
#### Recommendations: [List improvements needed]
"""

print("\n=== VALIDATION TEMPLATE ===")
print(validation_template)
