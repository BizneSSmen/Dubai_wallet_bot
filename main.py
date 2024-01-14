import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiomysql import Pool

from DataBase import createPool
from config import loadConfig, Config
from Routers import routers

from Middlewares import DataBaseMiddleWare

from Misc.message_text import Service


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    config: Config = loadConfig("config.env")
    dbConfig = config.dataBase

    loop = asyncio.get_event_loop()

    pool: Pool = await createPool(user=dbConfig.login,
                                  password=dbConfig.password,
                                  address=dbConfig.address,
                                  port=dbConfig.port,
                                  db=dbConfig.dbName,
                                  loop=loop)

    bot: Bot = Bot(config.tgBot.userToken, parse_mode="HTML")
    await bot.set_my_description(description=Service.faq)
    dp: Dispatcher = Dispatcher(storage=MemoryStorage(), loop=loop)
    dp.message.outer_middleware(DataBaseMiddleWare(pool=pool))
    dp.callback_query.outer_middleware(DataBaseMiddleWare(pool=pool))

    dp.include_routers(*routers)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
