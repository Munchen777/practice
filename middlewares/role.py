from typing import Callable, Any, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from filters.role import AdminCheckRole


class RoleMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable,
                       event: TelegramObject,
                       data: Dict[str, Any]
                       ):
        user = data['event_from_user']
        print('Вызвался мидлвари')
        result = AdminCheckRole()(user.id)
        if result:
            print('Вы админ.')
            return await handler(event, data)
        else:
            print('Вы не админ.')
