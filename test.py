import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import loadConfig, Config
from Routers import routers

from Middlewares import DataBaseMiddleWare



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
config: Config = loadConfig("config.env")
dbLoop = asyncio.new_event_loop()
asyncio.set_event_loop(dbLoop)

adminBot: Bot = Bot("6730070621:AAFsndJsyenj6idpjzc-UhKdUntUkE7KR58")
bot: Bot = Bot(config.tgBot.token, parse_mode="HTML")

adminDp: Dispatcher= Dispatcher(storage=MemoryStorage())
dp: Dispatcher = Dispatcher(storage=MemoryStorage())
# dp.message.outer_middleware(Test(123))

dp.include_routers(*routers)

async def start1():
    await adminDp.start_polling(adminBot)
    

async def start2():
    await dp.start_polling(bot)


if __name__ == "__main__": # Здесь был Пупсень
    loop = asyncio.get_event_loop()
    tasks = [start1(), start2()]
    loop.run_forever(asyncio.gather(*tasks))
