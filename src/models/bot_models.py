from datetime import datetime

from pydantic import BaseModel

from src.utils.type_utils import By


class RequestModel(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: By


class ResponseModel(BaseModel):
    labels: list[datetime]
    dataset: list[int]
