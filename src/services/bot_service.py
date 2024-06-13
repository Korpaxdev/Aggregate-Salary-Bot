from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from src.services.salary_service import SalaryService
from src.utils.consts import HELLO_MESSAGE
from src.utils.env_utils import ENV_SETTINGS


class BotService:
    def __init__(self, salary_service: SalaryService):
        self.bot = AsyncTeleBot(ENV_SETTINGS.TOKEN)
        self.__salary_service = salary_service
        self.__configure_bot()

    async def __hello_handler(self, message: Message):
        return await self.bot.reply_to(message, HELLO_MESSAGE)

    def __configure_bot(self):
        self.bot.message_handler(commands=["start"])(self.__hello_handler)
