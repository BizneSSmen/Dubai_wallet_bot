from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import KeyboardButton, Message, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from Misc.buttons_text import MainMenu, ServiceButtons
from Misc.message_text import Service
from aiogram.fsm.context import FSMContext

from Utils import GetCourse
from params import AED, FEE

mainMenu: Router = Router()


@mainMenu.message(Command("start"))
async def _start(message: Message, state: FSMContext):
    await state.clear()

    aedCourse: float = await GetCourse(*AED)()

    keyboard: ReplyKeyboardBuilder = ReplyKeyboardBuilder().add(*[KeyboardButton(text=btnTxt.value) for btnTxt in MainMenu])
    keyboard.adjust(1)

    await message.answer(reply_markup=keyboard.as_markup(resize_keyboard=True),
                         text=Service.start.format(
                             __AED_TO_RUB__=aedCourse + FEE,
                             __RUB_TO_AED__=aedCourse - FEE))


@mainMenu.message(F.text == ServiceButtons.cancel.value)
async def _cancel(message: Message, state: FSMContext):
    await state.clear()

    keyboard: ReplyKeyboardBuilder = ReplyKeyboardBuilder().add(*[KeyboardButton(text=btnTxt.value) for btnTxt in MainMenu])
    keyboard.adjust(1)

    await message.answer(text=Service.cancelled, reply_markup=keyboard.as_markup(resize_keyboard=True))


@mainMenu.message(F.text == MainMenu.course.value)
async def _course(message: Message):
    aedCourse: float = await GetCourse(*AED)()

    await message.answer(text=Service.course.format(
                             __AED_TO_RUB__=aedCourse + FEE,
                             __RUB_TO_AED__=aedCourse - FEE))
