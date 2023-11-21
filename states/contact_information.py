from aiogram.fsm.state import State, StatesGroup


class UserInfoState(StatesGroup):
    name = State()
    phone_number = State()


class UserInstPicture(StatesGroup):
    url = State()
    get_picture = State()
