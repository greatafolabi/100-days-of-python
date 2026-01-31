# Day 8 Quick Reference: Functions & Caesar Cipher

## Function Basics

### Defining a Function
```python
def function_name(parameter1, parameter2):
    # Function body
    result = parameter1 + parameter2
    return result
```

### Calling a Function
```python
# Positional arguments (order matters)
function_name(5, 10)

# Keyword arguments (order doesn't matter)
function_name(parameter2=10, parameter1=5)
```

## Parameters vs Arguments

**Parameters**: Variables listed in function definition
```python
def greet(name, age):  # name and age are PARAMETERS
    print(f"Hello {name}, you are {age}")
```

**Arguments**: Actual values passed when calling
```python
greet("Daniel", 20)  # "Daniel" and 20 are ARGUMENTS
```

## Positional vs Keyword Arguments

### Positional Arguments
```python
def calculate(x, y, z):
    return x + y * z

calculate(2, 3, 4)  # x=2, y=3, z=4 (order matters!)
```

### Keyword Arguments
```python
calculate(z=4, x=2, y=3)  # Order doesn't matter with keywords
```

### Mixing Both
```python
calculate(2, z=4, y=3)  # Positional first, then keyword
# calculate(x=2, 3, 4)  # ERROR! Can't use positional after keyword
```

## Caesar Cipher Algorithm

### Encryption (Shift Forward)
```python
shifted_position = (current_position + shift) % 26
```

### Decryption (Shift Backward)
```python
shifted_position = (current_position - shift) % 26
```

### Why Modulo (%) ?
- Handles wraparound: z + 1 = a
- Example: position 25 (z) + 1 = 26 % 26 = 0 (a)

## Key Takeaways

1. **Functions make code reusable** - write once, use many times
2. **Parameters = placeholders**, Arguments = actual values
3. **Positional arguments** depend on order
4. **Keyword arguments** are explicit and order-independent
5. **Modulo operator** (%) is perfect for circular/wraparound logic

## Common Mistakes Fixed Today

1. ❌ Calling function inside its own definition (recursion by accident)
2. ❌ Confusing parameters with arguments
3. ❌ Forgetting to handle edge cases (wraparound)
4. ✅ Using keyword arguments for clarity

## Next Steps

Day 9: More function concepts - scope, return values, nested functions?

---

**Caesar Cipher Fun Fact:**  
Named after Julius Caesar who used it to protect military messages!  
ROT13 (shift of 13) is still used today for spoiler protection online.
```
