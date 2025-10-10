from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📚 Каталог", callback_data="catalog:root")],
        [InlineKeyboardButton(text="🔎 Поиск", switch_inline_query_current_chat="")],
        [InlineKeyboardButton(text="🧾 Мои скины", callback_data="skins:list")],
        [InlineKeyboardButton(text="➕ Добавить по ссылке", callback_data="add:bylink")],
        [InlineKeyboardButton(text="⏰ Алерты", callback_data="alerts:menu")],
    ])


def simple_list_kb(rows):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=title, callback_data=cb)] for title, cb in rows
    ])


def back_kb(cb="menu:main"):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад", callback_data=cb)]])
