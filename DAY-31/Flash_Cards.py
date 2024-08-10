"""
Aim: Flash Cards App.
Author: Mehdiali
Date: 23 / July / 2024 - 07:03 PM
"""
BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
import random
from tkinter import *


try:
    data = pd.read_csv("DAY-31/data/WordsToLearn.csv")

except FileNotFoundError:
    orgData = pd.read_csv("DAY-31/data/Words.csv")
    wordsList = orgData.to_dict(orient="records")
else:
    wordsList = data.to_dict(orient="records")

currentCard = {}

def nextCard():
    global currentCard, flipTimer
    myWindow.after_cancel(flipTimer)
    currentCard = random.choice(wordsList)
    myCanvas.itemconfig(cardTitle, text="Hindi", fill="black")
    myCanvas.itemconfig(cardWord, text=f"{currentCard["Hindi"]}", fill="black")
    myCanvas.itemconfig(cardBackgroundImage, image=cardFrontImage)
    flipTimer = myWindow.after(3000, func=flipCard)

def flipCard():
    myCanvas.itemconfig(cardTitle, text="English", fill="white")
    myCanvas.itemconfig(cardWord, text=f"{currentCard["English"]}", fill="white")
    myCanvas.itemconfig(cardBackgroundImage, image=cardBackImage)

def isKnown():
    wordsList.remove(currentCard)
    data = pd.DataFrame(wordsList)
    data.to_csv("DAY-31\data\WordsToLearn.csv", index=False)

    nextCard()

myWindow = Tk()
myWindow.title("Flash Cards")
myWindow.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flipTimer = myWindow.after(3000, func=flipCard)

myCanvas = Canvas(width=800, height=526)

cardFrontImage = PhotoImage(file="DAY-31/images/card_front.png")
cardBackImage = PhotoImage(file="DAY-31/images/card_back.png")
cardBackgroundImage = myCanvas.create_image(400, 263, image=cardFrontImage)
cardTitle = myCanvas.create_text(400, 150,text="", font=("Arial", 40, "italic"))
cardWord = myCanvas.create_text(400, 263,text=f"", font=("Arial", 60, "bold"))

myCanvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
myCanvas.grid(row=0, column=0, columnspan=2)

crossImage = PhotoImage(file="DAY-31/images/wrong.png")
crossButton = Button(image=crossImage, highlightthickness=0, bg=BACKGROUND_COLOR, cursor="dot", command=nextCard)
crossButton.grid(row=1, column=0)

checkImage = PhotoImage(file="DAY-31/images/right.png")
checkButton = Button(image=checkImage, highlightthickness=0, bg=BACKGROUND_COLOR, cursor="dot", command=isKnown)
checkButton.grid(row=1, column=1)

nextCard()
myWindow.mainloop()
