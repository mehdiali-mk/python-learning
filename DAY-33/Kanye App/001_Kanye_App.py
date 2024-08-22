import requests
from tkinter import *


def getQuote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()

    quote = data["quote"]
    myCanvas.itemconfig(quoteText, text=quote)


myWindow = Tk()
myWindow.title("Kanye App")
myWindow.config(padx=50, pady=50)

myCanvas = Canvas(width=300, height=414)
backgroundImage = PhotoImage(file="DAY-33/Kanye App/background.png")
myCanvas.create_image(150, 207, image=backgroundImage)
quoteText = myCanvas.create_text(150, 207, text="Kanye Quotes goes here...", width=250, font=("Arial", 18, "bold"))
myCanvas.grid(row=0,column=0)


kanyeImage = PhotoImage(file="DAY-33/Kanye App/kanye.png")
kanyeButton = Button(image=kanyeImage, highlightthickness=0, command=getQuote)
kanyeButton.grid(row=1, column=0)


myWindow.mainloop()
