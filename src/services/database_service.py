from motor.motor_asyncio import AsyncIOMotorClient

from src.utils.env_utils import ENV_SETTINGS


class DatabaseService:
    __URI = f"mongodb://{ENV_SETTINGS.DB_USERNAME}:{ENV_SETTINGS.DB_PASSWORD}@localhost:27017"

    def __init__(self):
        self.__client = AsyncIOMotorClient(self.__URI)
        self.db = self.__client[ENV_SETTINGS.DB]
