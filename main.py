import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from db import Database
from keyboards import *


API_TOKEN = '5971412217:AAG1tpPOeGsWvBdtKlDtst9tTevjJ3or2gg'

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=storage)
db = Database('database.db')


class FSMfilm(StatesGroup):
    film = State()


class FSMfilm_name(StatesGroup):
    film_name = State()


class FSMsearche(StatesGroup):
    searche_number = State()


class FSMspam(StatesGroup):
    spam = State()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('Привет, ' + message.from_user.full_name +
                         '!\nДля БЕСПЛАТНОГО просмотра\nнажмите на «🔎Найти фильм/сериал» 👇', reply_markup=search)


@dp.message_handler(commands=['admin'])
async def send_welcome(message: types.Message):
    if message.from_user.id == 1912165183:
     await message.answer('Привет', reply_markup=admin)


@dp.message_handler(content_types=['text'])
async def send_button(message: types.Message):
    if message.text == 'Найти фильм/сериал 🔎':
        await FSMsearche.searche_number.set()
        await message.answer('Номер фильма')
    elif message.text == 'Случайный фильм📽':
        await message.answer('ffff')
    if message.from_user.id == 1912165183:
        if message.text == 'Рассылка':
            await message.answer('Текст для рассылки')
        elif message.text == 'Статитсика':
            await message.answer('hhh')
    else:
        await message.answer('Используй клавиатру', reply_markup=search)

@dp.message_handler(content_types='text', state=FSMsearche.searche_number)
async def searche(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        await state.finish()
        if str(data['text']).isnumeric():
            try:
                searg = db.searche_film(data['text'])
                await message.answer('Фильм называется: ' + str(searg), reply_markup=search)
            except IndexError:
                await message.answer('Такого фильма нет, попробуйте еще раз ', reply_markup=search)
        else:
            await message.answer('🚫 Не верный ввод  кода, только цифры больше нуля!', reply_markup=search)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
