from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


class Admin_keyb:
    def start_keyb(self):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'🚫️ Стоп слова', callback_data='stop'))

        return self._start_key

    def stop(self):
        core_keyb = InlineKeyboardMarkup(row_width=1)

        core_keyb.add(InlineKeyboardButton(text=f'➕ Добавить слово', callback_data='add_stop'))

        core_keyb.add(InlineKeyboardButton(text=f'🔙 Назад', callback_data='admin_pamel'))

        return core_keyb

    def back_add_words(self):
        core_keyb = InlineKeyboardMarkup(row_width=1)

        core_keyb.add(InlineKeyboardButton(text=f'🔙 Назад', callback_data='stop'))

        return core_keyb
