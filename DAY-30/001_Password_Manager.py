"""
Aim: Password Manager App.
Author: Mehdiali
Date: 04 / July / 2024 - 05:42 PM
"""
from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json

# Constants
FONTS = "Montserrat"
DARK = "#222831"
GRAY = "#393E46"
CYAN = "#00FFF5"

# Save the data into the file.
def save():
    
    websiteName = websiteEntry.get()
    username = usernameEntry.get()
    password = passwordEntry.get()

    newData = {websiteName: {
        "email": username,
        "password": password
    }}

    if (websiteName == "" or username == "" or password == ""):
        messagebox.showwarning(title="Empty Field", message="Please enter the valid entries.")
    else:
        try:
            with open("DAY-30\data.json", "r") as dataFile:
                data = json.load(dataFile)
        except FileNotFoundError:
            with open("DAY-30\data.json", "w") as dataFile:
                json.dump(newData, dataFile, indent=4)
        else:
            data.update(newData)

            with open("DAY-30\data.json", "w") as dataFile:
                json.dump(data, dataFile, indent=4)
        finally:    
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)
            usernameEntry.delete(0, END)
            usernameEntry.insert(0, "mehdialikadiwala@gmail.com")


# Generate Random Password.

def generatePassword():

    alphabetsList = [letter for letter in string.ascii_uppercase + string.ascii_lowercase]
    digitsList = [digit for digit in string.digits]
    symbolsList = [symbol for symbol in string.punctuation]

    passwordLetters = [random.choice(alphabetsList) for _ in range(random.randint(8,10))]
    passwordDigits = [random.choice(digitsList) for _ in range(random.randint(2,4))]
    passwordSymbols = [random.choice(symbolsList) for _ in range(random.randint(2, 4))]

    newPassword = passwordLetters + passwordDigits + passwordSymbols
    random.shuffle(newPassword)

    passwordGenerated = "".join(newPassword)

    passwordEntry.delete(0, END)
    passwordEntry.insert(0, passwordGenerated)

    pyperclip.copy(passwordGenerated)


def searchPassword():

    websiteName = websiteEntry.get()
    try:
        with open("DAY-30\data.json", "r") as dataFile:
            data = json.load(dataFile)
    except FileNotFoundError:
        messagebox.showwarning(title="File Not Found", message=f"The main directory file doesn't exists.")
    else:
        if websiteName in data:
            email = data[websiteName]["email"]
            password = data[websiteName]["password"]

            messagebox.showinfo(title=websiteName, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="No Data Found!", message=f"Sorry! there is no data about {websiteName}.")










myScreen = Tk()
myScreen.title("Password Manager")
myScreen.config(padx=50, pady=50, bg=DARK)

myCanvas = Canvas(width=250,height=300, bg=DARK, highlightthickness=0)
myImage = PhotoImage(file="DAY-29/lock-01.png")
myCanvas.create_image(150, 120, image=myImage)
myCanvas.grid(row=0, column=0, columnspan=4)

websiteLabel = Label(text="Website:", font=(FONTS, 16, "bold"), bg=DARK, fg=CYAN)
websiteLabel.grid(row=1, column=0)

websiteEntry = Entry(width=25, highlightbackground=CYAN, highlightthickness=2, background=GRAY, fg=CYAN)
websiteEntry.grid(row=1, column=1)
websiteEntry.focus()

searchBtn = Button(text="Search", bg=GRAY, highlightbackground=CYAN, command=searchPassword, highlightthickness=2, fg=CYAN, width=8)
searchBtn.grid(row=1, column=2)

usernameLabel = Label(text="Email/Username:", font=(FONTS, 16, "bold"), bg=DARK, fg=CYAN)
usernameLabel.grid(row=2, column=0)

usernameEntry = Entry(width=35, highlightbackground=CYAN, highlightthickness=2, background=GRAY, fg=CYAN)
usernameEntry.grid(row=2, column=1, columnspan=4)
usernameEntry.insert(0, "mehdialikadiwala@gmail.com")

passwordLabel = Label(text="Password:", font=(FONTS, 16, "bold"), bg=DARK, fg=CYAN, width=16)
passwordLabel.grid(row=3, column=0)

passwordEntry = Entry(width=25, highlightbackground=CYAN, highlightthickness=2, background=GRAY, fg=CYAN)
passwordEntry.grid(row=3, column=1)

generatePasswordBtn = Button(text="Generate", command=generatePassword, bg=GRAY, highlightbackground=CYAN, highlightthickness=2, fg=CYAN)
generatePasswordBtn.grid(row=3, column=2)


addBtn = Button(text="Add", width=36, command=save, bg= CYAN, fg=DARK)
addBtn.grid(row=4, column=1, columnspan=2)


myScreen.mainloop()