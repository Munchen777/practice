from aiogram import Router, F
from loader import bot, dp
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from database.models import User
from handlers.default_handlers.start import start_router
from keyboard.reply.get_phone_number import get_phone
from states.contact_information import UserInfoState


@start_router.message(UserInfoState.name)
async def get_name(message: Message, state: FSMContext):

    await state.set_state(UserInfoState.phone_number)
    if message.text.isalpha():
        name = message.text
        await state.update_data(name=name)
        await message.answer(f'Thanks a lot. Please, insert your phone number.',
                             reply_markup=get_phone())

    else:
        await message.answer(f'A name should be made off letters.')


@start_router.message(UserInfoState.phone_number)
async def get_contact(message: Message, state: FSMContext):

    await state.update_data(phone_number=message.contact.phone_number)
    await message.answer(f'Thank you for full information.',
                         reply_markup=ReplyKeyboardRemove())
    user_data = await state.get_data()
    User.create(
        telegram_id=message.from_user.id,
        name=user_data["name"],
        phone=user_data['phone_number']
    ).save()

    await state.clear()

