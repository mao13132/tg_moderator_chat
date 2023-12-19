from aiogram.types import Message

from aiogram import Dispatcher

from settings import ADMIN


async def start(message: Message):
    id_user = message.chat.id

    if str(id_user) in ADMIN:
        await message.bot.send_message(message.chat.id, message.text)


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, text_contains='')
