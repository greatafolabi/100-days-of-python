# Day 004 - Rock Paper Scissors Game
# Play Rock Paper Scissors against the computer!

import random

# ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store in list for easy access
game_images = [rock, paper, scissors]

print("Welcome to Rock Paper Scissors!")
print()

# Get user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Validate input
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    # Show user's choice
    print("\nYou chose:")
    print(game_images[user_choice])
    
    # Computer makes random choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    
    # Determine winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win! Rock beats Scissors!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win! Scissors beats Paper!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win! Paper beats Rock!")
    else:
        print("You lose!")
