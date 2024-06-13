import asyncio

from src.app import App
from src.services.bot_service import BotService
from src.services.database_service import DatabaseService
from src.services.salary_service import SalaryService

if __name__ == "__main__":
    app = App(BotService(SalaryService(DatabaseService())))
    asyncio.run(app.run())
