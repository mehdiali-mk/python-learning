"""
AIM: Class & Objects
Author: Mehdiali
Date: 03 / June / 2024 - 03:00 PM
"""

class Student:
    collegeName = "LJ Polytechnic"

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName + " " + lastName
        print("students is added successfully...,", self.fullName)
    
    def welcomeMessage(self):
        print("Welcome to", self.collegeName, self.fullName)
    
    def inputMarks(self, marksOfMaths, marksofScience, marksOfEnglish):
        self.marksOfMaths = marksOfMaths
        self.marksOfScience = marksofScience
        self.marksOfEnglish = marksOfEnglish
        self.findTotalAverage(self.marksOfMaths, self.marksOfScience, self.marksOfEnglish)
        
    
    def findTotalAverage(self, marks1, marks2, marks3):
        self.totalMarks = marks1 + marks2 + marks3
        self.averageMarks = self.totalMarks / 3


print("\nFor Student1\n")
s1 = Student("Mehdiali", "Kadiwala")
print("fullName =", s1.fullName)
print("Collage Name =", s1.collegeName)
s1.welcomeMessage()
s1.inputMarks(98,97,96)
print("Total =", s1.totalMarks, "/ 300")
print("Average =", s1.averageMarks)

print("\nFor Student2\n")
s2 = Student("Aayan", "Mansuri")
print("fullName =", s2.firstName, s2.lastName)
print("Collage Name =", Student.collegeName)
s2.welcomeMessage()
s2.inputMarks(77,82,91)
print("Total =", s2.totalMarks, "/ 300")
print("Average =", s2.averageMarks)
