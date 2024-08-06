"""
Aim: Miles to Kilometers by Tkinter.
Author: Mehdiali
Date: 01 / July / 2024 - 10:31 PM
"""

from tkinter import *

myScreen = Tk()
myScreen.minsize(width=450, height=250)
myScreen.title("Miles to km")
myScreen.config(padx=40, pady=40)

FONTS = ("Arial", 20, "bold")

userInput = Entry(font=FONTS)
userInput.grid(column=1, row=0)

milesLabel = Label(text="Miles", font=FONTS)
milesLabel.grid(column=2, row=0)

isEqualToLabel = Label(text="is equal to", font=FONTS)
isEqualToLabel.grid(column=0, row=1)

kmResultLabel = Label(text="0", font=FONTS)
kmResultLabel.grid(column=1, row=1)

kmLabel = Label(text="Km", font=FONTS)
kmLabel.grid(column=2, row=1)

def calculateKm():
    miles = userInput.get()
    km = float(miles) * 1.609344

    kmResultLabel.config(text=round(km, 2))

calculateBtn = Button(text="Calculate", command=calculateKm, font=FONTS)
calculateBtn.grid(column=1, row=2)

myScreen.mainloop()