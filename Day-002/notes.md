# Day 002 - Quick Notes

## Data Types Covered:
1. **String (str)** - Text data
2. **Integer (int)** - Whole numbers
3. **Float (float)** - Decimal numbers
4. **Boolean (bool)** - True/False

## Key Concepts:
- **Subscripting:** Access characters with `[index]`
- **Concatenation:** Join strings with `+`
- **Type Checking:** Use `type()` function
- **Type Conversion:** `str()`, `int()`, `float()`

## Mathematical Operations:
```python
+ - * /     # Basic operations
**          # Exponent (power)
//          # Floor division
%           # Modulo (remainder)
```

## PEMDAS:
Parentheses → Exponents → Multiplication/Division → Addition/Subtraction

## Type Conversion Examples:
```python
num_str = "123"
num_int = int(num_str)  # Convert to integer
num_float = float(num_str)  # Convert to float

age = 25
age_str = str(age)  # Convert to string
```

## Important Notes:
- `input()` ALWAYS returns a string!
- Must convert to int/float for math
- Use `round(number, 2)` for money (2 decimals)
- Type errors occur when mixing incompatible types

## Questions Answered:
- Why do I need type conversion? → Because input() gives strings!
- When to use int vs float? → Int for whole numbers, float for decimals
- How does subscripting work? → `text[0]` = first character (zero-based!)

## Ideas for Practice:
- Build a currency converter
- Create a BMI calculator
- Make a percentage calculator
