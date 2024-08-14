import smtplib

senderUsername = "mehdialikadiwala@gmail.com"
receiverUsername = "ahesan.agk@gmail.com"
senderAppPassword = "hajddzlckyvvktzm"

connection = smtplib.SMTP("smtp.gmail.com:587")
connection.starttls()
connection.login(user=senderUsername, password=senderAppPassword)
connection.sendmail(
    from_addr=senderUsername,
    to_addrs=receiverUsername,
    msg="Subject:About the EVA project.\n\nHello, Tomorrow we have to submit the assignment for EVA sessions."
)
connection.close()
print("\n\nEmail Sent Successfully!!\n\n")










# import smtplib

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second
# dayOfWeek = now.weekday()

# print(f"{year},{month},{day},{dayOfWeek}\n{hour}:{minute}:{second}")

# birthDay = dt.datetime(year=2007, month=8, day=30, hour=7, minute=30, second=20)

# print(birthDay)