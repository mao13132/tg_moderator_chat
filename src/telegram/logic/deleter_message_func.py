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


async def delete_message_func(message: Message):
    text_msg = message.text if message.text else message.caption

    name_channel = message.chat.full_name

    try:
        await message.delete()
    except Exception as es:
        if "be deleted for everyone" in str(es) or "Message can't be deleted" in str(es):

            await Sendler_msg.sendler_to_admin(message, f'Не могу удалить сообщение "{text_msg}" '
                                                        f'т.к. я не являюсь администратором в '
                                                        f'канале "{name_channel}"', None)


        else:
            error_ = f'Ошибка при удаление сообщения "{es}"'

            print(error_)

            await Sendler_msg.sendler_to_admin(message, f'Не могу удалить сообщение "{error_}" '
                                                        f'т.к. я не являюсь администратором в '
                                                        f'канале "{name_channel}" "{es}"', None)
