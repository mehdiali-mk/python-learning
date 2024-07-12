class QuizBrain:

    def __init__(self, questionList):
        self.questionNumber = 0
        self.questionList = questionList
        self.score = 0

    def nextQuestion(self):
        newQuestion = self.questionList[self.questionNumber]

        while True:
            userAnswer = input(f"Q.{self.questionNumber + 1}: {newQuestion.text}. (True/False)?: ").lower()

            if (userAnswer == "true" or userAnswer == "false"):
                break
            else:
                print("\nPlease enter the correct choice.")
        
        self.questionNumber += 1

        self.checkAnswer(userAnswer, newQuestion.answer)

    def stillHasQuestion(self):
        return self.questionNumber < len(self.questionList)
    
    def checkAnswer(self, userAnswer, correctAnswer):
        if (userAnswer.lower() == correctAnswer.lower()):
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
            print(f"The correct answer was: {correctAnswer}")
        
        print(f"Your current Score is: {self.score}/{self.questionNumber}\n\n")