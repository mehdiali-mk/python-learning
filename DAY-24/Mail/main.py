"""
Aim: Mail Merge.
Author: Mehdiali
Date: 28 / June / 2024 - 05:02 PM
"""

import os
# Shutil is a module to remove the tree folder which contains some other files.
import shutil
candidateNames = []

with open("DAY-24/Mail/input/Names/candidate_names.txt", "r") as fileOfNames:
    names = fileOfNames.readlines()

    for name in names:
        name = name.replace("\n", "")
        candidateNames.append(name)

shutil.rmtree("DAY-24/Mail/output")
os.mkdir("DAY-24/Mail/output")

with open("DAY-24/Mail/input/Common/mail.txt", "r") as commonMailFile:
    commonMail = commonMailFile.read()
    
    for name in candidateNames:
        mailWithName = commonMail.replace("{name}", name)
        with open(f"DAY-24/Mail/output/{name}.txt", "w") as mailFile:
            mailFile.write(mailWithName)
    
print(candidateNames)