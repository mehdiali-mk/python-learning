"""
Aim: Quiz App
Author: Mehdiali
Date: 21 / June / 2024 - 05:00 PM
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

# Here we are adding the questionData into questionBank as Object.
questionBank = []

for count in range(0, len(question_data)):
    questionBank.append(Question(question_data[count]["text"], question_data[count]["answer"]))

quiz = QuizBrain(questionBank)

os.system("cls")
while quiz.stillHasQuestion():
    quiz.nextQuestion()
    

print("\nYou have completed the quiz.")
print(f"Your final score is: {quiz.score} / {quiz.questionNumber}")