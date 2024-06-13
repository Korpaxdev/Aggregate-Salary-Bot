from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DB: str
    DB_USERNAME: str
    DB_PASSWORD: str
    TOKEN: str


ENV_SETTINGS = _Settings()  # type: ignore
