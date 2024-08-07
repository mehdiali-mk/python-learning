"""
Aim: Pomodoro App
Author: Mehdiali
Date: 02 / July / 2024 - 05:44 PM
"""

from tkinter import *
from getDate import todayDate
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
YELLOW = "#DE8E0C"
BLUE = "#191840"
FONT_NAME = "Gilroy"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 0.220
laps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def resetTimer():
    myScreen.after_cancel(timer)
    myCanvas.itemconfig(timerText, text="00:00")
    currentState.config(text="Start The Timer.")
    tickLabel.config(text="")
    global laps
    laps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def setTimer():
    global laps
    laps += 1
    workCount = WORK_MIN * 60
    shortBreakCount = SHORT_BREAK_MIN * 60
    longBreakCount = LONG_BREAK_MIN * 20

    if laps % 8 == 0:
        countDown(longBreakCount)
        currentState.config(text="Break")
    elif (laps % 2 == 0):
        countDown(shortBreakCount)
        currentState.config(text="Break")
    else:
        countDown(workCount)
        currentState.config(text="Work")

        marks = ""
        numberOfSessons = math.floor(laps / 2)
        for _ in range(numberOfSessons):
            marks += "✔"
        
        tickLabel.config(text=marks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countDown(count):
    global timer
    countMin = math.floor(count / 60)
    countSec = count % 60

    if (countSec < 10):
        countSec = f"0{countSec}"
    if (countMin < 10):
        countMin = f"0{countMin}"

    myCanvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if (count > 0):
        timer = myScreen.after(1000, countDown, count - 1)
    else:
        setTimer()

# ---------------------------- UI SETUP ------------------------------- #

myScreen = Tk()
myScreen.title("Pomodoro App")
myScreen.config(padx=120, pady=120, bg=BLUE)

myCanvas = Canvas(width=600,height=600, bg=BLUE, highlightthickness=0)
myImage = PhotoImage(file="DAY-28/alaram-min-new.png")
myCanvas.create_image(300, 300, image=myImage)
timerText = myCanvas.create_text(300, 325, text="00:00", fill=BLUE, font=(FONT_NAME, 42, "bold"))
myCanvas.grid(column=1, row=1)

dateLabel = Label(text=todayDate, foreground="white", bg=BLUE, font=(FONT_NAME, 20, "bold"))
dateLabel.grid(column=1, row=0)

tickLabel = Label(text="", fg=YELLOW, bg=BLUE, font=(FONT_NAME, 34, "bold"))
tickLabel.grid(column=1, row=3)

blankLabel = Label(text="",bg=BLUE )
blankLabel.grid(row=4, column=1)

startBtn = Button(text="START", bg=YELLOW, fg=BLUE, font=(FONT_NAME, 16, "bold"), padx=16, pady=8, highlightthickness=0, command=setTimer)
startBtn.grid(column=0, row=2, columnspan=1)

currentState = Label(text="Start The Timer.", bg=BLUE, fg="white", font=(FONT_NAME, 20, "bold"), highlightthickness=0)
currentState.grid(column=1, row=2)

resetBtn = Button(text="RESET", bg=YELLOW, fg=BLUE, font=(FONT_NAME, 16, "bold"), padx=16, pady=8, highlightthickness=0, command=resetTimer)
resetBtn.grid(column=2, row=2)

myScreen.mainloop()

