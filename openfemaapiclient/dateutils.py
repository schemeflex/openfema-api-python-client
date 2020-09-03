from datetime import datetime

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


def try_extract_date(value):
    return datetime.strptime(value, DATE_FORMAT) if value else value
