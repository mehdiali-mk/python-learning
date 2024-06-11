"""
AIM: File I/O Operations
Author: Mehdiali
Date: 02 / June / 2024 - 03:36 PM
"""

file = open("Programs\demo1.txt", "r")

'''
data = file.read()

print(data)
'''

line1 = file.readline()
line2 = file.readline()

print(f"\n\n{line1}", end="")
print(line2)

file.close()


# Write Mode.
newFile = open("Programs\demo1.txt", "w")

newFile.write("I will read books tomorrow.")

newFile.close()

# Append Mode.
newFile = open("Programs\demo1.txt", "a")

newFile.write("\nBut tomorrow I will be very busy.")

newFile.close()