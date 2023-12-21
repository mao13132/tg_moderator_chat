# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from aiogram.types import Message

from src.telegram.logic.check_black import check_black
from src.telegram.logic.check_link import check_link
from src.telegram.logic.deleter_message_func import delete_message_func


async def start_group(message: Message):
    good_status = ['creator', 'administrator']

    user_id = message.from_user.id

    chat_id = message.chat.id

    text_msg = message.text if message.text else message.caption

    info_user = await message.bot.get_chat_member(chat_id, user_id)

    status_user_from_group = info_user['status']

    is_black = await check_black(text_msg)

    print(f'В чате сообщение "{text_msg}" is_black "{is_black}"')

    if status_user_from_group not in good_status and is_black:
        await delete_message_func(message)

    is_link = await check_link(text_msg)

    if status_user_from_group not in good_status and is_link:
        await delete_message_func(message)
