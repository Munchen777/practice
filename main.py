import asyncio
import logging

from aiogram import Bot

from loader import dp, bot
from handlers.default_handlers.start import start_router
from handlers.custom_handlers.get_inst_picture import get_inst_router
from utils.set_bot_commands import set_all_commands
from middlewares.role import RoleMiddleware
logger = logging.getLogger('Logger')


async def set_commands(bot: Bot):
    await set_all_commands(bot)


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(start_router)
    dp.include_router(get_inst_router) # Try
    await set_commands(bot)
    dp.update.outer_middleware(RoleMiddleware())
    await dp.start_polling(bot, close_bot_session=True)


def cli():
    """Wrapper for command line"""
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")


if __name__ == '__main__':
    asyncio.run(main())
