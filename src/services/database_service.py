from motor.motor_asyncio import AsyncIOMotorClient

from utils.env_utils import ENV_SETTINGS


class DatabaseService:
    __URI = f"mongodb://{ENV_SETTINGS.DB_USERNAME}:{ENV_SETTINGS.DB_PASSWORD}@localhost:27017"
    __instance = None

    def __init__(self):
        self.__client = AsyncIOMotorClient(self.__URI)
        self.__db = self.__client[ENV_SETTINGS.DB]
        self.__collections = self.__db["sample_collection"]

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(DatabaseService, cls).__new__(cls)
        return cls.__instance
