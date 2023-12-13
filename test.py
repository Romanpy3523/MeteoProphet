import requests
import os

TOKEN = os.getenv('WEATHER_TOKEN')

city = input()
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN}&units=metric'
response = requests.post(url)

data = response.json()

name = data['name']
temp = data['main']['temp']
press = data['main']['pressure']
wind = data['wind']['speed']
        
print(f'Погода в городе: {name}\n Температура: {temp} \n Давление: {press}\n Скорость ветра: {wind} м/с')