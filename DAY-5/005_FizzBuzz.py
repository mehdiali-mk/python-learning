"""
Aim: Fizz Buzz
Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz" = "F".
When the number is divisible by 5 then instead of printing the number it should print "Buzz" = "B".
When the number is divisible by both 5 and 3 then instead of printing the number it should print "FizzBuzz" = "FB".

Author: Mehdiali
Date: 10 / June / 2024 - 06:53 PM
"""

for number in range(1, 101):
    if (number % 3 == 0 and number % 5 == 0):
        print("FB", end="\t")
    elif (number % 3 == 0):
        print("F", end="\t")
    elif (number % 5 == 0):
        print("B", end="\t")
    else:
        print(number, end="\t")
    
    if (number % 10 == 0):
        print("\n")
