from datetime import datetime

from src.utils.type_utils import By


def _base_date_pipeline(dt_from: datetime, dt_upto: datetime):
    return [{"$sort": {"dt": 1}}, {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}}]


def by_month_pipeline(dt_from: datetime, dt_upto: datetime):
    return [
        *_base_date_pipeline(dt_from, dt_upto),
        {
            "$group": {
                "_id": {
                    "$dateFromParts": {
                        "year": {"$year": "$dt"},
                        "month": {"$month": "$dt"},
                    }
                },
                "sum": {"$sum": "$value"},
            }
        },
        {"$sort": {"_id": 1}},
    ]


def get_date_pipeline(dt_from: datetime, dt_upto: datetime, by: By):
    match (by):
        case "month":
            return by_month_pipeline(dt_from, dt_upto)
        case _:
            raise NotImplementedError
