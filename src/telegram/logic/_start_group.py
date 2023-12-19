# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from aiogram.types import Message

from src.telegram.sendler.sendler import Sendler_msg


async def start_group(message: Message):
    good_status = ['creator', 'administrator']

    print(f'В чате сообщение "{message.text}"')

    user_id = message.from_user.id

    chat_id = message.chat.id

    text_msg = message.text if message.text else message.caption

    name_channel = message.chat.full_name

    info_user = await message.bot.get_chat_member(chat_id, user_id)

    is_admin = info_user['status']

    try:
        await message.delete()
    except Exception as es:
        await Sendler_msg.sendler_to_admin(message, f'Не могу удалить сообщение "{text_msg}" '
                                                    f'т.к. я не являюсь администратором в '
                                                    f'канале "{name_channel}"', None)
