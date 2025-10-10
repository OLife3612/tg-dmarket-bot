from aiogram import F


# Префиксный фильтр для callback_data типа "additem:..." и т.д.

def prefix(prefix_str: str):
    return F.data.startswith(prefix_str)
