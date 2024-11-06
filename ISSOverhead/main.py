import os
import requests
import smtplib
from datetime import datetime
import time
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
to_email = os.getenv("TO_EMAIL")
smtp_address = os.getenv("SMTP_ADDRESS")

MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")


def am_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    dif_lat = iss_latitude - float(MY_LAT)
    dif_long = iss_longitude - float(MY_LONG)
    if 5 >= dif_lat >= -5 and 5 >= dif_long >= -5:
        return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if hour_now < sunrise - 1 or hour_now > sunset + 1:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if am_close() and is_dark():
        with smtplib.SMTP(smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:ISS is here! \n\nLook up! \nThe ISS is passing over your head now."
                                )
    else:
        print("Not here!")
