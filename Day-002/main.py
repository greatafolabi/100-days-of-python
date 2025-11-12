# Day 002 - Tip Calculator
# Calculate how much each person should pay including tip

print("Welcome to the tip calculator!")

# Get inputs from user
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate tip and total
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# Calculate per person
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# Display result
print(f"Each person should pay: ${final_amount}")
