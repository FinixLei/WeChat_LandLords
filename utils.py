# coding=utf-8

import copy
import time
from functools import wraps

s2v = {
    '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'j': 11,
    'Q': 12, 'q': 12,
    'K': 13, 'k': 13,
    'A': 14, 'a': 14,
    '2': 18, 2: 18,
    'Y': 20, 'y': 20, '小王': 20,
    'Z': 30, 'z': 30, '大王': 30

}

v2s = {
    3: '3', 4: '4', 5: '5', 6: '6',
    7: '7', 8: '8', 9: '9', 10: '10',
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
    18: '2',
    20: '小王',
    30: '大王'
}

MIN_SINGLE_CARDS = 5
MIN_PAIRS = 3
MIN_TRIPLES = 2


def validate_cards(cards):
    for card in cards:
        if card not in s2v.keys():
            return False
    return True


def format_input_cards(cards):
    return sorted([s2v[i] if i in s2v else i for i in cards])


def format_output_cards(cards):
    return sorted([v2s[i] if i in v2s else i for i in cards])


def calc_time(fn):
    @wraps(fn)
    def wrapper(*args, **kw):
        begin = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print("Calc Time: %.2f seconds" % (end-begin))
        return result
    return wrapper


def print_func_name(fn):
    @wraps(fn)
    def wrapper(*args, **kw):
        print("--- %s ---" % fn.__name__)
        result = fn(*args, **kw)
        print("-" * 50)
        return result
    return wrapper


def get_rest_cards(cards, move):
    """
    :param cards: a list, current cards
    :param move: a list, current move
    :return: rest_cards, a list, rest cards
    """
    rest_cards = copy.deepcopy(cards)
    current_move = copy.deepcopy(move)
    while len(current_move) > 0:
        if current_move[0] in rest_cards:
            rest_cards.remove(current_move[0])
            current_move.remove(current_move[0])
        else:
            raise Exception("move is not a sub set of cards")
    return rest_cards


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


def show_situation(lorder_cards=(), farmer_cards=list(),
                   move=list(), next_player=''):
    print("Move is: %s" % format_output_cards(move))
    print("lorder cards: %s" % format_output_cards(lorder_cards))
    print("farmer cards: %s" % format_output_cards(farmer_cards))
    print("Next player: %s" % next_player)
    print("-" * 20)


def check_win(cards, role):
    if len(cards) == 0:
        print('%s win!' % role)
        return True
    return False
