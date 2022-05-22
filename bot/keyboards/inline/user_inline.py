# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки при поиске профиля через админ-меню
open_profile_inl = InlineKeyboardMarkup()
input_kb = InlineKeyboardButton(text="💳 Refill the balance", callback_data="user_input")
mybuy_kb = InlineKeyboardButton(text="📦 My purchases", callback_data="my_buy")
open_profile_inl.add(input_kb, mybuy_kb)

# Кнопка с возвратом к профилю
to_profile_inl = InlineKeyboardMarkup()
to_profile_inl.add(InlineKeyboardButton(text="🛍 Profile", callback_data="user_profile"))
