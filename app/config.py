from typing import Any
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str
    DOMAIN: str

    SLACK_BOT_TOKEN: str
    SLACK_APP_TOKEN: str
    SLACK_CLIENT_ID: str
    SLACK_CLIENT_SECRET: str

    SCOPE: list[str]
    JSON_KEYFILE_DICT: dict[str, Any]
    SPREAD_SHEETS_URL: str
    DEPOSIT_SHEETS_URL: str
    SECRET_KEY: str

    SUPPORT_CHANNEL: str
    COFFEE_CHAT_PROOF_CHANNEL: str
    ADMIN_CHANNEL: str
    ADMIN_IDS: list[str]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()  # type: ignore
