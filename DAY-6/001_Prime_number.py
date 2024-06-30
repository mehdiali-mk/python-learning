"""
Aim: Find the given number is prime or not.
Author: Mehdiali
Date: 11 / June / 2024 - 06:31 PM
"""

def isPrime(num):
    if (num == 1):
        return False
    else:
        for count in range(2, int(num**0.5) + 1):
            if (num % count == 0):
                return False
        return True

number = int(input("Enter the number = "))
if (isPrime(number)):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")