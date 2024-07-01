"""
Aim: Ceasar Ciphar Message Encoding and Decoding Machine.
Author: Mehdiali
Date: 12 / June / 2024 - 03:12 PM
"""

import string
import os

# Funtions to Implement logic

def convertStingToList(myString):
    myList = []
    for count in range(0, len(myString)):
        myList.append(myString[count])
    
    return myList

def convertListToString(myList):
    myString = ""
    for element in myList:
        myString += element
    
    return myString

def encodeTheMessage(messageToOperate, numberToShift):
    messageToOperateList = convertStingToList(messageToOperate)
    encodedMessage = []
    for messageLetter in messageToOperateList:
        found = alphabetsLetters.find(messageLetter)
        newIndex = found + numberToShift
        encodedMessage.append(alphabetsList[newIndex])
    
    encodedMessage = convertListToString(encodedMessage)
    print(f"\nThe encoded message = {encodedMessage}")
    messageInfo.append(encodedMessage)

def decodeTheMessage(messageToOperate, numberToShift):
    messageToOperateList = convertStingToList(messageToOperate)
    decodedMessage = []
    for messageLetter in messageToOperateList:
        found = alphabetsLetters.find(messageLetter)
        newIndex = found - numberToShift
        decodedMessage.append(alphabetsList[newIndex])
    
    decodedMessage = convertListToString(decodedMessage)
    print(f"\nThe encoded message = {decodedMessage}")
    messageInfo.append(decodedMessage)

        

alphabetsLetters = string.ascii_lowercase + string.ascii_uppercase
alphabetsList = convertStingToList(alphabetsLetters)

os.system("cls")
print("Welcome, to the Ceasar Ciphar Machine.")

# Store the information of the message.
messageInfo = []

while True:    
    while True:
        actionToDo = input("""Type "encode" to encrypt, and "decode" to decrypt = """).lower()

        if (actionToDo == "encode" or actionToDo == "decode"):
            break
        else:
            print("\nPlease enter the correct choice.")

    messageToOperate = input("\nEnter your message = ")
    numberToShift = int(input("Enter the shift number = "))
    
    messageInfo.append(numberToShift)
    if (actionToDo == "encode"):
        messageInfo.append(messageToOperate)
        encodeTheMessage(messageToOperate, numberToShift)
    else:
        decodeTheMessage(messageToOperate, numberToShift)
        messageInfo.append(messageToOperate)


    while True:
        repeatOrNot = input("\nPerform another task? (Y / N) = ").lower()

        if (repeatOrNot == "y" or repeatOrNot == "n"):
            break
        else:
            print("\nPlease enter the correct choice.")
    
    if (repeatOrNot == "n"):
        break
    else:
        os.system("cls")
        print("\nYour pervious message:")
        for index in range(0, len(messageInfo), 3):
            print(f"Encoded = {messageInfo[index + 1]}, Decoded = {messageInfo[index + 2]}, Shift = {messageInfo[index]}")
        print("\n")

