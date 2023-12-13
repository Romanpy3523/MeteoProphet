import datetime
from aiogram import Router
from aiogram import types
import requests
import os

router = Router()



@router.message()
async def meteo(message: types.message):
    current_date = datetime.datetime.now().strftime('%Y - %m - %d')
    
    TOKEN = os.getenv('WEATHER_TOKEN')
    response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={TOKEN}&units=metric')
    
    data = response.json()
    name = data['name']
    temp = data['main']['temp']
    press = data['main']['pressure']
    wind = data['wind']['speed']
        
    await message.answer(f'{name}\n ***{current_date}***\n Температура: {temp} \n Давление: {press} мм.рт.ст \n Скорость ветра: {wind} м/с')
