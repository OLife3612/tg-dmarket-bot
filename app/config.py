from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseModel):
    bot_token: str = os.getenv("BOT_TOKEN", "")
    dmarket_api_key: str = os.getenv("DMARKET_API_KEY", "")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
