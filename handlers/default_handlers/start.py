from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.contact_information import UserInfoState
from database.models import User

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    find_user = User.select().where(message.from_user.id == User.telegram_id)
    if not find_user:
        await state.set_state(UserInfoState.name)
        await message.answer( f'We are not familiar. I\'m Scrappi. What is your name?')

    else:
        await message.answer(text=f'Hello, {message.from_user.username}!\n'
                                  f'I\'m glad to see you again.)')
        await state.clear()
