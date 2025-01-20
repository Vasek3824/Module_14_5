import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config_14_5 import *
from crud_functions_14_5 import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
database = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup([[KeyboardButton(text='Регистрация')]], resize_keyboard = True)

class RegistrationState(StatesGroup):
    username = State()
    email  = State()
    age = State()
    balance = State()

@database.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Добро пожаловать {message.from_user.username}', reply_markup=kb)

@database.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит): ')
    await RegistrationState.username.set()

@database.message_handler(state=RegistrationState.username)
async  def set_username(message, state):
    dbUser = 'database.db'
    if message.text:
        if not is_included(dbUser, username=message.text):
            await state.update_data(username=message.text)
            await message.answer('Введите свой email:')
            await RegistrationState.email.set()
        else:
            await message.answer('Пользователь существует, введите другое имя')
    else:
        await message.answer('Имя пользователя не может быть пустым. Пожалуйста, введите имя:')

@database.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await  message.answer('Введите свой возраст: ')
    await RegistrationState.age.set()

@database.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    dbUser = 'database.db'
    await  state.update_data(age = int(message.text))
    data = await state.get_data()
    add_user(dbUser, data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно!')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(database, skip_updates=True)
