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
            response = await self.__generate_response(request)
            return await self.bot.reply_to(message, response.model_dump_json())
        except ValidationError as e:
            for err in e.errors():
                if err["type"] == "value_error":
                    if not err["loc"] or err["loc"][0] in ("dt_upto", "dt_from"):
                        err_msg = err["msg"] or INCORRECT_REQUEST
                else:
                    err_msg = INCORRECT_REQUEST
                return await self.bot.reply_to(message, err_msg)

    def __configure_bot(self):
        self.bot.message_handler(commands=["start", "help"])(self.__start_handler)
        self.bot.message_handler(func=lambda message: True)(self.__text_handler)

    async def __generate_response(self, request: RequestModel):
        labels = generate_labels_by(request.dt_from, request.dt_upto, request.group_type)
        dataset = []
        aggregated_salaries = dict()
        async for doc in self.__salary_service.get_salaries_by(request.dt_from, request.dt_upto, request.group_type):
            aggregated_salaries[doc["_id"]] = doc["sum"]
        for label in labels:
            dataset.append(aggregated_salaries.get(label, 0))
        return ResponseModel(labels=labels, dataset=dataset)
