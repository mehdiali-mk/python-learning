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

    account_sid = 'AC5de9f657383592936d4b690b73298a88'
    auth_token = '93636ebff54fd009f913a9fa209170ad'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG57d909a5ae43adbe70aae1376230ed07',
    body='It is rainy today, requesting to take an umbrella!!\n\nBe safe, do well.',
    to='+919537827429'
    )

    print(message.sid)