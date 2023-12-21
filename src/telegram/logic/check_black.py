# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from aiogram.types import Message

from src.telegram.bot_core import BotDB


async def check_black(tex_message):
    stop_word_list = BotDB.get_stop_word()

    if tex_message is None:
        return False

    try:
        tex_message_lower = tex_message.lower()
    except Exception as es:
        print(f'check_black Ошибка при уменьшения регистра у tex_message "{tex_message}" ошибка "{es}"')

        return True

    for word in stop_word_list:
        try:
            stop_word = word[1].lower()
        except Exception as es:
            print(f'Ошибка при уменьшения регистра у sql word "{word[1]}" ошибка "{es}"')

            continue

        if stop_word in tex_message_lower:
            return True

    return False
