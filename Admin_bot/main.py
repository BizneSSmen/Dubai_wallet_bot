import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import loadConfig, Config
from Routers import routers


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    config = loadConfig("config.env").tgBot

    bot: Bot = Bot(token='6564981419:AAGH-tz6Edur9AOlcHAG8gPvi5iDigY4hHU', parse_mode="HTML")

    dp: Dispatcher = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
