from aiogram import Router
from aiogram.types import Message, CallbackQuery
from app.keyboards import main_menu_kb
from app import db

router = Router()


@router.message(commands={"start"})
async def cmd_start(m: Message):
    assert m.from_user
    db.ensure_user(m.from_user.id)
    await m.answer(
        "Привет! Добавь скины через каталог/поиск/ссылку — и я покажу общую сумму в USD.",
        reply_markup=main_menu_kb(),
    )


@router.callback_query(lambda c: c.data == "menu:main")
async def cb_main_menu(c: CallbackQuery):
    await c.message.edit_text(
        "Главное меню:", reply_markup=main_menu_kb()
    )
    await c.answer()
