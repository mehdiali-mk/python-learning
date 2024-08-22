import requests
import datetime as dt
import smtplib
import time

senderUsername = "mehdialikadiwala@gmail.com"
receiverUsername = "ahesan.agk@gmail.com"
senderAppPassword = "hajddzlckyvvktzm"

myLongitude = 72.523768
myLatitude = 22.993584

def isISSOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    issLatitude = float(data["iss_position"]["latitude"])
    issLongitude = float(data["iss_position"]["longitude"])

    if ((myLongitude - 5) <= issLongitude <= (myLongitude + 5)) and ((myLatitude - 5) <= issLatitude <= (myLatitude + 5)):
        return True


def isNight():
    parametersForAPI = {
        "lat": myLatitude,
        "lng": myLongitude,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parametersForAPI)
    response.raise_for_status()
    data = response.json()
    sunriseTime = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunsetTime = data["results"]["sunset"].split("T")[1].split(":")[0]

    todayTime = dt.datetime.now()

    if todayTime.hour >= sunsetTime and todayTime.hour <= sunriseTime:
        return True
    
while True:
    time.sleep(60)
    if (isISSOverhead() and isNight()):
        with smtplib.SMTP("smtp.gamil.com:587") as connection:
            connection.starttls()
            connection.login(user=senderUsername, password=senderAppPassword)
            connection.sendmail(
                from_addr=senderUsername,
                to_addrs=receiverUsername,
                msg="Subject:Look Up 👆👆\n\nThe ISS is above you in the sky."
            )
