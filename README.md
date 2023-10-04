# Rain Alert Message
Creating a rain alert message system using Python, the OpenWeatherMap API, and Twilio allows you to receive notifications when rain is expected in your area. This can be a helpful tool to plan your day especially if you need to be prepared for rainy weather.

## Prerequisites
- Python - version 3.11.1
- OpenWeatherMap API Key - Sign up [OpenWeatherMap](https://openweathermap.org/api)
- Twilio account and credentials - Sign up [Twilio](https://www.twilio.com/)

## Executing Output
**1. Get OpenWeatherMap API Key:**
Sign up for an OpenWeatherMap account and generate an API key. You'll need this key to access weather data.

**2. Install Required Libraries:**
Install the necessary Python libraries `requests`` for API requests and the Twilio Python library for sending SMS messages. 
You can install them using pip
```
pip3 install twilio
```

**3. Write Python Script:** 
Clone this repo to your desktop and replace `API_KEY` `MY_ACCOUNT_SID` `MY_AUTH_TOKEN` `TWILIO_NUMBER` and `RECIPIENT_PHONE_NUMBER` with your actual API keys and phone numbers.

**4. Run the Script:**
Run `main.py` file 
```
python3 ./main.py
```
