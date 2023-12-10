import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram import types
from aiogram.filters import CommandStart


bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message()
async def start(message:types.message):
    msg = await message.answer(text=message.text)
    


async def main():
    await dp.start_polling(bot)
    logging.basicConfig(level=logging.info, stream=sys.stdout)

if __name__=='__main__':
    asyncio.run(main())
    