# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from settings import LOGO
from src.telegram.keyboard.keyboards import Admin_keyb
from src.telegram.sendler.sendler import Sendler_msg


async def start_admin(message: Message):
    keyb = Admin_keyb().start_keyb()

    await Sendler_msg().sendler_photo_message(message, LOGO, f'Приветствую тебя, хозяйка', keyb)

    return True
