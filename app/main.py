import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import settings
from app.handlers import start, add, list_skins, alerts, search

logging.basicConfig(level=getattr(logging, settings.log_level, logging.INFO))


async def main():
    if not settings.bot_token:
        raise RuntimeError("BOT_TOKEN не задан в .env")
    bot = Bot(settings.bot_token, parse_mode="Markdown")
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)
    dp.include_router(add.router)
    dp.include_router(list_skins.router)
    dp.include_router(alerts.router)
    dp.include_router(search.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
