# tg-dmarket-bot (MVP)

## Установка
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
# впиши ключи
python -m app.main
```

## Команды

* /start — меню
* /add <url> — добавить по ссылке DMarket (каркас)
* /find <query> — поиск (демо)
* /skins — список отслеживаемых + сумма
* /alert — настроить алерт (каркас)
