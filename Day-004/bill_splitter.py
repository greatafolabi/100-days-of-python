# Day 004 - Who Will Pay the Bill?
# Randomly select who pays from a list of friends

import random

# List of friends
friends = ["Alice", "Bob", "Charlie", "David", "Emma"]

# Method 1: Using random.choice()
person_who_pays = random.choice(friends)

print(f"{person_who_pays} is going to buy the meal today!")

# Alternative Method 2: Using random.randint() with indexing
# random_index = random.randint(0, len(friends) - 1)
# person_who_pays = friends[random_index]
# print(f"{person_who_pays} is going to buy the meal today!")
