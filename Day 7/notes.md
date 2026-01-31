# Day 7 Quick Reference: Hangman & Game Logic

## While Loop Game Pattern
```python
game_over = False
while not game_over:
    # Game logic
    if win_condition:
        game_over = True
    if lose_condition:
        game_over = True
```

## String Building in Loops
```python
display = ""
for item in collection:
    if condition:
        display += item
    else:
        display += "_"
```

## Life/Health System
```python
lives = 6
if wrong_action:
    lives -= 1
    if lives == 0:
        game_over = True
```

## List Indexing for States
```python
stages = ["stage0", "stage1", "stage2"]
current_stage = stages[index]
```

## Key Takeaways
- While loops are perfect for game flow
- Boolean flags control when loops end
- String concatenation builds displays dynamically
- List indexing can represent visual states
- Track game state with variables (lives, correct_letters, etc.)

## Common Mistakes Fixed Today
1. **Indentation**: Game logic must be INSIDE the while loop
2. **Boolean types**: Use `True/False`, not `"true"/"false"`
3. **Variable names**: Use the actual variable name, not a string

## Next: Day 8 - Functions
Breaking code into reusable pieces!
```

---
