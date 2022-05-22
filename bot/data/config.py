# - *- coding: utf- 8 - *-
import configparser

config = configparser.ConfigParser()
config.read('settings.ini', encoding='utf-8')
BOT_TOKEN = config["settings"]["token"]
admins = config["settings"]["admin_id"]
crystal_name = config["crystal"]["nickname"]
crystal_secret = config["crystal"]["secret_1"]
payments_enabled = config["payments"]["enabled"]

payments_enabled = payments_enabled.replace(" ", "").split(",")

if len(payments_enabled) == 0:
    print("❌ You did not specify the included payment systems! Please indicate at least one!")

if "," in admins:
    admins = admins.replace(" ", "").split(",")
else:
    if len(admins) >= 1:
        admins = [admins]
    else:
        admins = []
        print("❌ You didn't specify bot admins!")

bot_version = "2.9"
bot_description = f"<b>♻ Bot created by @SlimyAdmin</b>\n" \
