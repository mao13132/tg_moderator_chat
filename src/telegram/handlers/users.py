from aiogram.types import Message

from aiogram import Dispatcher

from settings import ADMIN, LOGO
from src.telegram.keyboard.keyboards import Admin_keyb
from src.telegram.logic._start_admin import start_admin
from src.telegram.logic._start_group import start_group
from src.telegram.sendler.sendler import Sendler_msg
from src.telegram.bot_core import BotDB


async def del_(message: Message):
    try:
        id_tur = str(message.text).split('_')[1]
    except Exception as es:
        msg = (f'Ошибка при разборе для удаления del_{es}')
        print(msg)
        try:
            await Sendler_msg.send_msg_message(message, msg, None)
        except:
            pass
        return False

    _del_word = BotDB.del_word(id_tur)

    if _del_word:
        _msg = f'✅ Стоп слово удалено'
    else:
        _msg = f'❌ Ошибка удаления стоп слова'

    keyb = Admin_keyb().back_add_words()

    await Sendler_msg().new_sendler_photo_message(message, LOGO, _msg, keyb)


async def start(message: Message):
    id_user = message.chat.id

    type_message = message.chat.type

    if type_message == 'group':
        await start_group(message)

    if type_message == 'private':
        if str(id_user) in ADMIN:
            await start_admin(message)


def register_user(dp: Dispatcher):
    dp.register_message_handler(del_, text_contains='/del_')

    dp.register_message_handler(start, text_contains='')
