from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#191825"
FONT_NAME = "Montserrat"

"""
THEME_COLOR = "#375362"
FONT_NAME = "Montserrat"

class quizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.myWindow = Tk()
        self.myWindow.title("Quiz App")
        self.myWindow.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreLabel = Label(text="Score: 0", fg="White", bg=THEME_COLOR, font=(FONT_NAME, 14, "bold"))
        self.scoreLabel.grid(row=0, column=1)

        self.myCanvas = Canvas(width=300, height=250, bg="White")
        self.questionText = self.myCanvas.create_text(150, 125,text="Question text goes here...Question text goes here...Question text goes here...", fill=THEME_COLOR, font=(FONT_NAME, 16, "bold italic"), width=280)
        self.myCanvas.grid(row=1, column=0, columnspan=2, pady=50)

        trueImage = PhotoImage(file="DAY-34/Quiz App/images/true.png")
        self.trueButton = Button(image=trueImage, highlightthickness=0, command=self.trueButtonPressed)
        self.trueButton.grid(row=2, column=1)

        falseImage = PhotoImage(file="DAY-34/Quiz App/images/false.png")
        self.falseButton = Button(image=falseImage, highlightthickness=0, command=self.falseButtonPressed)
        self.falseButton.grid(row=2, column=0)

        self.getNextQuestion()

        self.myWindow.mainloop()


    def getNextQuestion(self):
        self.myCanvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.scoreLabel.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.myCanvas.itemconfig(self.questionText, text=question)
        else:
            self.myCanvas.itemconfig(self.questionText, text=f"You've reached the end of the quiz.\n\nYour final score = {self.quiz.score}")
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")
    
    def trueButtonPressed(self):
        self.giveFeedback(self.quiz.check_answer("True"))

    # Another way or wirting.
    def falseButtonPressed(self):
        self.giveFeedback(self.quiz.check_answer("False"))

    def giveFeedback(self, isRight):
        print(isRight)
        if isRight == True:
            self.myCanvas.config(bg="green")
        else:
            self.myCanvas.config(bg="red")
        
        # self.myWindow.after(1000, self.getNextQuestion)
        self.getNextQuestion()
"""

class quizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.myWindow = Tk()
        self.myWindow.title("Quiz App")
        self.myWindow.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreLabel = Label(text="Score: 0", fg="White", bg=THEME_COLOR, font=(FONT_NAME, 14, "bold"))
        self.scoreLabel.grid(row=0, column=1)

        self.myCanvas = Canvas(width=300, height=250, bg="White")
        self.questionText = self.myCanvas.create_text(150, 125,text="Question text goes here...Question text goes here...Question text goes here...", fill=THEME_COLOR, font=(FONT_NAME, 16, "bold italic"), width=280)
        self.myCanvas.grid(row=1, column=0, columnspan=2, pady=50)

        trueImage = PhotoImage(file="DAY-34/Quiz App/images/true.png")
        self.trueButton = Button(image=trueImage, highlightthickness=0, command=self.trueButtonPressed)
        self.trueButton.grid(row=2, column=1)

        falseImage = PhotoImage(file="DAY-34/Quiz App/images/false.png")
        self.falseButton = Button(image=falseImage, highlightthickness=0, command=self.falseButtonPressed)
        self.falseButton.grid(row=2, column=0)

        self.getNextQuestion()

        self.myWindow.mainloop()


    def getNextQuestion(self):
        self.myCanvas.config(bg="White")
        self.myCanvas.itemconfig(self.questionText, fill="black")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.myCanvas.itemconfig(self.questionText, text=question)
        else:
            self.myCanvas.itemconfig(self.questionText, text=f"You've reached the end of the quiz.\n\nYour final score = {self.quiz.score}")
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")

        self.scoreLabel.config(text=f"Score: {self.quiz.score}")

    def trueButtonPressed(self):
        self.giveFeedback(self.quiz.check_answer("True"))

    # Another way or wirting.
    def falseButtonPressed(self):
        self.giveFeedback(self.quiz.check_answer("False"))

    def giveFeedback(self, isRight):
        print(isRight)
        if isRight == True:
            self.myCanvas.config(bg="green")
            pass
        else:
            self.myCanvas.config(bg="red")
            # self.myCanvas.itemconfig(self.questionText,fill="red")
        
        self.myWindow.after(500, self.getNextQuestion)
        # self.getNextQuestion()










