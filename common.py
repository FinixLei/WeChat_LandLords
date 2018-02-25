import time
from functools import wraps

s2v = {
    'J': 11, 'j': 11,
    'Q': 12, 'q': 12,
    'K': 13, 'k': 13,
    'A': 14, 'a': 14,
    '2': 18, 2: 18,
    'Y': 20, 'y': 20,
    'Z': 30, 'z': 30
}

v2s = {
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
    18: 2,
    20: 'Y',
    30: 'Z'
}


def format_input(cards_list):
    return sorted([s2v[i] if i in s2v else i for i in cards_list])


def calc_time(fn):
    @wraps(fn)
    def wrapper(*args, **kw):
        begin = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print("Time cost of %s: %s" % (fn.__name__, end - begin))
        return result
    return wrapper
