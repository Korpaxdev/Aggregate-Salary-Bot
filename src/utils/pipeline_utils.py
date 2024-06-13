from datetime import datetime


def _base_date_pipeline(dt_from: datetime, dt_upto: datetime):
    return [{"$sort": {"dt": 1}}, {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}}]
