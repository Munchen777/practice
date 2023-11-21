import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
# RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота."),
    ("help", "Вывести справку."))
#     ('survey', 'Опрос.'),
#     ('history', 'Ваша история запросов.'),
#     ('low', 'Фильм с наименьшим рейтингом IMDb.'),
#     ('high', 'Фильм с наивысшим рейтингом IMDb.'),
#     ('definite_year', 'Фильм с определенным годом съемки.')
# )
DB_PATH = 'for_async_db.db'

import configparser
from dataclasses import dataclass


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_id: int
    use_redis: bool


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config["tg_bot"]

    return Config(
        tg_bot=TgBot(
            token=tg_bot.get("token"),
            admin_id=tg_bot.getint("admin_id"),
            use_redis=tg_bot.getboolean("use_redis"),
        ),
        db=DbConfig(**config["db"]),
    )