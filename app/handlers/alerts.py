from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(commands={"alert"})
async def cmd_alert(m: Message):
    await m.answer("Алерты будут тут: /alert <часть_названия> <цена_usd>")
