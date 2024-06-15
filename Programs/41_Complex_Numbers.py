"""
Aim: Complex Number
Author: Mehdiali
Date: 04 / June / 2024 - 01:07 PM
"""

class Complex:

    def __init__(self, realNumber, imageNumber):
        self.realNumber = realNumber
        self.imageNumber = imageNumber
    
    def showNumber(self):
        print(self.realNumber, "+", self.imageNumber, end="")
        print("i")

    def __add__(self, newObj):
        newRealNumber = self.realNumber + newObj.realNumber
        newImageNumber = self.imageNumber + newObj.imageNumber

        return Complex(newRealNumber, newImageNumber)
    
    def __sub__(self, newObj):
        newRealNumber = self.realNumber - newObj.realNumber
        newImageNumber = self.imageNumber - newObj.imageNumber

        return Complex(newRealNumber, newImageNumber)

    
num1 = Complex(3, 6)
num2 = Complex(4, 5)

num1.showNumber()
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()