import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from handlers import handler_start, prophet



bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_routers(handler_start.router, prophet.router)
    


async def main():
    await dp.start_polling(bot)
    logging.basicConfig(level=logging.info, stream=sys.stdout)

if __name__=='__main__':
    asyncio.run(main())
    