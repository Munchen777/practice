from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_all_commands(bot: Bot):
    return await bot.set_my_commands([
        BotCommand(command='start', description='start_session'),
        BotCommand(command='help', description='help_with_navigation'),
        BotCommand(command='test', description='test_command')

    ],
        scope=BotCommandScopeDefault()
)
