from pydantic import ValidationError
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from src.models.bot_models import RequestModel, ResponseModel
from src.services.salary_service import SalaryService
from src.utils.consts import HELLO_MESSAGE, INCORRECT_REQUEST
from src.utils.date_utils import generate_labels_by
from src.utils.env_utils import ENV_SETTINGS


class BotService:
    def __init__(self, salary_service: SalaryService):
        self.bot = AsyncTeleBot(ENV_SETTINGS.TOKEN)
        self.__salary_service = salary_service
        self.__configure_bot()

    async def __start_handler(self, message: Message):
        return await self.bot.reply_to(message, HELLO_MESSAGE)

    async def __text_handler(self, message: Message):
        try:
            if not message.text:
                raise ValidationError
            request = RequestModel.model_validate_json(message.text)
            return await self.bot.reply_to(message, self.__generate_response(request).model_dump_json())
        except ValidationError:
            return await self.bot.reply_to(message, INCORRECT_REQUEST)

    def __configure_bot(self):
        self.bot.message_handler(commands=["start"])(self.__start_handler)
        self.bot.message_handler(func=lambda message: True)(self.__text_handler)

    def __generate_response(self, request: RequestModel):
        labels = generate_labels_by(request.dt_from, request.dt_upto, request.group_type)
        dataset = []
        return ResponseModel(labels=labels, dataset=dataset)
