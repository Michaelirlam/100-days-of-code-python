import requests
from datetime import datetime, timezone
import smtplib
import time

# Svendborg Coordinates
MY_LATITUDE = 55.067400
MY_LONGITUDE = 10.607300

def latitude_compare(my_lat, iss_lat):
    return abs(my_lat - iss_lat) <= 5

def longitude_compare(my_lng, iss_lng):
    return abs(my_lng - iss_lng) <= 5

def is_night(sunrise, sunset, current_time):
    return current_time < sunrise or current_time > sunset


while True:
    current_hour = datetime.now(timezone.utc).hour

    # |--------------------- ISS API -----------------------|

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")

    # Raises HTTP error code message is response is not 200
    iss_response.raise_for_status()

    # Access API data and pull out ISS latitude and longitude for comparison against current pos
    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_position = (iss_latitude, iss_longitude)

    # |--------------------- SUNSET API -----------------------|

    # Parameters to pass into the sunset API call
    sunset_params =  {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=sunset_params)
    sunset_response.raise_for_status()

    sunset_data = sunset_response.json()

    # Sunrise and sunset by hour using 24 hr clock
    sunrise_hour = int(sunset_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sunset_data["results"]["sunset"].split("T")[1].split(":")[0])


    if latitude_compare(MY_LATITUDE, iss_latitude) and longitude_compare(MY_LONGITUDE, iss_longitude) and is_night(sunrise_hour, sunset_hour, current_hour):
        print("LOOK UP")
        # TODO: setup throw away email account to test
        # with smtplib.SMTP("smtp.example.com") as connection:
        #     connection.starttls()
        #     connection.login(user="your@email.com", password="yourpassword")
        #     connection.sendmail(
        #         from_addr="your@email.com",
        #         to_addrs="to@email.com",
        #         msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
        #     )
    else:
        print("You'll have to wait")
    
    time.sleep(60)