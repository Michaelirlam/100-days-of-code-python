import requests
import os
import smtplib

# Using environmental variables for sensitive information
sender_email = os.environ.get("SENDER_EMAIL")
sender_password = os.environ.get("SENDER_PASSWORD")
recipient_email = os.environ.get("RECIPIENT_EMAIL")
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
LAT = os.environ.get("POS_LATITUDE")
LON = os.environ.get("POS_LONGITUDE")

# Parameters to be passed into the api call to Open Weather API
PARAMS = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
}

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