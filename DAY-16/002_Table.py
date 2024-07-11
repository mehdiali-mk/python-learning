"""
Aim: PrettyTable Class and its Objects.
Author: Mehdiali
Date: 20 / June / 2024 - 03:42 PM
"""
# Please refer the official doctumentation of pretty table on: https://pypi.org/project/prettytable/


from prettytable import PrettyTable
from os import system
system("cls")

studentTable = PrettyTable()

studentTable.add_column("Student Name", ["Mehdiali", "Man Patel", "Aayan Mansuri", "Nityam Mehta", "Kazi Aman", "Abbas Haider"])
studentTable.add_column("Mobile Number", [7531594560, 4567891235, 9876543215, 6575497865, None, 1234566546])

studentTable.align = "l"
studentTable.padding_width = 1

print(studentTable)

# print(studentTable.get_html_string(attributes = {"id":"myTable", "class":"red-table"}))