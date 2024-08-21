##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



import datetime as dt
import pandas as pd
import smtplib
import random

todayDate = dt.datetime.now()
currentMonth = todayDate.month
currentDay = todayDate.day

senderAddress = "mehdialikadiwala@gmail.com"
senderAppPassword = "hajddzlckyvvktzm"

data = pd.read_csv("DAY-32/Birthday Wisher/birthdays.csv")
monthList = list(data["month"])
dayList = list(data["day"])
nameList = list(data["name"])
emailList = list(data["email"])

indexOfReceiver = []

for count in range(0,len(monthList)):
    if currentMonth == monthList[count] and currentDay == dayList[count]:
        indexOfReceiver.append(count)

for index in indexOfReceiver:
    numberOfLetter = random.randint(1,3)
    with open(f"DAY-32/Birthday Wisher/letter_templates/letter_{numberOfLetter}.txt") as file:
        letterData = file.read()

    letterData = letterData.replace("[NAME]",str(nameList[index]))
    
    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(user=senderAddress, password=senderAppPassword)
        connection.sendmail(
            from_addr=senderAddress,
            to_addrs=emailList[index],
            msg=f"Subject:Happy Birthday!!\n\n{letterData}"
        )