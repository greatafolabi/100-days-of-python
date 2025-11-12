# Day 002 - Data Types & Tip Calculator ✅

**Date:** November 12, 2024  
**Course Section:** Day 2 - Understanding Data Types and How to Manipulate Strings  
**Status:** ✅ Completed

---

## 📝 What I Learned Today

### The 4 Python Data Types:

#### 1. **Strings (str)** 📝
- Text data enclosed in quotes
- **Concatenation** - Joining strings together with `+`
- **Subscripting** - Accessing individual characters using `[index]`
  - Example: `"Hello"[0]` gives `"H"`
  - Python uses zero-based indexing!

#### 2. **Integers (int)** 🔢
- Whole numbers without decimal points
- Can be positive or negative
- Examples: `123`, `-45`, `0`

#### 3. **Floats (float)** 🎯
- Numbers with decimal points
- Used for precise calculations
- Examples: `3.14`, `2.5`, `-0.75`

#### 4. **Booleans (bool)** ✓✗
- True or False values
- Used for logical operations
- Only two values: `True` or `False`

---

## 🔍 Type Operations Learned

### Type Error
- What happens when you mix incompatible types
- Example: Can't add a string and an integer directly

### Type Checking
- Using `type()` to check what data type a variable is
- Example: `type(123)` returns `<class 'int'>`

### Type Conversion (Type Casting)
- Converting between data types:
  - `str()` - Convert to string
  - `int()` - Convert to integer
  - `float()` - Convert to float
- Super useful for calculations with user input!

---

## ➗ Mathematical Operations

### Basic Operations:
- **Addition:** `+`
- **Subtraction:** `-`
- **Multiplication:** `*`
- **Division:** `/` (always gives float)
- **Exponent:** `**` (power)
- **Floor Division:** `//` (division without decimals)
- **Modulo:** `%` (remainder)

### PEMDAS Order:
**P**arentheses → **E**xponents → **M**ultiplication/**D**ivision → **A**ddition/**S**ubtraction

Python follows this order when calculating!

### Number Manipulation:
- Rounding: `round(number, decimal_places)`
- Floor division for whole numbers
- Using `//=` and other assignment operators

---

## 💻 Today's Project

**Project Name:** Tip Calculator 💰

**Description:**
A program that calculates how much each person should pay when splitting a bill, including the tip!

**What it does:**
- Takes the total bill amount
- Asks for tip percentage (10%, 12%, or 15%)
- Asks how many people are splitting the bill
- Calculates each person's share including tip
- Displays the amount each person should pay

**Example Output:**
```
Welcome to the tip calculator!
What was the total bill? $150.00
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 5
Each person should pay: $33.60
```

**The Math Behind It:**
```
Total Bill = $150
Tip % = 12% = 0.12
Tip Amount = $150 × 0.12 = $18
Total with Tip = $150 + $18 = $168
Split by 5 people = $168 ÷ 5 = $33.60
```

---

## 🔥 Challenges Faced

1. **Challenge:** Understanding type conversion - when to use `int()` vs `float()`
   - **Solution:** Realized `input()` always gives strings, so I need to convert them for math!

2. **Challenge:** The tip calculator math was complex at first
   - **Solution:** Broke it down step by step - calculate tip, add to bill, then divide

3. **Challenge:** Getting the output to show exactly 2 decimal places for money
   - **Solution:** Used `round()` function with 2 decimal places

4. **Challenge:** Understanding PEMDAS and parentheses in calculations
   - **Solution:** Used parentheses carefully to control calculation order

---

## ✅ Key Takeaways

- **Strings** need quotes, can be subscripted with `[index]`
- **Always convert** `input()` to `int()` or `float()` for math
- **Type errors** happen when mixing incompatible types
- Use `type()` to check what data type you're working with
- **PEMDAS** matters! Use parentheses to control calculation order
- `round()` is perfect for formatting money to 2 decimal places
- Breaking complex problems into small steps makes them manageable!

**Biggest Breakthrough:** Understanding that I need to convert data types before doing math - this clicked when building the tip calculator!

---

## 💡 Code Snippets

### Type Conversion:
```python
# Converting user input for calculations
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip? "))
people = int(input("How many people? "))
```

### The Calculation:
```python
# Calculate tip and total
tip_as_decimal = tip_percent / 100
tip_amount = bill * tip_as_decimal
total_bill = bill + tip_amount

# Split among people
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
```

### Subscripting Example:
```python
word = "Hello"
print(word[0])  # Prints: H
print(word[4])  # Prints: o
print(word[-1]) # Prints: o (last character)
```

---

## 🎯 Tomorrow's Goal

**Day 003:** Learn about Control Flow and Conditional Statements

Topics to cover:
- If/Else statements
- Comparison operators
- Logical operators
- Building decision-making programs

---

## 📚 Resources Used

- Udemy: 100 Days of Code - Python (Day 2)
- Course exercises on data types
- Tip calculator project walkthrough
- Practice problems

---

## ⏱️ Time Spent

**Total coding time:** ~1.5-2 hours

---

## 📊 Stats

- **Lines of code written:** ~20
- **Concepts learned:** 10+ (data types, operations, conversions)
- **Projects completed:** 1 (Tip Calculator)
- **Type errors encountered and fixed:** Several! 😅
- **"Aha!" moments:** 3 (type conversion, PEMDAS, subscripting)

---

## 💭 Personal Reflection

Day 2 was INTENSE but SO rewarding! 🔥

I learned so much today - 4 data types, type conversion, mathematical operations, PEMDAS... my brain is full but in a good way!

The Tip Calculator was more complex than Day 1's Band Name Generator, but that's the point - I'm leveling up! Breaking down the problem into smaller steps really helped.

**Biggest Challenge:** The tip calculator math seemed overwhelming at first, but once I broke it into steps (calculate tip → add to bill → divide by people → round), it all made sense!

**Biggest Win:** Understanding type conversion! Now I know why I need to convert `input()` to `int()` or `float()` before doing calculations. This is a fundamental concept that will help me every day!

**Favorite New Thing:** Subscripting! Being able to grab individual characters from a string with `[index]` feels like magic. 🪄

**Energy Level:** Still motivated! 2 days down, 98 to go! 💪

---

## 🔗 Social Media Posts

- **Twitter:** [Add your Day 2 tweet link here]
- **LinkedIn:** [Add your Day 2 LinkedIn post link here]

---

**Day 2/100 Complete! ✅**

**Progress:** ▓▓░░░░░░░░░░░░░░░░░░ 2%

**Current Streak:** 2 days 🔥🔥

*"The only way to learn programming is to write programs."*

---

#100DaysOfCode #Python #Day2 #LearningInPublic #DataTypes #ChemicalEngineering #UNILAG

**Previous:** [Day 001](../Day-001/README.md) | **Next:** Day 003
