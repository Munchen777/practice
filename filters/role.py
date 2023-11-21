import typing
import os
from aiogram.filters import BaseFilter

from aiogram.types.base import TelegramObject
from models.role import UserRole


class AdminCheckRole(BaseFilter):
    def __init__(self):
        self.admin = int(os.getenv('ADMIN_ID'))

    def __call__(self, some_id):
        return some_id == self.admin
