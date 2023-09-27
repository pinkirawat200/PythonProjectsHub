import requests
import json

city = input("Enter name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=9645fb3a80a3423a95d35347232509&q={city}"

r = requests.get(url)
print(r.text)
print(type(r.text))
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])

import win32com.client as wincom

if r.status_code == 200:
    data = json.loads(r.text)
    if "current" in data:
        current_weather = data["current"]
        temp_c = current_weather.get("temp_c")
        humidity = current_weather.get("humidity")

        print(f"Temperature in {city}: {temp_c} degrees Celsius")
        print(f"Humidity in {city}: {humidity}%")

        # Initialize the text-to-speech engine
        speaker = wincom.Dispatch("SAPI.SpVoice")

        # Speak the temperature and humidity
        speaker.Speak(f"The temperature in {city} is {temp_c} degrees Celsius.")
        speaker.Speak(f"The humidity in {city} is {humidity} percent.")
    else:
        print(f"Unable to fetch weather data for {city}.")
else:
    print(f"Error fetching data for {city}. Status code: {r.status_code}")

