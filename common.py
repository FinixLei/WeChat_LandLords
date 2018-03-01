import copy
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

MIN_SINGLE_CARDS = 5
MIN_PAIRS = 3
MIN_TRIPLES = 2

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


class GenAnyN(object):
    """
    Get any N cards from a card list
    Usage:
        gan = GenAnyN(a_card_list, n)
        n_cards_lists = gan.gen_n_cards_lists()
    """
    def __init__(self, array, count):
        self.array = array
        self.count = count
        self.all_listed = list()
        self.final_result = list()

    def _get_any_n(self, array, count, result=list()):
        if count == 0:
            tmp_result = copy.deepcopy(result)
            self.all_listed.append(tmp_result)
            return

        for i in array:
            new_array = copy.deepcopy(array)
            new_array.remove(i)
            result.append(i)
            self._get_any_n(new_array, count - 1, result)
            result.remove(i)

    def gen_n_cards_lists(self):
        array = copy.deepcopy(self.array)
        count = self.count
        self._get_any_n(array, count)

        tmp_result = [sorted(item) for item in self.all_listed]
        duplicated = list()
        i = 0
        while i < len(tmp_result) - 1:
            j = i + 1
            while j < len(tmp_result):
                if tmp_result[i] == tmp_result[j]:
                    duplicated.append(j)
                j += 1
            i += 1

        self.final_result = list()
        for i in range(len(tmp_result)):
            if i not in duplicated:
                self.final_result.append(tmp_result[i])

        return self.final_result
