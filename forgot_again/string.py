from datetime import datetime


def parse_float_list(lst):
    return [float(x) for x in lst.split(',')]


def now_timestamp():
    return datetime.now().isoformat().replace(":", ".")
