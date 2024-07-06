"""
Aim: Blackjack Game.
Author: Mehdiali
Date: 14 / June / 2024 - 07:08 PM
"""

import os
import random

os.system("cls")
# Here is the list of cards.
cardsList = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Here is the function to add the new card to game.
def getCard(index):
    """It takes the index and return the value from the list."""
    return cardsList[index]

# Here is the function to find the score.
def calculateScore(cardList):
    """It takes the list of card and return the sum of the values."""
    score = 0
    for card in cardList:
        score += card
    
    return score

# Here is the function to display the cards in formatted form.
def displayCard(cardList, score):
    print("[ ", end="")
    for card in cardList:
        print(card, end=" ")
    print(f"], score = {score}")


# Taking the user choice to play the game.
while True:
    start = input("\nDo you want to play the Blackjack game? (Y/N) = ").lower()

    if (start == "y" or start == "n"):
        break
    else:
        print("\nPlease choose the correct choice.")

if (start == "n"):
    exit()

userCard = []
computerCard = []

userCard.append(getCard(random.randint(0, len(cardsList) - 1)))
userCard.append(getCard(random.randint(0, len(cardsList) - 1)))

computerCard.append(getCard(random.randint(0, len(cardsList) - 1)))
computerCard.append(getCard(random.randint(0, len(cardsList) - 1)))


while True:
    userScore = calculateScore(userCard)
    computerScore = calculateScore(computerCard)

    print("\nYour cards = ", end="")
    displayCard(userCard, userScore)
    print(f"Computer's cards = [ {computerCard[0]} ]")

    if (userScore == 21 and len(userCard) == 2):
        print("\nYour are the Winner.")
        exit()
    elif (computerScore == 21  and len(computerCard) == 2):
        print("\nComputer Win\nYou loose.")
        exit()

    if (userScore > 21):
        if userCard.count(11) > 0:
            index = userCard.index(11)
            userCard[index] = 1
            userScore = calculateScore(userCard)
            
            print("\nYour new cards = ", end="")
            displayCard(userCard, userScore)
            
            if (userScore > 21):
                print("\nComputer Win\nYou loose.")
                exit()
            else:
                pass
        else:
            print("\nComputer Win\nYou loose.")
            exit()


    if (userScore <= 21):
        while True:
            repeat = input("Do you want to take another card? (Y/N) = ").lower()

            if (repeat == "y" or repeat == "n"):
                break
            else:
                print("\nPlease choose the correct choice.")
        if (repeat == "y"):
            userCard.append(getCard(random.randint(0, len(cardsList) - 1)))
        else:
            break

while computerScore < 16:
    computerCard.append(getCard(random.randint(0, len(cardsList) - 1)))
    computerScore = calculateScore(computerCard)


if (computerScore > 21):
    print("\nYour are the Winner.")
    exit()

if (userScore == computerScore):
    print("\nIt's Draw!")
    exit()
elif (userScore > computerScore):
    print("\nYour are the Winner.")
    exit()
elif (userScore < computerScore):
    print("\nComputer Win\nYou loose.")
    exit()
