from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, FSInputFile
from Misc.buttons_text import MainMenu, ServiceButtons
from Misc.message_text import Service
from aiogram.fsm.context import FSMContext
from aiomysql import Pool
from DataBase import Database
from Entities import Rates

from Utils import GetCourse
from params import AED, FEE

"""
Роутер стартового меню
"""
mainMenu: Router = Router()


@mainMenu.message(Command("start"))
async def _start(message: Message, state: FSMContext, pool: Pool):
    await state.clear()
    db: Database = Database(pool=pool)
    await db.addUserId(message.from_user.id)
    
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=btnTxt.value)] for btnTxt in list(MainMenu)[:2]] +
                 [[KeyboardButton(text=btnTxt.value) for btnTxt in list(MainMenu)[2:]]],
        resize_keyboard=True
    )
    
    rates: Rates = await db.getRates()
    await message.answer(text=Service.start.format(
        __AED_TO_RUB__=rates.buy.value,
        __RUB_TO_AED__=rates.sell.value,
        __AED_TO_RUB_MIN__=rates.buyBig.value,
        __RUB_TO_AED_MIN__=rates.sellBig.value), reply_markup=keyboard)


@mainMenu.message(F.text == ServiceButtons.cancel.value)
async def _start(message: Message, state: FSMContext, pool: Pool):
    await state.clear()
    db: Database = Database(pool=pool)
    await message.answer(text=Service.cancelled)

    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=btnTxt.value)] for btnTxt in list(MainMenu)[:2]] +
                 [[KeyboardButton(text=btnTxt.value) for btnTxt in list(MainMenu)[2:]]],
        resize_keyboard=True
    )

    rates: Rates = await db.getRates()
    await message.answer(text=Service.start.format(
        __AED_TO_RUB__=rates.buy.value,
        __RUB_TO_AED__=rates.sell.value,
        __AED_TO_RUB_MIN__=rates.buyBig.value,
        __RUB_TO_AED_MIN__=rates.sellBig.value), reply_markup=keyboard)


@mainMenu.message(Command("restart"))
async def _restart(message: Message, state: FSMContext, pool: Pool):
    await state.clear()
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=btnTxt.value)] for btnTxt in list(MainMenu)[:2]] +
                 [[KeyboardButton(text=btnTxt.value) for btnTxt in list(MainMenu)[2:]]],
        resize_keyboard=True
    )
    await message.answer_photo(caption=Service.faq, photo=FSInputFile("Misc/faq_media.jpg"), reply_markup=keyboard)


@mainMenu.message(Command("course"))
@mainMenu.message(F.text == MainMenu.course.value)
async def _course(message: Message, pool: Pool):
    """
    Получение актуальных курсов обмена валют
    """
    db: Database = Database(pool=pool)
    rates: Rates = await db.getRates()
    await message.answer(text=Service.course.format(
        __AED_TO_RUB__=rates.buy.value,
        __RUB_TO_AED__=rates.sell.value,
        __AED_TO_RUB_MIN__=rates.buyBig.value,
        __RUB_TO_AED_MIN__=rates.sellBig.value))


@mainMenu.message(Command("faq"))
@mainMenu.message(F.text == MainMenu.faq.value)
async def _faq(message: Message):
    await message.answer_photo(caption=Service.faq, photo=FSInputFile("Misc/faq_media.jpg"))
