# TG DMarket Bot

Этот проект представляет собой пример телеграм‑бота на основе `aiogram` для
отслеживания цен на предметы из CS2 на платформе DMarket. Пользователь может
добавлять ссылки на предметы с DMarket, и бот будет отображать текущую цену
каждого предмета, а также суммировать их стоимость.

## Запуск локально

1. Склонируйте репозиторий и создайте виртуальное окружение:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Создайте файл `.env` на основе `.env.example` и заполните значения:

   ```env
   BOT_TOKEN=your_telegram_bot_token
   DMARKET_API_KEY=your_dmarket_api_key
   DATABASE_URL=sqlite+aiosqlite:///db.sqlite3
   ```

3. Инициализируйте базу данных (это можно сделать при первом запуске):

   ```python
   from app.repo import init_db
   import asyncio
   asyncio.run(init_db())
   ```

4. Запустите бот:

   ```bash
   python -m app.main
   ```

Бот работает в режиме *polling*, поэтому его можно разместить локально. Для
продакшн‑окружения рекомендуется переключиться на webhooks.

## Структура проекта

- `app/main.py` — точка входа, инициализирует dispatcher и регистрирует
  команды.
- `app/dmarket_client.py` — обёртка над API DMarket. Требует заполнить
  метод `get_best_price`.
- `app/repo.py` — функции для работы с SQLite: создание таблиц, добавление
  предметов и получение списка отслеживаемых предметов.
- `app/handlers/` — хэндлеры aiogram для команд `/start`, `/add` и `/skins`.

## TODO

- Реализовать метод `get_best_price` для реального получения цен через
  DMarket API.
- Добавить поиск предметов через inline‑кнопки.
- Настроить алерты по заданной цене.