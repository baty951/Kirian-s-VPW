import telebot; from telebot import types
import configparser
import time
import datetime
import asyncio
from telebot.async_telebot import AsyncTeleBot
from sql_asks import user_add_to_db

async def date_check(x):
    d = datetime.datetime.now()
    #await asyncio.sleep(x - d.hour * 3600 - d.minute * 60 - d.second)
    await bot.send_message(1217941962, "Hi!")
    while True:
        await asyncio.sleep(x)


# Config
config = configparser.ConfigParser()
config.read("config.ini")
token = config["Bot"]["token"]
# Bot
bot = AsyncTeleBot(token)

# Start
@bot.message_handler(commands=["start"])
async def start(message):
    task = asyncio.create_task(user_add_to_db(message))
    await task
    await bot.send_message(message.chat.id, "Welcome to Kirian's VPW Bot!\n\nTo get started, type /menu.\n\nIf you have any questions, type /help.")

# Menu
@bot.message_handler(commands=["help"])
async def menu(message):
    await bot.send_message(message.chat.id, "Here you can join to our group and pay for rent VDS and use it for encryption your internet traffic")

@bot.message_handler(commands=["menu"])
async def menu(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("🔐 VPN", callback_data="vpn")
    item2 = types.InlineKeyboardButton("❌ Delete message", callback_data="delete")
    item3 = types.InlineKeyboardButton("💰 Payment", callback_data="payment")
    item4 = types.InlineKeyboardButton("📞 Support", callback_data="support")
    markup.add(item1, item3, item4, item2)
    await bot.send_message(message.chat.id, "Choose what do you want:", reply_markup=markup)

async def main():
    task_bot = asyncio.create_task(bot.polling())
    task_date_check = asyncio.create_task(date_check(86400))

    await task_bot
    await task_date_check

asyncio.run(main())