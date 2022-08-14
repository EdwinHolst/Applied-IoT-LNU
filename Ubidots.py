import urequests as requests


TOKEN = "BBFF-rw4bYoFCKwDBvCotcQy2tNoEVBW3Gv" #Put here your TOKEN
DEVICE_LABEL = "freenove-esp32-wrover-dev" # Assign the device label desire to be send

TEMP_LABEL = "temp"  # Assign the variable label desire to be send
PHOTO_LABEL = "pres"

# Sending data to Ubidots Restful Webserice
def sendData(temp, photo_res):
    data = {TEMP_LABEL: {"value": temp}, PHOTO_LABEL: {"value": photo_res}}
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + DEVICE_LABEL
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

        if data is not None:
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass
    