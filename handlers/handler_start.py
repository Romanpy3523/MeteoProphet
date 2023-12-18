from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from kb.keyboards import keyboard

router = Router()


@router.message(Command('start'))
async def start(message: types.message):
   
    await message.answer(text = 'Привет')
    await message.answer(text = 'Напиши мне название города, и я пришлю тебе сводку погоды на сегодня!🙂', reply_markup=keyboard)