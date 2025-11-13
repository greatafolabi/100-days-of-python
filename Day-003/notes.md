# Day 003 - Quick Notes

## Topics Covered:
- Control Flow
- If/Else statements
- Elif (else if)
- Comparison operators
- Logical operators (and, or, not)
- Nested conditionals
- Code blocks and indentation
- Scope

## Comparison Operators:
```python
>   # Greater than
<   # Less than
>=  # Greater than or equal
<=  # Less than or equal
==  # Equal to
!=  # Not equal to
```

## Logical Operators:
```python
and  # Both conditions must be True
or   # At least one condition must be True
not  # Reverses the condition
```

## If/Elif/Else Structure:
```python
if condition1:
    # executed if condition1 is True
elif condition2:
    # executed if condition1 is False and condition2 is True
elif condition3:
    # executed if above are False and condition3 is True
else:
    # executed if all conditions are False
```

## Nested Conditionals:
```python
if condition1:
    if condition2:
        if condition3:
            # deep nesting
        else:
            # alternative
    else:
        # alternative
else:
    # alternative
```

## Important Points:
- **Indentation matters!** Python uses whitespace to define code blocks
- Use 4 spaces (or 1 tab) for each indentation level
- `elif` is better than multiple `if` for related conditions
- Comparison operators return Boolean (True/False)
- Logical operators combine multiple conditions
- Nested if statements can get complex - plan logic carefully
- `.lower()` or `.upper()` helps with user input consistency

## Common Mistakes to Avoid:
- Using `=` (assignment) instead of `==` (comparison)
- Forgetting colons `:` after if/elif/else
- Wrong indentation levels
- Not handling all possible user inputs

## Practice Tips:
- Draw decision trees for complex logic
- Test every possible path in your code
- Use descriptive variable names
- Comment your code for clarity

## Projects Built:
1. **Pizza Delivery App** - Conditional pricing logic
2. **Treasure Island Game** - Nested conditionals for game paths

## Concepts Mastered:
✅ Basic if/else
✅ Multiple elif statements
✅ Comparison operators
✅ Logical operators
✅ Nested if statements
✅ Code block structure
✅ Building interactive programs

## Questions Answered:
- When to use `if` vs `elif`? → Use elif for mutually exclusive conditions
- How deep can nesting go? → As deep as needed, but keep it readable!
- Why indentation errors? → Python requires consistent spacing
- How to handle invalid input? → Add else clause for unexpected values

## Ideas for Practice:
- Build a calculator with operations choice
- Create a quiz game with scoring
- Make a simple RPG with choices
- Build a vending machine simulator
```

