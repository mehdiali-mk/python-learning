"""
Aim: Here is the program for blind auction.
Author: Mehdiali
Date: 13 / June / 2024 - 01:14 PM
"""

# Importing some modules.
import os
from Auction_Logo import (logo)
import msvcrt



# Empty dictionary for people name and bid.
peopleOfAuction = {}

# Functions to enter a new value in dictionary.
def addEntry(name, bid):
    peopleOfAuction[name] = bid

# Function to display winner.
def displayWinner():
    maxBid = 0
    person = ""
    for key in peopleOfAuction:
        bid = peopleOfAuction[key]
        if (bid > maxBid):
            maxBid = bid
            person = key

    print(f"\nThe winner is {person} with the bid amount of ₹{maxBid}.\n\n")

while True:
    # Welcome screen for user.
    os.system("cls")
    print(logo)
    print("\nWelcome to the blind auction program.\n")
    print("\nPress any key to continue...")
    msvcrt.getch()
    os.system("cls")


    name = input("\nEnter your name = ")
    bid = int(input("Enter your bid value = ₹"))

    addEntry(name, bid)

    while True:
        repeat = input("\nAre there any other bidders? (Y / N) = ").lower()
        if (repeat == "y" or repeat == "n"):
            break
        else:
            print("\nPlease choose the correct choice:", end = "")

    if (repeat == "n"):
        break

os.system("cls")
displayWinner()