from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot_config import database


review_dialog_router = Router()

# FSM - Finite State Machine
class RestourantReview(StatesGroup):
    name = State()
    age = State()
    food = State()
    opinion = State()

@review_dialog_router.message(Command("review"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await message.answer("Как Вас зовут?")


@review_dialog_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    print(message.text)

    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.age)
    await message.answer("Ваш возраст?")




@review_dialog_router.message(RestourantReview.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Вводите только цифры")
        return
    age = int(age)
    if age < 7 or age > 122:
        await message.answer("Некорректный возраст")
        return
    await state.set_state(RestourantReview.food)
    await state.update_data(age=message.text)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="вкусно"),
                types.KeyboardButton(text="невкусно")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Как вам еда?", reply_markup=kb)




@review_dialog_router.message(RestourantReview.food)
async def process_food_quality(message: types.Message, state: FSMContext):
    await state.update_data(food=message.text)
    await state.set_state(RestourantReview.opinion)
    await message.answer("Пожалуйста, оставьте ваш отзыв о ресторане", reply_markup=types.ReplyKeyboardRemove())


@review_dialog_router.message(RestourantReview.opinion)
async def process_opinion(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    await database.execute('''INSERT INTO review(name, age, food, opinion) VALUES ( ?, ?, ?, ?)''',
               (data['name'], data['age'], data['food'], data['opinion']))
    await state.update_data(opinion=message.text)
    await state.clear()
    await message.answer("Спасибо за пройденный опрос")
