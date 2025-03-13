import telebot; from telebot import types
import configparser
import time
import asyncio
from telebot.async_telebot import AsyncTeleBot

async def date_check(x):
    while True:
        print(time.strftime("%H:%M:%S", time.localtime()))
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
    await bot.send_message(message.chat.id, "Welcome to Kirian's VPW Bot!\n\nTo get started, type /menu.")

# Menu
@bot.message_handler(commands=["menu"])
async def menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton("🔍 Search")
    itembtn2 = types.KeyboardButton("📚 Library")
    itembtn3 = types.KeyboardButton("📖 About")
    markup.add(itembtn1, itembtn2, itembtn3)
    await bot.send_message(message.chat.id, "Main Menu", reply_markup=markup)
    inline_markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton("🔍 Search", callback_data="search")
    itembtn2 = types.InlineKeyboardButton("📚 Library", callback_data="library")
    itembtn3 = types.InlineKeyboardButton("📖 About", callback_data="about")
    inline_markup.add(itembtn1, itembtn2, itembtn3)
    await bot.send_message(message.chat.id, "Select an option from the menu.", reply_markup=inline_markup)

async def main():
    task_bot = asyncio.create_task(bot.polling())
    task_date_check = asyncio.create_task(date_check(10))

    await task_bot
    await task_date_check

asyncio.run(main())