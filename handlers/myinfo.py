from aiogram.filters.command import Command
from aiogram import types
from aiogram import Dispatcher
from aiogram import Router

my_info_router = Router()

async def send_myinfo(message: types.Message):
    user_info = (
        f"Ваш ID: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш username: {message.from_user.username}"
    )
    await message.reply(user_info)

def register_handlers(dp: Dispatcher):
     dp.message(Command('myinfo'))(send_myinfo)




