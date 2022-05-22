# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import payments_enabled


# Проверка оплаты киви
def create_pay_func(send_requests, receipt, message_id, way):
    check_pay_inl = InlineKeyboardMarkup()
    check_pay_inl.add(InlineKeyboardButton(text="🌀 Go to the payment", url=send_requests))
    check_pay_inl.add(InlineKeyboardButton(text="🔄 Check payment",
                                           callback_data=f"Pay:{way}:{receipt}:{message_id}"))
    return check_pay_inl


# Кнопки выбора оплаты
def choose_pay_type_func(user_id):
    pay_type = InlineKeyboardMarkup()
    if "qiwi" in payments_enabled:
        pay_type.add(InlineKeyboardButton(text="🥝 Qiwi", callback_data="pay_type:qiwi"))
    if "crystal" in payments_enabled:
        pay_type.add(InlineKeyboardButton(text="💎 CrystalPay", callback_data="pay_type:crystal_pay"))
    return pay_type


# Кнопки при открытии самого товара
def open_item_func(position_id, remover, category_id):
    open_item = InlineKeyboardMarkup()
    open_item.add(InlineKeyboardButton(text="💳 Buy item",
                                       callback_data=f"buy_this_item:{position_id}"))
    open_item.add(InlineKeyboardButton("⬅ Back ↩",
                                       callback_data=f"back_buy_item_position:{remover}:{category_id}"))
    return open_item


# Подтверждение покупки товара
def confirm_buy_items(position_id, get_count, message_id):
    confirm_buy_item_keyboard = InlineKeyboardMarkup()
    yes_buy_kb = InlineKeyboardButton(text="✅ Confirm",
                                      callback_data=f"xbuy_item:{position_id}:{get_count}:{message_id}")
    not_buy_kb = InlineKeyboardButton("❌ Cancel",
                                      callback_data=f"not_buy_items:{message_id}")
    confirm_buy_item_keyboard.add(yes_buy_kb, not_buy_kb)
    return confirm_buy_item_keyboard
