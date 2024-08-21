import datetime as dt
import smtplib
import random

today = dt.datetime.now()
todayDay = today.weekday()

def extractQuotes():
    with open("DAY-32/quotes.txt") as file:
        quotesData = file.read()
    quotesList = quotesData.split("\n")
    myQuotes = []

    for quote in quotesList:
        myQuoteList = quote.split(" - ")
        myQuoteDict = {
            "Quote": myQuoteList[0], 
            "Author": myQuoteList[1]
        }
        myQuotes.append(myQuoteDict)
    return random.choice(myQuotes)

if todayDay == 2:
    todayQuote = extractQuotes()
    print(todayQuote)

    senderUsername = "mehdialikadiwala@gmail.com"
    receiverUsername = "ahesan.agk@gmail.com"
    senderAppPassword = "hajddzlckyvvktzm"

    connection = smtplib.SMTP("smtp.gmail.com:587")
    connection.starttls()
    connection.login(user=senderUsername, password=senderAppPassword)
    connection.sendmail(
        from_addr=senderUsername,
        to_addrs=receiverUsername,
        msg=f"Subject:Monday Motivation by {todayQuote["Author"]}.\n\nHello, today is a monday as we promised we are providing you with the motivation quote.\n\n{todayQuote["Quote"]}\n--{todayQuote["Author"]}"
    )
    connection.close()




