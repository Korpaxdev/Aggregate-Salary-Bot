from datetime import datetime

from pydantic import BaseModel, field_validator, model_validator

from src.utils.type_utils import By


class RequestModel(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: By

    @model_validator(mode="after")
    def validate_group_type(cls, values):
        if values.dt_from > values.dt_upto:
            raise ValueError("dt_from не может быть больше dt_upto")
        return values

    @field_validator("dt_from")
    def validate_dt_from(cls, value):
        if value > datetime.now():
            raise ValueError("dt_from не может быть больше текущей даты")
        return value

    @field_validator("dt_upto")
    def validate_dt_upto(cls, value):
        if value > datetime.now():
            raise ValueError("dt_upto не может быть больше текущей даты")
        return value


class ResponseModel(BaseModel):
    dataset: list[int]
    labels: list[datetime]
