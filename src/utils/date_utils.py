from datetime import datetime

from dateutil.relativedelta import relativedelta

from src.utils.type_utils import By


def generate_labels_by(dt_from: datetime, dt_upto: datetime, by: By):
    current_date = dt_from
    date_list = []
    by_mapper = {"hour": "hours", "day": "days", "month": "months"}

    while current_date <= dt_upto:
        date_list.append(current_date)
        current_date += relativedelta(**{by_mapper[by]: 1})  # type: ignore

    return date_list
