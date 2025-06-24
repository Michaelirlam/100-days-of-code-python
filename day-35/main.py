import requests
import os
import smtplib

# Using environmental variables for sensitive information, youwill need to set these in your environment to run the script
# There will be a check to ensure that all required variables are set before making the API call
sender_email = os.environ.get("SENDER_EMAIL") # use export SENDER_EMAIL= in the console to set
sender_password = os.environ.get("SENDER_PASSWORD") # use export SENDER_PASSWORD= in the console to set
recipient_email = os.environ.get("RECIPIENT_EMAIL") # use export RECIPIENT_EMAIL= in the console to set
API_KEY = os.environ.get("OPENWEATHER_API_KEY") # use export OPENWEATHER_API_KEY= in the console to set
LAT = os.environ.get("POS_LATITUDE") # use export POS_LATITUDE= in the console to set
LON = os.environ.get("POS_LONGITUDE") # use export POS_LONGITUDE= in the console to set

# Parameters to be passed into the api call to Open Weather API
PARAMS = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
}

# Make a GET request to the Open Weather API to get the weather forecast for the next 5 days
# The API returns a JSON response with weather data
# Check if all required environment variables are set
if not all([sender_email, sender_password, recipient_email, API_KEY, LAT, LON]):
    raise ValueError("Please set all required environment variables: SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, OPENWEATHER_API_KEY, POS_LATITUDE, POS_LONGITUDE")
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=PARAMS)
response.raise_for_status()
weather_data = response.json()["list"]

def check_raining(data):
    """Checks Weather data for rainy conditions
    :params = data - should be the json data from the weather api get request
    """
    return any(forecast["weather"][0]["id"] < 700 for forecast in data)

# Uses the smtp library to send an email to the recipient when the check_raining function is True
if check_raining(weather_data):
    try:
        with smtplib.SMTP("smtp.example.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=sender_password,
                msg="Subject:It's going to rain today!\n\nMake sure you pack an umbrella ☂️."
            )
    except Exception as exc:
        print(f"Error sending email: {exc}")
else:
    print("No rain detected. No email has been sent")