 Day 005 - Quick Notes

## Topics Covered:
- For loops
- The range() function
- Code blocks and indentation
- Looping through lists
- Accumulator pattern
- Combining loops with conditionals

## For Loop Syntax:
```python
for item in sequence:
    # code block (indented!)
    # runs for each item
```

## Range Function:
```python
range(5)           # 0, 1, 2, 3, 4
range(1, 6)        # 1, 2, 3, 4, 5
range(0, 10, 2)    # 0, 2, 4, 6, 8

# range(start, stop, step)
# start: inclusive (default 0)
# stop: EXCLUSIVE (not included!)
# step: increment (default 1)
```

## Important Notes:
- **Indentation matters!** 4 spaces or 1 tab
- **Stop value is EXCLUSIVE** - range(1, 11) = 1 to 10
- **Start value is INCLUSIVE** - range(1, 11) starts at 1
- Loops can iterate through lists, strings, ranges
- Code inside loop runs for EACH item

## Common Loop Patterns:

### Accumulator Pattern:
```python
total = 0
for i in range(1, 11):
    total += i
# total = 55
```

### Loop Through List:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Build New List:
```python
numbers = [1, 2, 3]
doubled = []
for num in numbers:
    doubled.append(num * 2)
```

### Loop + Conditional:
```python
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
```

## FizzBuzz Key Points:
- Check divisible by 15 FIRST (before 3 or 5)
- Use modulo `%` to check divisibility
- `number % 3 == 0` means divisible by 3
- Order of conditions matters!

## Password Generator Key Points:
- Build password as LIST first
- Use `random.choice()` for random selection
- Use `random.shuffle()` to randomize order
- Convert list to string with `"".join(list)` or loop
- Shuffling = more secure passwords

## Common Mistakes Avoided:
- ❌ `range(5)` thinking it includes 5 (it doesn't!)
- ❌ Forgetting to indent code inside loop
- ❌ Checking FizzBuzz conditions in wrong order
- ❌ Trying to shuffle a string (must be list!)
- ✅ Always indent loop body
- ✅ Remember: range stop is EXCLUSIVE
- ✅ Check combined conditions first in FizzBuzz

## Projects Built:
1. **FizzBuzz** - Classic interview challenge
2. **Password Generator** - Practical security tool

## Concepts Mastered:
✅ For loops
✅ Range function (all variations)
✅ Indentation and code blocks
✅ Looping through lists
✅ Accumulator pattern
✅ Combining loops + conditionals
✅ Combining loops + randomization

## Real-World Applications:
- Data processing (loop through records)
- Automation (repeat tasks)
- Game development (game loops)
- Password generation (security)
- Data analysis (process datasets)
- Web scraping (iterate through pages)

## Ideas for Practice:
- Multiplication table generator
- Prime number finder
- Average calculator from user input
- Countdown timer
- Pattern printer (pyramids, diamonds)
```

**Commit message:** `Add Day 5 quick notes`

---
