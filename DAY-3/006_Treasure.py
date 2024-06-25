"""
Aim: Treasure Island


Author: Mehdiali
Date: 08 / June / 2024 - 01:05 PM
"""


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are at a Cross Road.")
while True:
    crossRoad = input("""Where do you want to go? "right" or "left" = """).lower()
    
    if (crossRoad == "right" or crossRoad == "left"):
        break
    else:
        print("\nPlease enter the correct choice.")

if (crossRoad == "right"):
    print("\nYou fall into a hole.")
else:
    print("\nNow you are at a Lake. There is a Island middle of the lake.")
    while True:
        lake = input("""Type "wait" to wait for a boat. Type "swim" to swim across. = """).lower()
        if (lake == "wait" or lake == "swim"):
            break
        else:
            print("\nPlease enter the correct choice.")

    if (lake == "swim"):
        print("\nYou got an Attack by trout.")
    else:
        print("""\nYou arrived at the Island of unharmed. There is a house of three doors. One "red", one "yellow", and one "blue".""")
        while True:
            door = input("""Which color do you choose = """).lower()

            if (door == "red" or door == "yellow" or door == "blue"):
                break
            else:
                print("\nPlease enter the correct choice.")
        
        if (door == "red"):
            print("\nThere is fire!!!\nYou were burned by fire.")
        elif (door == "blue"):
            print("\nThere are Beasts!!!\nYou were eaten by beasts.")
        else:
            print("\nWOW!!! Treasure. You got that.\nYou win.")
        
print("\n~~ Game OVER ~~")
    

