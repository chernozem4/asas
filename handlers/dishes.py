
from aiogram import Router, F, types
dishes_router = Router()

@dishes_router.message(F.text == "pizza")
async def horror_handler(message: types.Message):
    await message.answer("пепперони")
    await message.answer("маргарита")
    await message.answer("4 сезона")
    await message.answer("с грибами")
    await message.answer("5 сыров")

