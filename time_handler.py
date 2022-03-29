"""Time converter logic"""
from datetime import datetime


intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)


def time_to_num(time_str: str) -> int:
    """Converting from datetime.now() obj to integer so we can pass to
    your display_time_func"""
    hh, mm, ss = map(int, time_str.split(':'))
    return ss + 60*(mm + 60*hh)


def display_time(seconds: int, granularity: int = 3) -> int:
    """Time convertion function. From seconds to hour, minutes, seconds
    Granularity=3 [Hours, minutes, seconds]"""
    if seconds <= 0:
        return "Please provide correct values"
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])
