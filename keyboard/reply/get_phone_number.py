from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_phone() -> ReplyKeyboardMarkup:
    kb = [[KeyboardButton(text=f'Touch to send a contact.', request_contact=True)]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                   row_width=1, one_time_keyboard=True)
    return keyboard
