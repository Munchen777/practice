import requests
from bs4 import BeautifulSoup
from aiogram import Router, F

from aiogram.filters import StateFilter, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
# from database.models import User

from states.contact_information import UserInstPicture


get_inst_router = Router()


@get_inst_router.message(Command('get_instagram_picture'))
async def get_user_url(message: Message, state: FSMContext):
    await state.set_state(UserInstPicture.url)
    await message.answer(f'Please, send an Instagram url.')


@get_inst_router.message(UserInstPicture.url)
async def url(message, state: FSMContext):
    await state.update_data(url=message.text)
    # req = requests.get()
    # soup = BeautifulSoup(req.text, 'lxml')
    # media = soup.find('div', class_='stk-subcategory__item-container')
    # print(media)
    await state.clear()

