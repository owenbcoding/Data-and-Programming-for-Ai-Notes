# Variables

## What are Variables?
Variables are containers for storing data values. They allow us to label data with a descriptive name, making our code more readable and easier to maintain.

## Creating Variables

### Basic Assignment
```python
x = 5
name = "Alice"
price = 19.99
is_active = True
```

### Variable Naming Rules
- **Start with letter or underscore**: Not a number
- **Letters, numbers, underscores**: Only these characters
- **Case-sensitive**: `myVar` and `myvar` are different
- **No reserved words**: Can't use Python keywords
- **Descriptive names**: Use meaningful names

### Naming Conventions
```python
# Good variable names
user_name = "Alice"
total_price = 19.99
is_logged_in = True
item_count = 5

# Bad variable names
x = "Alice"  # Not descriptive
n = 5  # Not clear what n represents
flag = True  # Not descriptive
```

## Data Types

### Common Data Types
```python
# Integer (int)
age = 25

# Float (float)
price = 19.99

# String (str)
name = "Alice"

# Boolean (bool)
is_active = True

# List
items = [1, 2, 3, 4, 5]

# Dictionary
person = {"name": "Alice", "age": 25}

# Tuple
coordinates = (10, 20)

# Set
unique_items = {1, 2, 3, 4, 5}
```

### Checking Data Types
```python
x = 5
print(type(x))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>
```

## Assignment

### Simple Assignment
```python
x = 5
y = "Hello"
z = 3.14
```

### Multiple Assignment
```python
# Multiple variables from values
x, y, z = 5, "Hello", 3.14

# Same value to multiple variables
x = y = z = 0
```

### Assignment from Expressions
```python
# Result of expression
sum_result = 5 + 3
average = (10 + 20 + 30) / 3
```

## Variable Scope

### Local Variables
```python
def my_function():
    local_var = 10  # Local to function
    print(local_var)

my_function()
# print(local_var)  # Error: not defined outside function
```

### Global Variables
```python
global_var = 10  # Global variable

def my_function():
    print(global_var)  # Can access global variable

my_function()
print(global_var)  # Can access outside function
```

### Modifying Global Variables
```python
global_var = 10

def modify_global():
    global global_var
    global_var = 20

modify_global()
print(global_var)  # Prints 20
```

## Variable Reassignment

### Reassigning Variables
```python
x = 5
print(x)  # 5

x = 10
print(x)  # 10

x = "Hello"
print(x)  # "Hello"
```

### Type Changes
```python
x = 5
print(type(x))  # <class 'int'>

x = "Hello"
print(type(x))  # <class 'str'>
```

## Best Practices

### Descriptive Names
```python
# Good
user_name = "Alice"
total_price = 19.99
is_logged_in = True

# Avoid
x = "Alice"
n = 5
flag = True
```

### Consistent Style
```python
# Follow PEP 8 naming conventions
snake_case for variables
user_name = "Alice"
total_items = 5
is_active = True
```

### Avoid Overwriting Built-ins
```python
# Avoid using built-in function names
# list = [1, 2, 3]  # Bad: overwrites list()
numbers = [1, 2, 3]  # Good
```

## Common Mistakes

### Using Reserved Words
```python
# This will cause an error
print = 5  # Overwrites print function
# print("Hello")  # Error: print is not callable
```

### Case Sensitivity
```python
my_var = 5
MyVar = 10
myvar = 15

# These are all different variables
print(my_var)  # 5
print(MyVar)  # 10
print(myvar)  # 15
```

### Undefined Variables
```python
# This will cause an error
print(undefined_var)  # NameError: name 'undefined_var' is not defined
```

## Dynamic Typing

### Dynamic Typing
```python
# Python is dynamically typed
x = 5  # int
x = "Hello"  # str
x = 3.14  # float
x = [1, 2, 3]  # list
```

### Type Checking
```python
x = 5
if isinstance(x, int):
    print("x is an integer")

x = "Hello"
if isinstance(x, str):
    print("x is a string")
```

## Practical Examples

### Data Science Context
```python
# Storing data
dataset_name = "sales_data"
n_samples = 1000
n_features = 10
has_missing_values = False
column_names = ["age", "income", "education"]
```

### Machine Learning Context
```python
# Model parameters
learning_rate = 0.01
n_epochs = 100
batch_size = 32
is_trained = False
model_accuracy = 0.95
```

### Web Development Context
```python
# User data
username = "alice"
email = "alice@example.com"
is_active = True
last_login = "2023-06-15"
user_id = 12345
```

## Variable Storage

### Memory Considerations
- **Small values**: Minimal memory usage
- **Large datasets**: Significant memory usage
- **Reference semantics**: Variables store references
- **Garbage collection**: Python manages memory
- **Memory profiling**: Use tools for large data

### Variable Deletion
```python
x = 5
del x  # Delete the variable
# print(x)  # Error: name 'x' is not defined
```

## Debugging with Variables

### Print Variables
```python
x = 5
y = 10
print(f"x = {x}, y = {y}")
print(f"x + y = {x + y}")
```

### Using Debugger
- Use IDE debugger
- Set breakpoints
- Inspect variable values
- Step through code
- Watch variables

## Constants

### Convention for Constants
```python
# Convention: use UPPER_CASE for constants
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_KEY = "your_api_key"
DATABASE_URL = "database_url"
```

### Immutability
- Python doesn't enforce constants
- Use UPPER_CASE convention
- Be careful with modification
- Document as constant
- Avoid reassignment