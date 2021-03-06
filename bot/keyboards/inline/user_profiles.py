# - *- coding: utf- 8 - *-
from utils.db_api.sqlite import get_userx, get_purchasesx


def get_user_profile(user_id):
    get_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = f"<b>π Your profile:</b>\n" \
          f"βββββββββββββ\n" \
          f"π My ID: <code>{get_user[1]}</code>\n" \
          f"π€ Login: <b>@{get_user[2]}</b>\n" \
          f"π Registration: <code>{get_user[6]}</code>\n" \
          f"βββββββββββββ\n" \
          f"π³ Balance: <code>{get_user[4]}rub</code>\n" \
          f"π΅ Total replenished: <code>{get_user[5]}rub</code>\n" \
          f"π Purchased goods: <code>{count_items}piece</code>"
    return msg


def search_user_profile(user_id):
    get_status_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = f"<b>π ΠΡΠΎΡΠΈΠ»Ρ ΠΏΠΎΠ»ΡΠ·ΠΎΠ²Π°ΡΠ΅Π»Ρ:</b> <a href='tg://user?id={get_status_user[1]}'>{get_status_user[3]}</a>\n" \
          f"βββββββββββββ\n" \
          f"π ID: <code>{get_status_user[1]}</code>\n" \
          f"π€ ΠΠΎΠ³ΠΈΠ½: <b>@{get_status_user[2]}</b>\n" \
          f"β ΠΠΌΡ: <a href='tg://user?id={get_status_user[1]}'>{get_status_user[3]}</a>\n" \
          f"π Π Π΅Π³ΠΈΡΡΡΠ°ΡΠΈΡ: <code>{get_status_user[6]}</code>\n" \
          f"βββββββββββββ\n" \
          f"π³ ΠΠ°Π»Π°Π½Ρ: <code>{get_status_user[4]}ΡΡΠ±</code>\n" \
          f"π΅ ΠΡΠ΅Π³ΠΎ ΠΏΠΎΠΏΠΎΠ»Π½Π΅Π½ΠΎ: <code>{get_status_user[5]}ΡΡΠ±</code>\n" \
          f"π ΠΡΠΏΠ»Π΅Π½ΠΎ ΡΠΎΠ²Π°ΡΠΎΠ²: <code>{count_items}ΡΡ</code>\n"
    return msg
