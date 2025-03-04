import re
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatPermissions
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from dotenv import load_dotenv



load_dotenv()
TOKEN = "7562892913:AAFEJq-dm0FbIDlsKQRzB5daABtiKA06Yuo" # Токен бота

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Хэндлер на старт
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет! меня зовут Ньютон, я антиспам-бот, буду следить за порядком в вашей группе или канале. 👮‍")

# Асинхронный запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())  # Запуск бота

    from flask import Flask
    from threading import Thread

    app = Flask(__name__)


    @app.route('/')
    def home():
        return "Бот работает!"


    def run():
        app.run(host="0.0.0.0", port=10000)


    Thread(target=run).start()
