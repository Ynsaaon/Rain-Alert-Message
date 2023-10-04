import requests
from twilio.rest import Client

CW_ENDPOINTS = "https://api.openweathermap.org/data/2.5/weather"
api_key = API_KEY
ACC_SID = MY_ACCOUNT_SID
AUTH_TOKEN = MY_AUTH_TOKEN

parameters = {
    "lat": YOUR_LATITUDE,
    "lon": YOUR_LONGITUDE,
    "appid": api_key
}

response = requests.get(CW_ENDPOINTS, params=parameters)
response.raise_for_status()
data = response.json()
condition_code = data["weather"][0]["id"]

if int(condition_code) < 800:
    client = Client(ACC_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️.",
        from_=TWILIO_NUMBER,
        to=RECIPIENT_PHONE_NUMBER
    )
    print(message.status)