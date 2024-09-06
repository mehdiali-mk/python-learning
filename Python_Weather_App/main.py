# Import for the GUI
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
# Import for taking the Location of the user.
from geopy.geocoders import Nominatim
from geopy.geocoders import Photon
# Import for finding the timezone of the user.
from timezonefinder import TimezoneFinder
# Import for taking the today's date and time of user.
from datetime import *
# Import for requesting for the api of weather.
import requests
# 
import pytz
# Import for the Image manipulation and efficient representation of image, and powerfull image processing capabilities.
from PIL import Image, ImageTk



# Here is the getWeatherData function which was invoke by clicking on search button.
def getWeatherData():
    # Getting the city name written in the search bar.
    city = textField.get()
    # To make a geo locator to find the longitude and latitude.
    geoLocator = Nominatim(user_agent="Python_Weather_App")
    # To find the geoCode of the city entered in the search bar.
    # location = geoLocator.geocode(city)
    location = geoLocator.geocode("Ahmedabad")
    # Object to find the time zone according to the UTC+.
    obj = TimezoneFinder()

    # Here result stores the actual timezon according the location by longitude and latitude.
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    # Puting the result to the output screen through the timezone lable.
    timeZone.config(text=result)
    # Puting longitude and latittude to the output screen through the longLat Label.
    longLat.config(text=f"{round(location.longitude, 2)}°N,  {round(location.latitude,2)}°E")

    # Home is a user pin on the earth to find time.
    home = pytz.timezone(result)
    # Finding the local time of the user address
    localTime = datetime.now(home)
    # Formatting the current time of the user as 03:14 PM.
    # %I:returns Hours %M:returns Minutes %p:returns the time as PM and AM.
    currentTime = localTime.strftime("%I:%M %p")
    # Putting the current time on the screen through the clock label.
    clock.config(text=currentTime)


    # # Weather
    # Here is the API KEY
    APIKEY = "50f281806b06ecc7a08b9021c7be86ca"
    # Here is the API URL to pass as an request
    # apiURL = "https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid="+APIKEY
    # 7 Days API
    apiURL = "https://api.openweathermap.org/data/2.5/forecast?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid="+APIKEY

    print(apiURL)
    # Here we are requesting for APIURL to fetch data.
    jsonData = requests.get(apiURL).json()
    
    # Fetch data is assigned to individual variables.
    temp = jsonData['list'][0]['main']['temp']
    humidity = jsonData['list'][0]['main']['humidity']
    pressure = jsonData['list'][0]['main']['pressure']
    wind = jsonData['list'][0]['wind']['speed']
    description = jsonData['list'][0]['weather'][0]['description']

    # Storing the min and max temp of all days.
    minMaxOfAll = []
    minMaxOfAll.append({"tempMin": round(jsonData['list'][0]['main']['temp_min'] - 273.15, 1), "tempMax": round(jsonData['list'][4]['main']['temp_max']  - 273.15, 1)})
    minMaxOfAll.append({"tempMin": round(jsonData['list'][8]['main']['temp_min'] - 273.15), "tempMax": round(jsonData['list'][12]['main']['temp_max'] - 273.15)})
    minMaxOfAll.append({"tempMin": round(jsonData['list'][16]['main']['temp_min'] - 273.15), "tempMax": round(jsonData['list'][20]['main']['temp_max'] - 273.15)})
    minMaxOfAll.append({"tempMin": round(jsonData['list'][24]['main']['temp_min'] - 273.15), "tempMax": round(jsonData['list'][28]['main']['temp_max'] - 273.15)})
    minMaxOfAll.append({"tempMin": round(jsonData['list'][32]['main']['temp_min'] - 273.15), "tempMax": round(jsonData['list'][36]['main']['temp_max'] - 273.15)})
    minMaxOfAll.append({"tempMin": round(jsonData['list'][39]['main']['temp_min'] - 273.15), "tempMax": round(jsonData['list'][37]['main']['temp_max'] - 273.15)})
    minMaxOfAll.append({"tempMin": round(jsonData['list'][16]['main']['temp_min'] - 273.15), "tempMax": round(jsonData['list'][20]['main']['temp_max'] - 273.15)})

    # Converting if Min is Greater than Max.
    for element in minMaxOfAll:
        if element["tempMin"] > element["tempMax"]:
            newElement = element["tempMin"]
            element["tempMin"] = element["tempMax"]
            element["tempMax"] = newElement

    minMaxStr = [
        f"Min: {minMaxOfAll[0]["tempMin"]} ºC\nMax: {minMaxOfAll[0]['tempMax']} ºC",
        f"Min: {minMaxOfAll[1]["tempMin"]} ºC\nMax: {minMaxOfAll[1]['tempMax']} ºC",
        f"Min: {minMaxOfAll[2]["tempMin"]} ºC\nMax: {minMaxOfAll[2]['tempMax']} ºC",
        f"Min: {minMaxOfAll[3]["tempMin"]} ºC\nMax: {minMaxOfAll[3]['tempMax']} ºC",
        f"Min: {minMaxOfAll[4]["tempMin"]} ºC\nMax: {minMaxOfAll[4]['tempMax']} ºC",
        f"Min: {minMaxOfAll[5]["tempMin"]} ºC\nMax: {minMaxOfAll[5]['tempMax']} ºC",
        f"Min: {minMaxOfAll[6]["tempMin"]} ºC\nMax: {minMaxOfAll[6]['tempMax']} ºC",
    ]

    # Assigning the data to the actual label.
    t.config(text=(round(temp - 273.15), "ºC"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=(description))

    # First Cell
    firstDayImage = jsonData['list'][0]['weather'][0]['icon']

    img = (Image.open(f"Python_Weather_App\icon\{firstDayImage}@2x.png"))
    resizedImage = img.resize((75,75))
    photo1 = ImageTk.PhotoImage(resizedImage)
    firstImage.config(image=photo1)
    firstImage.image = photo1

    day1MinMax.config(text=minMaxStr[0])

    # Second Cell
    secondDayImage = jsonData['list'][8]['weather'][0]['icon']

    img = (Image.open(f"Python_Weather_App\icon\{secondDayImage}@2x.png"))
    resizedImage = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resizedImage)
    secondImage.config(image=photo2)
    secondImage.image = photo2
    
    day2MinMax.config(text=minMaxStr[1])

    # Third Cell
    thirdDayImage = jsonData['list'][16]['weather'][0]['icon']

    img = (Image.open(f"Python_Weather_App\icon\{thirdDayImage}@2x.png"))
    resizedImage = img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resizedImage)
    thirdImage.config(image=photo3)
    thirdImage.image = photo3

    day3MinMax.config(text=minMaxStr[2])

    # Fourth Cell
    fourthDayImage = jsonData['list'][24]['weather'][0]['icon']
    img = (Image.open(f"Python_Weather_App\icon\{fourthDayImage}@2x.png"))
    resizedImage = img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resizedImage)
    fourthImage.config(image=photo4)
    fourthImage.image = photo4

    day4MinMax.config(text=minMaxStr[3])

    # Fifth Cell
    fifthDayImage = jsonData['list'][32]['weather'][0]['icon']
    img = (Image.open(f"Python_Weather_App\icon\{fifthDayImage}@2x.png"))
    resizedImage = img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resizedImage)
    fifthImage.config(image=photo5)
    fifthImage.image = photo5

    day5MinMax.config(text=minMaxStr[4])

    # Sixth Cell
    sixthDayImage = jsonData['list'][39]['weather'][0]['icon']
    img = (Image.open(f"Python_Weather_App\icon\{sixthDayImage}@2x.png"))
    resizedImage = img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resizedImage)
    sixthImage.config(image=photo6)
    sixthImage.image = photo6

    day6MinMax.config(text=minMaxStr[5])

    # Seventh Cell
    seventhDayImage = jsonData['list'][16]['weather'][0]['icon']
    img = (Image.open(f"Python_Weather_App\icon\{seventhDayImage}@2x.png"))
    resizedImage = img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resizedImage)
    seventhImage.config(image=photo7)
    seventhImage.image = photo7

    day7MinMax.config(text=minMaxStr[6])

    # Days
    firstDay = datetime.now()
    day1.config(text=firstDay.strftime("%A"))

    secondDay = firstDay + timedelta(days=1)
    day2.config(text=secondDay.strftime("%A"))

    thirdDay = firstDay + timedelta(days=2)
    day3.config(text=thirdDay.strftime("%A"))

    fourthDay = firstDay + timedelta(days=3)
    day4.config(text=fourthDay.strftime("%A"))

    fifthDay = firstDay + timedelta(days=4)
    day5.config(text=fifthDay.strftime("%A"))

    sixthDay = firstDay + timedelta(days=5)
    day6.config(text=sixthDay.strftime("%A"))

    seventhDay = firstDay + timedelta(days=6)
    day7.config(text=seventhDay.strftime("%A"))

    


# This line is used to creat the root window of the application.
root = Tk()
#To give an tile to the window.
root.title("Weather App  |  Group #1  |  CE-3C")
# To give an dimension of the window.
root.geometry("890x470+300+200")
# To give the background color of the window.
root.configure(bg="#57adff")
# To give the restrection of the resize option of window.
root.resizable(False, False)



"""
Icons
"""
# Creating the photo element by giving element and storing it in variable
imageIcon = PhotoImage(file="Python_Weather_App/Images/logo.png")
# To provide an icon logo on the top left side of our app window.
root.iconphoto(False,imageIcon)

# Creating an image of rounded box to display today's weather.
roundBox = PhotoImage(file="Python_Weather_App\Images\Rounded Rectangle 1.png")
# It is used to place the round box on the root window of app.
Label(root, image=roundBox, bg="#57adff").place(x=30, y=110)

"""
Labels.
"""

# Creating the temperature label to put on the round box.
label1 = Label(root, text="Temperature :", font=('Helvetica', 11), fg="White", bg="#203243")
#Placing the temperature label to the round box.
label1.place(x=40, y=120)

# To sotre the actual data from API.
t = Label(root, text="36 °C", font=("Helvetica", 11, "bold"), fg="White", bg="#203243")
t.place(x=140, y=120)

# Creating the Humidity label to put on the round box.
label1 = Label(root, text="Humidity :", font=('Helvetica', 11), fg="White", bg="#203243")
#Placing the Humidity label to the round box.
label1.place(x=40, y=140)

# To sotre the actual data from API.
h = Label(root, text="56 %", font=("Helvetica", 11, "bold"), fg="White", bg="#203243")
h.place(x=140, y=140)

# Creating the Pressure label to put on the round box.
label1 = Label(root, text="Pressure :", font=('Helvetica', 11), fg="White", bg="#203243")
#Placing the Pressure label to the round box.
label1.place(x=40, y=160)

# To sotre the actual data from API.
p = Label(root, text="1003 hPa", font=("Helvetica", 11, "bold"), fg="White", bg="#203243")
p.place(x=140, y=160)

# Creating the Wind Speed label to put on the round box.
label1 = Label(root, text="Wind Speed :", font=('Helvetica', 11), fg="White", bg="#203243")
#Placing the Wind Speed label to the round box.
label1.place(x=40, y=180)


# To sotre the actual data from API.
w = Label(root, text="4.12 m/s", font=("Helvetica", 11, "bold"), fg="White", bg="#203243")
w.place(x=140, y=180)

# Creating the Description label to put on the round box.
label1 = Label(root, text="Description :", font=('Helvetica', 11), fg="White", bg="#203243")
#Placing the Description label to the round box.
label1.place(x=40, y=200)

# To sotre the actual data from API.
d = Label(root, text="Haze", font=("Helvetica", 11, "bold"), fg="White", bg="#203243")
d.place(x=140, y=200)

"""
Search Box
"""

# Creating an photo object by providing the search bar image path.
searchImage = PhotoImage(file="Python_Weather_App\Images\Rounded Rectangle 3.png")
# Creating an label on that image to put on the root window.
mySearchImage = Label(image=searchImage, bg="#57adff")
# Placing the image to the main root window.
mySearchImage.place(x=270, y=120)


# Creating an image to put on the search image to looks like search.
weatImage = PhotoImage(file="Python_Weather_App\Images\Layer 7.png")
# Crating weatImage as an label to put on the root window.
weatherImage = Label(root, image=weatImage, bg="#203243")
# Placing the weather image to the root window.
weatherImage.place(x=290, y=127)


# Text field on the search box to take an input.
textField = tk.Entry(root, justify="center", width=20, font=("poppins", 16, "bold"), bg="#203243", border=0, fg="White")
# Placing the textField to the search image.
textField.place(x=370, y=132)
# To focus on the textfield to fill it.
textField.focus()


# Creating the image of search icon to search the input.
searchIcon = PhotoImage(file="Python_Weather_App\Images\Layer 6.png")
# Creating the button of that search icon.
myImageIconButton = Button(image=searchIcon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeatherData)
# Placing the myImageIconButton on the search icon.
myImageIconButton.place(x=645, y=125)


"""
Bottom Boxes
"""

# Creating bottom box or bottom background.
bottomFrame  = Frame(root, width=900, height=180, bg="#212120")
bottomFrame.pack(side="bottom")

# Creating the first box to store the toay's weather conditions.
firstBox = PhotoImage(file="Python_Weather_App\Images\Rounded Rectangle 2.png")
# Creating the second box to store the upcomming days weather conditions.
secondBox = PhotoImage(file="Python_Weather_App\Images\Rounded Rectangle 2 copy.png")


# Making the box label and giving the placing it on the bottomFrame.
Label(bottomFrame, image=firstBox, bg="#212120").place(x=20, y=20)
Label(bottomFrame, image=secondBox, bg="#212120").place(x=290, y=30)
Label(bottomFrame, image=secondBox, bg="#212120").place(x=390, y=30)
Label(bottomFrame, image=secondBox, bg="#212120").place(x=490, y=30)
Label(bottomFrame, image=secondBox, bg="#212120").place(x=590, y=30)
Label(bottomFrame, image=secondBox, bg="#212120").place(x=690, y=30)
Label(bottomFrame, image=secondBox, bg="#212120").place(x=790, y=30)




"""
Clock
"""
clock = Label(root, text="02:30 PM", font=("Helvetica", 15, "bold"), fg="#212120", bg="#57adff", padx=10, pady=2, )
clock.place(x=65, y=20)


"""
Timezone
"""
timeZone = Label(root, text="Ahmedabad", font=("Helvetica", 15, "bold"), fg="#212120", bg="#57adff")
timeZone.place(x=700, y=20)


"""
Clock
"""
longLat = Label(root, text="LAT = 23.54", font=("Helvetica", 10, "bold"), fg="#212120", bg="#57adff")
longLat.place(x=700, y=45)


"""
Frames
"""

# First Frame
firstFrame = Frame(root, width=230, height=132, bg="#282829")
firstFrame.place(x=25, y=315)

day1 = Label(root, text="Wednesday", font=("Helvetica", 15), bg="#282829", fg="#fff")
day1.place(x=30, y=320)

firstImage = Label(root, bg="#282829")
firstImage.place(x=35, y=355)

day1MinMax = Label(firstFrame, bg="#282829", fg="#57adff", font=("Helvetica", 18, "bold"), text="Min: 23 °C\nMax: 24 °C")
day1MinMax.place(x=88, y=50)

# Second Frame
secondFrame = Frame(root, width=70, height=115, bg="#282829")
secondFrame.place(x=295, y=325)

day2 = Label(secondFrame, text="Tuesday", font=("Helvetica", 8), bg="#282829", fg="#fff")
day2.place(x=3, y=3)

secondImage = Label(secondFrame, bg="#282829")
secondImage.place(x=8, y=18)

day2MinMax = Label(secondFrame, bg="#282829", fg="#fff", text="Min: 23 °C\nMax: 24 °C", font=("Helvetica", 8))
day2MinMax.place(x=3, y=70)

# Third Frame
thirdFrame = Frame(root, width=70, height=115, bg="#282829")
thirdFrame.place(x=395, y=325)

day3 = Label(thirdFrame, text="Wednesday", font=("Helvetica", 8), bg="#282829", fg="#fff")
day3.place(x=3, y=3)

thirdImage = Label(thirdFrame, bg="#282829")
thirdImage.place(x=8, y=18)

day3MinMax = Label(thirdFrame, bg="#282829", fg="#fff", text="Min: 23 °C\nMax: 24 °C", font=("Helvetica", 8))
day3MinMax.place(x=3, y=70)

# Fourth Frame
fourthFrame = Frame(root, width=70, height=115, bg="#282829")
fourthFrame.place(x=495, y=325)

day4 = Label(fourthFrame, text="Thursday", font=("Helvetica", 8), bg="#282829", fg="#fff")
day4.place(x=3, y=3)

fourthImage = Label(fourthFrame, bg="#282829")
fourthImage.place(x=8, y=18)

day4MinMax = Label(fourthFrame, bg="#282829", fg="#fff", text="Min: 23 °C\nMax: 24 °C", font=("Helvetica", 8))
day4MinMax.place(x=3, y=70)

# Fifth Frame
fifthFrame = Frame(root, width=70, height=115, bg="#282829")
fifthFrame.place(x=595, y=325)

day5 = Label(fifthFrame, text="Friday", font=("Helvetica", 8), bg="#282829", fg="#fff")
day5.place(x=3, y=3)

fifthImage = Label(fifthFrame, bg="#282829")
fifthImage.place(x=8, y=18)

day5MinMax = Label(fifthFrame, bg="#282829", fg="#fff", text="Min: 23 °C\nMax: 24 °C", font=("Helvetica", 8))
day5MinMax.place(x=3, y=70)


# Sixth Frame
sixthFrame = Frame(root, width=70, height=115, bg="#282829")
sixthFrame.place(x=695, y=325)

day6 = Label(sixthFrame, text="Saturday", font=("Helvetica", 8), bg="#282829", fg="#fff")
day6.place(x=3, y=3)

sixthImage = Label(sixthFrame, bg="#282829")
sixthImage.place(x=8, y=18)

day6MinMax = Label(sixthFrame, bg="#282829", fg="#fff", text="Min: 23 °C\nMax: 24 °C", font=("Helvetica", 8))
day6MinMax.place(x=3, y=70)

# Seventh Frame
seventhFrame = Frame(root, width=70, height=115, bg="#282829")
seventhFrame.place(x=795, y=325)

day7 = Label(seventhFrame, text="Sunday", font=("Helvetica", 8), bg="#282829", fg="#fff")
day7.place(x=3, y=3)

seventhImage = Label(seventhFrame, bg="#282829")
seventhImage.place(x=8, y=18)

day7MinMax = Label(seventhFrame, bg="#282829", fg="#fff", text="Min: 23 °C\nMax: 24 °C", font=("Helvetica", 8))
day7MinMax.place(x=3, y=70)



# To give the infinite loop to the window until closed or else it will close suddendly.
root.mainloop()