from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(commands={"find"})
async def cmd_find(m: Message):
    q = (m.text or "").split(maxsplit=1)
    if len(q) == 1:
        await m.answer("Пример: /find ak fuel")
        return
    await m.answer(f"Результаты поиска по: {q[1]}\n(демо — подключи реальный поиск по DMarket)")
