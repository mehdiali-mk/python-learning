"""
Aim: Tkinter Introduction
Author: Mehdiali
Date: 01 / July / 2024 - 05:48 PM
"""

from tkinter import *

myWindow = Tk()
myWindow.title("Tkinter Introduction")
myWindow.minsize(width=800, height=500)

myLabel = Label(text="This is a label.", font=("Arial", 24, "bold"))
myLabel.pack()

myLabel.config(text="New Text")

def btnClicked():
    userInput = myInput.get()
    myLabel.config(text=userInput)
    myButton.config(bg="Yellow")

myButton = Button(text="Click Me!", command=btnClicked)
myButton.pack()


myInput = Entry()
myInput.pack()

myWindow.mainloop()
