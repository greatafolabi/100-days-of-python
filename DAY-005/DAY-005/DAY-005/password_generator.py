# Day 005 - PyPassword Generator
# Create strong, random passwords!

import random

# Character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Get user requirements
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# Build password as a list
password_list = []

# Add random letters
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list (important for security!)
random.shuffle(password_list)

# Convert list to string
password = ""
for char in password_list:
    password += char

# Display the password
print(f"Your password is: {password}")
