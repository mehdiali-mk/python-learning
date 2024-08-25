"""
Aim: STOCK market price alert on SMS.
Author: Mehdiali
Date: 04 / July / 2024 - 05:42 PM
"""

# Import Variables

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_NAME = "TESLA"

API_KEY = "You API KEY"
API_KEY_NEWS = "YOUR API KEY"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

KEY_OPEN = "1. open"
KEY_HIGH = "2. high"
KEY_LOW = "3. low"
KEY_CLOSE = "4. close"
KEY_VOLUME = "5. volume"


# Import
import requests
import datetime as dt


# Taking the STOCK Data.
STOCK_ENDPOINT_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=STOCK_ENDPOINT_PARAMETERS)
stockData = response.json()

dailyData = stockData["Time Series (Daily)"]


# Taking Required Date
todayDate = dt.date.today()
yesterdayDate = todayDate - dt.timedelta(days=2)
beforeYesterdayDate = yesterdayDate - dt.timedelta(days=1)


# Taking Data according to the DATE.
yesterdayData = dailyData[f"{yesterdayDate}"]
beforeYesterdayData = dailyData[f"{beforeYesterdayDate}"]


# Taking open and closing price on DATA
openYesterday = float(yesterdayData[KEY_OPEN])
openBeforeYesterday = float(beforeYesterdayData[KEY_OPEN])

closeYesterday = float(yesterdayData[KEY_CLOSE])
closeBeforeYesterday = float(beforeYesterdayData[KEY_CLOSE])

percentage = round(((closeYesterday - closeBeforeYesterday) / closeYesterday) * 100)


if (abs(percentage) >= 5):

    # Taking the news data.
    NEWS_ENDPOINT_PARAMETER = {
        "q": NEWS_NAME,
        "from": yesterdayDate,
        "to": yesterdayDate,
        "sortBy": "popularity",
        "apiKey": API_KEY_NEWS
    }

    response = requests.get(NEWS_ENDPOINT, params=NEWS_ENDPOINT_PARAMETER)

    newsData = response.json()
    newsArticle = newsData["articles"]


    # Taking the title and description
    newsTitle = newsArticle[1]["title"]
    newsDescription = newsArticle[1]["description"]


    # Sending the message to the user.
    from twilio.rest import Client

    account_sid = 'You Account SID'
    auth_token = 'Your Token'
    client = Client(account_sid, auth_token)

    if (percentage > 0):
        headingMessage = f"TSLA: 🔺{percentage}%"
    else:
        headingMessage = f"TSLA: 🔻{percentage}%"

    message = client.messages.create(
        messaging_service_sid='Your Message ID',
        body=f'\n\n{headingMessage}\nTitle = {newsTitle}\n\nDescription = {newsDescription}',
        to='+919537827429'
    )



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

