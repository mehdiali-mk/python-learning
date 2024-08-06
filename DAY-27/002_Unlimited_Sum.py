"""
Aim: Unlimited Arguments input to the function.
Author: Mehdiali
Date: 01 / July / 2024 - 06:00 PM
"""

def add(*args):
    print(f"The first arg: {args[0]}\nThe Last arg: {args[-1]}")
    numSum = 0
    for n in args:
        numSum += n
    
    return numSum

sumOfNum = add(1,2,3,4,5)

print(f"\n\n{sumOfNum}")