"""
Aim:

- Define an Employee class with attributes role, department & salary. This class has also showDetails() method.

Create an Engineer class that inherits properties from employee & has additional attributes: name & age.

Author: Mehdiali
Date: 04 / June / 2024 - 01:25 PM
"""

class Employee:

    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print("\nRole =", self.role, "\nDepartment =", self.department, "\nSalary =", self.salary)

class Engineer(Employee):

    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age
    
    def printDetails(self):
        print("\nName =", self.name, "\nAge =", self.age, end="")
        super().showDetails()

emp1 = Employee("Developer", "Software Development", 35000)
emp1.showDetails()

engin2 = Engineer("Mehdiali", 17, emp1.role, emp1.department, emp1.salary)

engin2.printDetails()