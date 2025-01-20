import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import texts_14_4
from config_14_4 import *
from keyboards_14_4 import *
from crud_functions import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
database = Dispatcher(bot, storage=MemoryStorage())

@database.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'ДОбро пожаловать {message.from_user.username}' + texts_14_4.start, reply_markup=start_kb)

@database.message_handler(text='О нас')
async def price(message):
    await message.answer(texts_14_4.abaut, reply_markup=start_kb)


@database.message_handler(text='Купить')
async def get_buying_list(message):
    db_file = 'database.db'
    products = get_all_products(db_file)
    for i, product in enumerate(products):
        id, title, description, price = product
        imag_pr = texts_14_4.image_product[i]
        with open(imag_pr, 'rb') as img:
            await message.answer(f'Название: {title}| \nОписание: {description}| \nЦена: {price}', )
            await message.answer_photo(img, )
    await message.answer('Выберите продукт для покупки: ', reply_markup=catalog_kb)


@database.callback_query_handler(text='buy_jam')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(database, skip_updates=True)