import requests

apiEndpoint = "https://api.openweathermap.org/data/2.5/weather"
apiKey = "50f281806b06ecc7a08b9021c7be86ca"

weatherParameters = {
    "q": "Ahmedabad,IN",
    "appid": apiKey
}

openInBrowser = f"{apiEndpoint}?q={weatherParameters['q']}&appid={weatherParameters['appid']}"
print(openInBrowser)

response = requests.get(apiEndpoint, params=weatherParameters)

weatherData = response.json()

print(weatherData)
rainMeter = weatherData["weather"][0]["id"]

if rainMeter > 700:
    from twilio.rest import Client

    account_sid = 'You SID'
    auth_token = 'Your Token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='Your Messaging Service SID',
    body='It is rainy today, requesting to take an umbrella!!\n\nBe safe, do well.',
    to='+919537827429'
    )

    print(message.sid)