from src.services.bot_service import BotService


class App:
    def __init__(self, bot_service: BotService):
        self.bot_service = bot_service

    async def run(self):
        return await self.bot_service.bot.polling()
