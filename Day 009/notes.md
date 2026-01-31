
# Day 9 Quick Reference: Dictionaries & Nesting

## Dictionary Basics

### Creating Dictionaries
```python
# Empty dictionary
my_dict = {}

# Dictionary with data
student = {
    "name": "Daniel",
    "age": 20,
    "course": "Chemical Engineering"
}
```

### Accessing Values
```python
print(student["name"])  # Output: Daniel
```

### Adding/Updating
```python
student["university"] = "UNILAG"  # Add new key
student["age"] = 21  # Update existing key
```

### Dictionary Methods
```python
student.keys()    # Get all keys
student.values()  # Get all values
student.items()   # Get key-value pairs
```

## Nesting Structures

### List of Dictionaries
```python
students = [
    {"name": "Daniel", "score": 95},
    {"name": "Alice", "score": 87}
]

# Access: students[0]["name"] → "Daniel"
```

### Dictionary of Lists
```python
travel_log = {
    "Nigeria": ["Lagos", "Abuja"],
    "USA": ["New York", "Houston"]
}

# Access: travel_log["Nigeria"][0] → "Lagos"
```

### Nested Dictionaries
```python
contacts = {
    "Daniel": {
        "phone": "123-456",
        "email": "daniel@email.com"
    },
    "Alice": {
        "phone": "789-012",
        "email": "alice@email.com"
    }
}

# Access: contacts["Daniel"]["email"]
```

## Looping Through Dictionaries

### Loop through keys
```python
for key in my_dict:
    print(key)
```

### Loop through values
```python
for value in my_dict.values():
    print(value)
```

### Loop through key-value pairs
```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

## When to Use What?

**Use Lists when:**
- Order matters
- You need indexed access
- Data is homogeneous (all same type)

**Use Dictionaries when:**
- You need labeled data
- Fast lookup by key is important
- Data has attributes/properties

**Use Nesting when:**
- Data has multiple levels
- Real-world complexity (users with orders, posts with comments)
- APIs return JSON (nested dictionaries/lists)

## Common Patterns

### Finding Maximum in Dictionary
```python
max_value = 0
max_key = ""

for key in my_dict:
    if my_dict[key] > max_value:
        max_value = my_dict[key]
        max_key = key
```

### Converting Between Structures
```python
# List of names to dictionary with counts
names = ["Alice", "Bob", "Alice"]
name_counts = {}

for name in names:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
```

## Key Takeaways

1. Dictionaries use `{}`, accessed by keys not indices
2. Keys must be unique and immutable (strings, numbers, tuples)
3. Values can be anything (including other dictionaries/lists!)
4. Nesting = combining lists and dictionaries for complex data
5. Plan your data structure before coding!

## Next: Day 10
More Python concepts building on data structures!
```
