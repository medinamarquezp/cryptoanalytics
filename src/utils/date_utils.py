from datetime import datetime

def date_from_timestamp(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp)

def parsed_date_from_timestamp(timestamp: int, include_time=False) -> str:
    date = date_from_timestamp(timestamp)
    date_format = "%Y-%m-%d %H:%M:%S" if include_time else "%Y-%m-%d"
    return date.strftime(date_format)

def is_today_timestamp(timestamp: int) -> bool:
    today = datetime.today()
    date = date_from_timestamp(timestamp)
    return today.date() == date.date()

def days_till_today(date: datetime) -> int:
    today = datetime.today()
    return (today - date).days