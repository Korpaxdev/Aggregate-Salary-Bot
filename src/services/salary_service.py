from datetime import datetime

from services.database_service import DatabaseService
from utils.type_utils import By


class SalaryService:
    def __init__(self, database_service: DatabaseService):
        self.__collection = database_service.db["sample_collection"]

    def get_salaries_by(self, dt_from: datetime, dt_upto: datetime, by: By):
        pass
