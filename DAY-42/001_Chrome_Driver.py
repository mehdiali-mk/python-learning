from selenium import webdriver
from selenium.webdriver.common.by import By
# driverPath = "C:/Developer/chromedriver"
driver = webdriver.Chrome()

driver.get("https://www.python.org/")

eventsName = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

eventList = (eventsName[0].text).split("\n")
eventDict = {}
numCount = 0
for count in range(0,len(eventList), 2):
    eventDict.update({
        numCount: {
        "time": eventList[count],
        "event": eventList[count + 1]
        }
    })
    numCount+=1

print(eventDict)
driver.close()
driver.quit()