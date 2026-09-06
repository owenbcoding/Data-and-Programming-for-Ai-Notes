# Comments

## What are Comments?
Comments are notes in code that are ignored by the Python interpreter. They are used to explain code, make it more readable, and document the programmer's intent.

## Single-Line Comments

### Creating Single-Line Comments
```python
# This is a single-line comment
x = 5  # This is an inline comment
```

### Usage
- **Code explanation**: Explain what code does
- **Notes**: Add notes for future reference
- **Debugging**: Comment out code temporarily
- **Documentation**: Document logic and decisions

## Multi-Line Comments

### Using Multiple # Characters
```python
# This is a multi-line comment
# that spans multiple lines
# using hash symbols
```

### Using Triple Quotes
```python
"""
This is a multi-line comment
that uses triple quotes
for documentation
"""
```

### Usage of Triple Quotes
- **Docstrings**: Used for function/module documentation
- **Multi-line explanations**: Complex explanations
- **Code blocks**: Documenting code blocks
- **REPL**: In REPL, triple quotes won't be ignored

## Best Practices

### When to Comment
- **Complex logic**: Explain complex or tricky code
- **Decisions**: Document why certain decisions were made
- **Assumptions**: Note any assumptions made
- **TODOs**: Mark areas that need future work
- **Warnings**: Warn about potential issues

### Good Comments
```python
# Calculate the average of the list
average = sum(numbers) / len(numbers)

# TODO: Optimize this for large datasets
def process_data(data):
    return data * 2

# HACK: Temporary fix for known issue
# Note: This should be replaced with proper solution
```

### Bad Comments
```python
# Set x to 5
x = 5  # Redundant, obvious

# Add 2 to x
x = x + 2  # Doesn't add value

# This code calculates the average
# This code adds 2 to x
# This code prints the result
# Comments for obvious code
```

## Commenting Out Code

### Temporary Deactivation
```python
# Debugging code
# print(x)  # Commented out for debugging
# print(y)
```

### Alternative Code
```python
# Old implementation
# x = calculate_old_way()

# New implementation
x = calculate_new_way()
```

## Documentation Comments

### Function Docstrings
```python
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): List of numbers to average
        
    Returns:
        float: The average of the numbers
    """
    return sum(numbers) / len(numbers)
```

### Module Docstrings
```python
"""
This module provides utility functions for data processing.
"""

def process_data(data):
    pass
```

## Commenting Guidelines

### Be Clear and Concise
- Explain why, not just what
- Keep comments up-to-date
- Avoid obvious comments
- Be specific and accurate
- Use proper grammar and spelling

### Keep Comments Relevant
- Remove outdated comments
- Update comments when code changes
- Don't leave commented-out code in production
- Remove debugging comments before deployment
- Keep comments current with code

### Use Consistent Style
- Follow PEP 257 for docstrings
- Use consistent comment style
- Use consistent spacing
- Follow team conventions
- Use style guides

## Common Mistakes

### Over-Commenting
```python
# Too many comments can make code harder to read
# Set x to 5
x = 5
# Add 2 to x
x = x + 2
# Print x
print(x)
```

### Outdated Comments
```python
# This function calculates the mean
def calculate_median(data):
    # Comment is wrong - function name changed
    return sorted(data)[len(data)//2]
```

### Commented-Out Code
```python
# Don't leave commented-out code in production
# old_function()
# backup_function()
# test_function()
```

## Commenting in Different Contexts

### Data Science
```python
# Load the dataset
data = pd.read_csv('data.csv')

# Remove outliers using IQR method
Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3 - Q1
data = data[~((data['value'] < (Q1 - 1.5 * IQR)) | 
              (data['value'] > (Q3 + 1.5 * IQR)))]
```

### Machine Learning
```python
# Split data into training and test sets
# Using 80-20 split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features to have zero mean and unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Web Development
```python
# Check if user is authenticated
if request.method == 'POST':
    # Process form data
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Validate credentials
    if authenticate_user(username, password):
        # Redirect to dashboard
        return redirect(url_for('dashboard'))
```

## Tools for Comments

### IDE Features
- **Comment shortcuts**: Ctrl+/Cmd+/ to comment/uncomment
- **Comment blocks**: Comment/uncomment multiple lines
- **Comment styling**: Different colors for comments
- **Comment templates**: Comment templates
- **Docstring templates**: Docstring templates

### Linters
- **flake8**: Checks for style issues
- **pylint**: More comprehensive linting
- **pydocstyle**: Checks docstring style
- **Comment checking**: Some check comment quality
- **Style enforcement**: Enforce comment style

## Advanced Commenting

### Type Hints in Comments
```python
def process_data(data):
    """
    Process data according to specified algorithm.
    
    Args:
        data (dict): Dictionary containing data
        
    Returns:
        dict: Processed data
    """
    pass
```

### TODO Comments
```python
# TODO: Implement error handling
# FIXME: This is a temporary fix
# HACK: Workaround for known issue
# NOTE: Important note about this code
# XXX: Mark for urgent attention
```

### Section Comments
```python
# ====================
# Data Loading Section
# ====================

# ====================
# Data Processing Section
# ====================
```