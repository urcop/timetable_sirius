from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(deep_link='383212537'))
async def teacher_link(message: types.Message):
    text = (f'Здравствуйте, {message.from_user.full_name}!',
            '<b>Пожалуйста пройдите небольшую регистрацию</b>',
            '<b>Это займет буквально одну минуту!</b>')
    await message.answer("\n".join(text))


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
