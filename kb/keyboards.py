from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton)


main = [
        [
           KeyboardButton(text='Москва'),
           KeyboardButton(text='Санкт-петербург')
        ],
        [   
           KeyboardButton(text='Тула'),
           KeyboardButton(text='Рязань')
        ],
        [   
           KeyboardButton(text='Сочи'),
           KeyboardButton(text='Владивосток')
        ],
               
      ]
keyboard = ReplyKeyboardMarkup(keyboard = main, resize_keyboard=True, )
