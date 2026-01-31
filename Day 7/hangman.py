import random

# ASCII art for hangman stages (0 lives to 6 lives)
HANGMAN_STAGES = [
"""
_______
|/      |
|      (_)
|      \|/
|       |
|      / \
|
_|___
""",

"""
_______
|/      |
|      (_)
|      \|/
|       |
|      /
|
_|___
""",

"""
_______
|/      |
|      (_)
|      \|/
|       |
|
|
_|___
""",

"""
_______
|/      |
|      (_)
|      \|
|       |
|
|
_|___
""",

"""
_______
|/      |
|      (_)
|       |
|       |
|
|
_|___
""",

"""
_______
|/      |
|      (_)
|
|
|
|
_|___
""",

"""
_______
|/      |
|
|
|
|
|
_|___
"""
]

# Word list for the game
word_list = ("aardvark", "baboon", "camel")

# Initialize game variables
lives = 6  # Player starts with 6 lives
chosen_word = random.choice(word_list)  # Randomly select a word
print(chosen_word)  # For testing - remove this in production!

# Create placeholder with underscores
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Game state variables
game_over = False
correct_letter = []  # Track correctly guessed letters

# Main game loop
while not game_over:
    guess = input("Guess a letter: ").lower()
    
    # Build the display string
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    
    print(display)
    
    # Check if guess was wrong
    if guess not in chosen_word:
        lives -= 1  # Reduce lives
        if lives == 0:
            game_over = True
            print("You lose!")
    
    # Check if player won
    if "_" not in display:
        game_over = True
        print("You win!")
    
    # Display current hangman stage
    print(HANGMAN_STAGES[lives])
