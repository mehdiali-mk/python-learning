"""
Aim:

- Define a Circle class to create a circle with radius r using the constructor.

- Define an Area() method of the class which calculates the area of the circle.

- Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

Author: Mehdiali
Date: 04 / June / 2024 - 01:15 PM
"""

class Circle:

    __valueOfPI = 3.14

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.__valueOfPI * self.radius ** 2
    
    @property
    def perimeter(self):
        return 2 * self.__valueOfPI * self.radius
    

circle1 = Circle(4)
print("The area of circle = ", circle1.area)
print("The perimeter of circle = ", circle1.perimeter)

circle1.radius = 8
print("The area of circle = ", circle1.area)
print("The perimeter of circle = ", circle1.perimeter)
