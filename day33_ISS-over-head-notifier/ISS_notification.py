import requests
from datetime import datetime

MY_LAT = -32.05945
MY_LNG = 115.84491

class ISS:
    def __init__(self):
        self.iss_position = (None, None)
        self.issLocation()

    def issLocation(self):
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()

        data = response.json()

        longitude = data["iss_position"]["longitude"]
        latitude = data["iss_position"]["latitude"]

        self.iss_position = (longitude, latitude)

class DayOrNight:
    def __init__(self):
        self.timeDayNight = (None, None)
        self.currentTime = datetime.now()
        self.DayOrNightTime()
    
    def DayOrNightTime(self):
        myParams = {
            "lat": MY_LAT,
            "lng": MY_LNG,
            "formatted": 0,
            }
        response = requests.get(url="https://api.sunrise-sunset.org/json", params=myParams, verify=False)
        response.raise_for_status()

        data = response.json()

        sunrise = data["results"]["sunrise"]
        sunset = data["results"]["sunset"]

        self.timeDayNight = (sunrise, sunset)

        

dayOrNight = DayOrNight()
print(dayOrNight.currentTime)
print(dayOrNight.timeDayNight)
#class ISS_Notification:
#    def __init__(self):
#        response = requests.get(url="http://api.open-notify.org/iss-now.json")
