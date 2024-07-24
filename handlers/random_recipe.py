from aiogram.filters.command import Command
from aiogram import types
import random
from aiogram.filters import command
from aiogram import Dispatcher

async def random_recipe(message: types.Message):
    recipes = [
        "Рецепт 1: \n1. Ингредиент А\n2. Ингредиент Б\n3. Ингредиент В\n4. Приготовление: смешать все и готовить 20 минут.",
        "Рецепт 2: \n1. Ингредиент Г\n2. Ингредиент Д\n3. Ингредиент Е\n4. Приготовление: запекать при 180 градусах 30 минут.",
        "Рецепт 3: \n1. Ингредиент Ж\n2. Ингредиент З\n3. Ингредиент И\n4. Приготовление: варить 10 минут на слабом огне.",
        "Рецепт 4: \n1. Ингредиент К\n2. Ингредиент Л\n3. Ингредиент М\n4. Приготовление: обжарить на среднем огне 15 минут.",
        "Рецепт 5: \n1. Ингредиент Н\n2. Ингредиент О\n3. Ингредиент П\n4. Приготовление: тушить 25 минут под крышкой."
    ]
    await message.reply(f"Вот случайный рецепт: {random.choice(recipes)}")



def register_handlers(dp: Dispatcher):
    dp.message(Command('random_recipe'))(random_recipe)