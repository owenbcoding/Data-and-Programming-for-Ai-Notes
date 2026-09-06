# print()

## The print() Function
The `print()` function is one of the most fundamental functions in Python, used to display output to the console.

## Basic Usage

### Simple Printing
```python
print("Hello, World!")
print(42)
print(3.14)
```

### Multiple Arguments
```python
print("Hello", "World")
print("Name:", "John", "Age:", 25)
```

### Separator
```python
print("Hello", "World", sep="-")
print("Name:", "John", "Age:", 25, sep=" | ")
```

### End Character
```python
print("Hello", end=" ")
print("World")  # Prints "Hello World"
```

## Data Types in print()

### Strings
```python
print("This is a string")
print('Single quotes work too')
```

### Numbers
```python
print(42)      # Integer
print(3.14)    # Float
print(2 + 3)   # Expression
```

### Booleans
```python
print(True)
print(False)
```

### Variables
```python
name = "Alice"
age = 30
print(name)
print(age)
```

## String Formatting

### f-strings (Python 3.6+)
```python
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")
```

### format() method
```python
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))
```

### % formatting (older method)
```python
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))
```

## Advanced Usage

### Print to File
```python
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
```

### Suppress Newline
```python
print("Hello", end="")
print("World", end="")
```

### Custom Separator
```python
items = ["apple", "banana", "cherry"]
print(*items, sep=", ")
```

## Common Mistakes

### Forgetting Quotes
```python
# Wrong
print(Hello)  # Error: NameError

# Correct
print("Hello")
```

### Mixing Quotes
```python
# Wrong
print("He said "Hello"")  # Error

# Correct
print('He said "Hello"')
print("He said 'Hello'")
```

### Printing Multiple Items
```python
# Won't work as expected
print("The result is", 2 + 2, "!")  # No spaces between items

# Better
print(f"The result is {2 + 2}!")
```

## Best Practices

### Descriptive Output
```python
print("Calculation complete")  # Informative
print("Error: File not found")  # Clear messages
```

### Debugging
```python
x = 10
print(f"Value of x: {x}")  # Debug variable values
print(f"Type of x: {type(x)}")  # Debug types
```

### User Communication
```python
print("Welcome to the program!")
print("Processing your data...")
print("Analysis complete!")
```

## Use Cases

### Debugging
- Check variable values
- Verify program flow
- Identify errors
- Test code sections

### User Interaction
- Display information
- Show results
- Provide feedback
- Guide users

### Logging
- Program status updates
- Error messages
- Progress indicators
- Informational messages

## print() vs. return
- **print()**: Displays output to console
- **return**: Returns value from function
- **print()**: Used for display and debugging
- **return**: Used for function results
- **Key difference**: print() doesn't return the value