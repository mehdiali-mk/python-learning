"""
Aim: Key Words Arguments (**kwargs) Intro.
Author: Mehdiali
Date: 01 / July / 2024 - 06:13 PM
"""


def calculate(n, **kwargs):

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(2, add=3, multiply=5)