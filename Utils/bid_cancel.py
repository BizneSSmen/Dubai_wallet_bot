# import asyncio
#
# from aiogram import Bot
# from aiogram.exceptions import TelegramBadRequest
# from aiogram.fsm.context import FSMContext
#
# from Misc.User_text import Message_text
#
#
# async def cancel(bot: Bot, messageId: str, chatId: str, state: FSMContext):
#     await asyncio.sleep(1200)
#     try:
#         await bot.edit_message_reply_markup(chat_id=chatId, reply_markup=None, message_id=messageId)
#     except TelegramBadRequest:
#         pass
#     await bot.send_message(text=Message_text.service_text.UserMessageText.cancelOrder, chat_id=chatId)
#     await state.clear()
