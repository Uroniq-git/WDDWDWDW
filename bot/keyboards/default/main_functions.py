# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup


def get_functions_func(user_id):
    functions_default = ReplyKeyboardMarkup(resize_keyboard=True)
    functions_default.row("📱 Поиск профиля 🔍", "📢 Рассылка", "📃 Поиск чеков 🔍")
    functions_default.row("⬅ Home")
    return functions_default
