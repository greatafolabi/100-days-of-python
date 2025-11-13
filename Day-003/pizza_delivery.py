# Day 003 - Pizza Delivery App
# Calculate pizza bill based on size and toppings

print("Welcome to Python Pizza Deliveries!")
print()

# Get user choices
size = input("What size pizza do you want? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Start with base price
bill = 0

# Calculate base price by size
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size!")

# Add pepperoni cost (different for small vs medium/large)
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:  # M or L
        bill += 3

# Add extra cheese cost
if extra_cheese == "Y":
    bill += 1

# Display final bill
print(f"\nYour final bill is: ${bill}")
print("Thank you for ordering! 🍕")
