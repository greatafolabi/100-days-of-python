# Blind Auction Program
import os

# ASCII art logo (optional)
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the Blind Auction!")

# Dictionary to store all bids
bids = {}

def add_bid(name, bid_amount):
    """Add a new bid to the dictionary"""
    bids[name] = bid_amount

def find_highest_bidder(bidding_record):
    """Find and announce the winner"""
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}!")

# Main auction loop
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    
    # Add bid to dictionary
    add_bid(name, price)
    
    # Ask if there are more bidders
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    if more_bidders == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif more_bidders == "yes":
        # Clear screen for next bidder (keep bids secret!)
        os.system('clear')  # Mac/Linux
        # os.system('cls')  # Windows
