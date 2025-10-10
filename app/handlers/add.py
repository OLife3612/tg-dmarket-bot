from aiogram import Router
from aiogram.types import CallbackQuery, Message
from app.keyboards import back_kb
from app.utils import prefix
from app import db

router = Router()


@router.callback_query(lambda c: c.data == "add:bylink")
async def cb_add_link(c: CallbackQuery):
    await c.message.edit_text(
        "Кинь мне ссылку на предмет с DMarket — добавлю его в отслеживание.",
        reply_markup=back_kb(),
    )
    await c.answer()


@router.message()
async def catch_link(m: Message):
    if not m.text:
        return
    text = m.text.strip()
    if not text.startswith("http"):
        return
    # TODO: распарсить URL, достать стабильный market_item_id, название, wear.
    # Пока — фейковый парсинг.
    market_item_id = text  # временно храним саму ссылку как id
    name = "DMarket Item"
    url = text
    item_id = db.upsert_item(
        market="dmarket", market_item_id=market_item_id, name=name, url=url
    )
    assert m.from_user
    db.add_user_item(m.from_user.id, item_id)
    await m.reply("Добавил! Посмотри /skins")
