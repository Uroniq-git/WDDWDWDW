# - *- coding: utf- 8 - *-
from aiogram.dispatcher.filters.state import State, StatesGroup


class StorageQiwi(StatesGroup):
    here_input_qiwi_secret = State()
    here_input_qiwi_login = State()
    here_input_qiwi_token = State()
    here_input_qiwi_amount = State()


class StorageCrystal(StatesGroup):
    here_input_crystal_amount = State()


class StoragePayType(StatesGroup):
    here_input_pay_type = State()
