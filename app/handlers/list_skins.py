from aiogram import Router
from aiogram.types import Message, CallbackQuery
from app import db
from app.keyboards import back_kb
from app.utils import prefix
from app.dmarket_client import DMarketClient
from app.config import settings

router = Router()


@router.message(commands={"skins"})
async def cmd_skins(m: Message):
    assert m.from_user
    rows = db.list_user_items(m.from_user.id)
    if not rows:
        await m.answer("Пока ничего не отслеживаешь. /start → Добавить")
        return
    client = DMarketClient(settings.dmarket_api_key)
    lines = []
    total = 0.0
    for _, item_id, name, url in rows:
        price = None
        # тут запрос к DMarket
        best = client.best_price_usd(market_item_id=str(item_id))  # TODO: подставь реальный id
        if best:
            price, curr = best
            total += price
        price_str = f"{price:.2f} USD" if price else "—"
        lines.append(f"• {name} — {price_str} — [ссылка]({url})")
    text = "\n".join(lines) + f"\n\n**Итого:** {total:.2f} USD"
    await m.answer(text, disable_web_page_preview=True)


@router.callback_query(prefix("skins:"))
async def cb_skins(c: CallbackQuery):
    assert c.from_user
    rows = db.list_user_items(c.from_user.id)
    if not rows:
        await c.message.edit_text("Пусто.")
        await c.answer()
        return
    await c.message.edit_text("Используй /skins для просмотра списка.", reply_markup=back_kb())
    await c.answer()
