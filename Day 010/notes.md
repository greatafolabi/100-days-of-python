# Day 10 Quick Reference: Functions with Outputs

## Return Statement Basics

### Function WITHOUT Return
```python
def greet(name):
    print(f"Hello {name}")

greet("Daniel")  # Prints but returns None
result = greet("Daniel")  # result = None
```

### Function WITH Return
```python
def greet(name):
    return f"Hello {name}"

message = greet("Daniel")  # Can store the value
print(message)  # Use it later
```

## Return vs Print

| Feature | Print | Return |
|---------|-------|--------|
| Shows output | ✅ Yes | ❌ No (unless you print it) |
| Can store value | ❌ No | ✅ Yes |
| Ends function | ❌ No | ✅ Yes |
| Use in expressions | ❌ No | ✅ Yes |
```python
# Print example
def add_print(a, b):
    print(a + b)

add_print(2, 3)  # Shows 5
x = add_print(2, 3)  # x = None

# Return example
def add_return(a, b):
    return a + b

result = add_return(2, 3)  # result = 5
print(result)  # Now we print when we want
```

## Multiple Return Values

### Returning Tuples
```python
def calculate(a, b):
    sum_result = a + b
    product = a * b
    return sum_result, product  # Returns tuple

total, prod = calculate(5, 3)
print(total)  # 8
print(prod)   # 15
```

### Early Returns
```python
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"  # Early exit
    return a / b
```

## Docstrings

### Single Line Docstring
```python
def add(a, b):
    """Add two numbers together."""
    return a + b
```

### Multi-Line Docstring
```python
def calculate_grade(score):
    """
    Convert numerical score to letter grade.
    
    Parameters:
    score (int): The numerical score (0-100)
    
    Returns:
    str: Letter grade (A, B, C, D, F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    # ... etc
```

### Accessing Docstrings
```python
print(add.__doc__)  # Shows the docstring
help(add)  # Shows formatted help
```

## String Methods

### Title Case
```python
name = "daniel afolabi"
print(name.title())  # Daniel Afolabi

# Also works with multiple words
text = "chemical engineering student"
print(text.title())  # Chemical Engineering Student
```

### Other Useful String Methods
```python
text = "hello world"

text.upper()      # HELLO WORLD
text.lower()      # hello world
text.capitalize() # Hello world
text.title()      # Hello World
```

## Functions as Dictionary Values

### Storing Functions
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Store functions in dictionary
operations = {
    "+": add,
    "-": subtract
}
```

### Calling Functions from Dictionary
```python
# Method 1: Get function then call
operation = operations["+"]
result = operation(5, 3)

# Method 2: Call directly
result = operations["+"](5, 3)
```

## Best Practices

### 1. Always Return Something
```python
# Bad: Sometimes returns, sometimes doesn't
def process(data):
    if data:
        return data * 2
    # Missing return for else case

# Good: Always returns
def process(data):
    if data:
        return data * 2
    return None
```

### 2. One Purpose Per Function
```python
# Bad: Function does too much
def calculate_and_print(a, b):
    result = a + b
    print(f"The answer is {result}")
    return result

# Good: Separate concerns
def calculate(a, b):
    return a + b

result = calculate(5, 3)
print(f"The answer is {result}")
```

### 3. Use Docstrings
```python
# Good: Documented function
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9
```

## Common Patterns

### Calculator Pattern
```python
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error"
}

result = operations["+"](10, 5)
```

### Validation Pattern
```python
def is_valid_email(email):
    """Check if email format is valid."""
    if "@" in email and "." in email:
        return True
    return False

if is_valid_email(user_input):
    print("Valid email!")
```

## Key Takeaways

1. **Return** gives values back, **print** just displays
2. **Return immediately exits** the function
3. Can return **multiple values** as tuples
4. **Docstrings** make code professional and maintainable
5. **Functions can be stored** in data structures
6. Always **document your functions**!

## Next Steps
Day 11: Building more complex applications with these function concepts!
```
