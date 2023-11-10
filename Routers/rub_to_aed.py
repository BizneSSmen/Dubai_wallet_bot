import re
from pprint import pprint

from aiogram import F, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardButton, KeyboardButton, CallbackQuery, Document, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiomysql import Pool

from Misc.buttons_text import MainMenu, BankList, LocationList, ServiceButtons
from Misc.message_text import RubToAed, Service
from DataBase import Database
from Entities import Claim, OperationStatuses, OperationTypes
from Utils import GetCourse
from params import AED, FEE

rubToAed: Router = Router()


class RubToAedStates(StatesGroup):
    bank: State = State()
    amount: State = State()
    phoneNumber: State = State()
    location: State = State()
    accept: State = State()


@rubToAed.message(F.text == MainMenu.rubToAed.value)
async def _start(message: Message, state: FSMContext):
    claim: Claim = Claim()
    claim.currency_B = 'AED'
    claim.currency_A = 'RUB'

    await message.answer(text=RubToAed.changeKbMessage,
                         reply_markup=ReplyKeyboardBuilder(
                             [[KeyboardButton(text=ServiceButtons.cancel.value)]]).as_markup(resize_keyboard=True))

    mainMsg: message = await message.answer(text=RubToAed.enterAmount)
    data: dict = {'claim': claim, 'mainMsg': mainMsg.message_id}

    await state.set_state(RubToAedStates.amount)
    await state.set_data(data)  # -> SET DATA


@rubToAed.message(RubToAedStates.amount)
async def _amount(message: Message, state: FSMContext, bot: Bot):
    data: dict = await state.get_data()  # <- GET DATA
    claim: Claim = data['claim']

    await message.delete()

    if message.text is not None:
        claim.targetAmount = float(message.text) if message.text.isdigit() else 0

    if claim.targetAmount > 0:
        if 'errMsg' in data:
            await bot.delete_message(chat_id=message.chat.id, message_id=data['errMsg'])
            del data['errMsg']

        await bot.delete_message(chat_id=message.chat.id, message_id=data['mainMsg'])

        claim.fee = FEE
        claim.exchangeAppliedRate = await GetCourse(*AED)()
        claim.finalAmount = round(claim.targetAmount / (claim.exchangeAppliedRate + claim.fee), 2)

        inlineKeyboard: InlineKeyboardBuilder = InlineKeyboardBuilder(
            [[InlineKeyboardButton(text=btnTxt.value, callback_data=f"{btnTxt.value}_bank") for btnTxt in
              BankList]])
        inlineKeyboard.adjust(3)
        mainMsg: Message = await message.answer(text=RubToAed.chooseBank.format(__TARGET_AMOUNT__=claim.targetAmount,
                                                                                __COURSE__=claim.exchangeAppliedRate + claim.fee,
                                                                                __FINAL_AMOUNT__=claim.finalAmount),
                                                reply_markup=inlineKeyboard.as_markup())

        data['claim'] = claim
        data['mainMsg'] = mainMsg.message_id

        await state.set_state(RubToAedStates.bank)
        await state.set_data(data)  # -> SET DATA

    else:
        if 'errMsg' not in data:
            errorMessage: Message = await message.answer(text=RubToAed.amountError)
            data['errMsg']: str = errorMessage.message_id

    await state.set_data(data=data)  # -> SET DATA


@rubToAed.callback_query(F.data.split("_")[-1] == "bank", RubToAedStates.bank)
async def _bank(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data: dict = await state.get_data()  # <- GET DATA
    data['bank'] = callback.data.split("_")[0]
    claim: Claim = data['claim']

    await bot.delete_message(chat_id=callback.message.chat.id, message_id=data['mainMsg'])

    inlineKeyboard: InlineKeyboardBuilder = InlineKeyboardBuilder(
        [[InlineKeyboardButton(text=btnTxt.value, callback_data=f"{btnTxt.value}_location") for btnTxt in
          LocationList]])
    inlineKeyboard.adjust(2)

    mainMsg: Message = await callback.message.answer(
        text=RubToAed.chooseLocation.format(__BANK__=data['bank'],
                                            __TARGET_AMOUNT__=claim.targetAmount,
                                            __COURSE__=claim.exchangeAppliedRate + claim.fee,
                                            __FINAL_AMOUNT__=claim.finalAmount
                                            ), reply_markup=inlineKeyboard.as_markup())

    data['mainMsg']: str = mainMsg.message_id
    data['claim'] = claim

    await state.set_state(RubToAedStates.location)
    await state.set_data(data=data)  # -> SET DATA


@rubToAed.callback_query(F.data.split("_")[-1] == 'location', RubToAedStates.location)
async def _location(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data: dict = await state.get_data()  # <- GET DATA
    data['location']: str = callback.data.split("_")[0]
    claim: Claim = data['claim']

    await bot.delete_message(chat_id=callback.message.chat.id, message_id=data['mainMsg'])

    keyboard: ReplyKeyboardBuilder = ReplyKeyboardBuilder(
        [[KeyboardButton(text=ServiceButtons.sharePhoneNumber.value, request_contact=True),
          KeyboardButton(text=ServiceButtons.cancel.value)]])
    keyboard.adjust(1)
    mainMsg: Message = await callback.message.answer(
        text=RubToAed.phoneNumber.format(__BANK__=data['bank'],
                                         __TARGET_AMOUNT__=claim.targetAmount,
                                         __COURSE__=claim.exchangeAppliedRate + claim.fee,
                                         __FINAL_AMOUNT__=claim.finalAmount,
                                         __LOCATION__=data['location']
                                         ), reply_markup=keyboard.as_markup(resize_keyboard=True))
    data['mainMsg'] = mainMsg.message_id
    data['claim'] = claim

    await state.set_state(RubToAedStates.phoneNumber)
    await state.set_data(data=data)  # -> SET DATA


@rubToAed.message(RubToAedStates.phoneNumber)
async def _phoneNumber(message: Message, state: FSMContext, bot: Bot, pool: Pool):
    data: dict = await state.get_data()  # <- GET DATA
    claim: Claim = data['claim']

    await message.delete()

    if message.contact is not None:
        claim.phoneNumber = message.contact.phone_number
    elif message.text is not None:
        phonePattern: re.Pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
        claim.phoneNumber = phonePattern.match(message.text).group() if phonePattern.match(message.text) else None

    if claim.phoneNumber:
        if "errMsg" in data:
            await bot.delete_message(chat_id=message.chat.id, message_id=data["errMsg"])
            del data["errMsg"]

        await bot.delete_message(chat_id=message.chat.id, message_id=data["mainMsg"])  # del MainMsg

        await message.answer(text='Спасибо!', reply_markup=ReplyKeyboardBuilder(
            [[KeyboardButton(text=ServiceButtons.cancel.value)]]).as_markup(resize_keyboard=True))

        description: str = RubToAed.result.format(__BANK__=data['bank'][1:],
                                                  __TARGET_AMOUNT__=claim.targetAmount,
                                                  __COURSE__=claim.exchangeAppliedRate + claim.fee,
                                                  __FINAL_AMOUNT__=claim.finalAmount,
                                                  __LOCATION__=data['location'][1:],
                                                  __PHONE__=claim.phoneNumber)
        claim.description = description

        db: Database = Database(pool=pool)
        data['claimId'] = await db.insertСlaim(vars(claim))

        mainMsg: Message = await message.answer(text=RubToAed.result.format(__BANK__=data['bank'],
                                                                            __TARGET_AMOUNT__=claim.targetAmount,
                                                                            __COURSE__=claim.exchangeAppliedRate + claim.fee,
                                                                            __FINAL_AMOUNT__=claim.finalAmount,
                                                                            __LOCATION__=data['location'],
                                                                            __PHONE__=claim.phoneNumber),
                                                reply_markup=InlineKeyboardBuilder(
                                                    [[InlineKeyboardButton(text="Подтвердить",
                                                                           callback_data="done")]]).as_markup())

        data["mainMsg"] = mainMsg.message_id  # set MainMsg
        data['claim'] = claim

        await state.set_state(RubToAedStates.accept)
        await state.set_data(data=data)  # -> SET DATA

    else:
        if "errMsg" not in data:
            errorMessage: Message = await message.answer(text=RubToAed.phoneNumberError)
            data["errMsg"]: str = errorMessage.message_id

    await state.set_data(data=data)  # -> SET DATA


@rubToAed.callback_query(F.data == 'done', RubToAedStates.accept)
async def _accept(callback: CallbackQuery, state: FSMContext, bot: Bot, pool: Pool):
    data: dict = await state.get_data()  # <- GET DATA
    claim: Claim = data['claim']
    claim.status = OperationStatuses.approved

    db: Database = Database(pool=pool)
    await db.updateClaimById(data['claimId'], {'status': OperationStatuses.approved})

    await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, reply_markup=None, message_id=data['mainMsg'])

    keyboard: ReplyKeyboardBuilder = ReplyKeyboardBuilder().add(
        *[KeyboardButton(text=btnTxt.value) for btnTxt in MainMenu])
    keyboard.adjust(1)
    await callback.message.answer(text=RubToAed.instruction, reply_markup=keyboard.as_markup(resize_keyboard=True))

    await state.clear()
