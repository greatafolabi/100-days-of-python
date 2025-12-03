# Day 004 - Coin Toss Challenge
# Randomly flip a coin and get Heads or Tails

import random

# Generate random number: 0 or 1
coin = random.randint(0, 1)

# Check result
if coin == 0:
    print("Heads")
else:
    print("Tails")
