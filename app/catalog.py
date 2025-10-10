from app.keyboards import simple_list_kb
from aiogram.types import InlineKeyboardMarkup

# Простой статический демо-каталог, потом заменишь на реальные данные.

CATEGORIES = {
    "root": [
        ("Винтовки", "catalog:rifles"),
    ],
    "rifles": [
        ("AK-47", "catalog:ak47"),
        ("AWP", "catalog:awp"),
    ],
    "ak47": [
        ("Fuel Injector (FN)", "additem:dmarket:AK47_FuelInjector_FN"),
        ("Fuel Injector (MW)", "additem:dmarket:AK47_FuelInjector_MW"),
        ("Fuel Injector (FT)", "additem:dmarket:AK47_FuelInjector_FT"),
    ],
    "awp": [
        ("Dragon Lore (FN?) — meme", "additem:dmarket:AWP_DragonLore_FN"),
    ]
}


def build_kb(node: str) -> InlineKeyboardMarkup:
    rows = CATEGORIES.get(node, [])
    return simple_list_kb(rows)
