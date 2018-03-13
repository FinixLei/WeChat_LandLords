import multiprocessing

from utils import format_input_cards, get_rest_cards, calc_time
from move_player import get_resp_moves
from move_classifier import MoveClassifier

MAX_SCORE = 100
MIN_SCORE = 0

mc_records = list()
m_class = MoveClassifier()


def process_search(lorder_cards, farmer_cards, current_move, next_player):
    score = minmax_search(lorder_cards, farmer_cards, current_move, next_player)
    print("Move: %s; Score: %d" % (current_move, score))


def minmax_search(lorder_cards, farmer_cards, current_move, next_player):
    global m_class

    if next_player == 'farmer':
        if len(lorder_cards) == 0:
            return MAX_SCORE  # lorder win, return MAX_SCORE

    elif next_player == 'lorder':
        if len(farmer_cards) == 0:
            return MIN_SCORE  # farmer win, return MIN_SCORE

    if next_player == 'farmer':  # the parameter next_player is current player
        score = MAX_SCORE  # For farmer, the default score is MAX_SCORE
        all_moves = get_resp_moves(farmer_cards, current_move)
        # a kind of optimization
        all_moves = sorted(all_moves, key=lambda x: len(x), reverse=True)
        for farmer_move in all_moves:
            fc = get_rest_cards(farmer_cards, farmer_move)
            score = minmax_search(lorder_cards,
                                  fc,
                                  farmer_move,
                                  'lorder')
            # Current player is farmer, so once finds MIN_SCORE, he must choose it.
            # Cut Branches! Ignore the rest farmer moves.
            if score == MIN_SCORE:
                break
        return score

    else:  # next_player is 'lorder', the parameter next_player is current player
        score = MIN_SCORE  # For 'lorder', the default value is MIN_SCORE
        all_moves = get_resp_moves(lorder_cards, current_move)
        # a kind of optimization
        all_moves = sorted(all_moves, key=lambda x: len(x), reverse=True)
        for lorder_move in all_moves:
            lc = get_rest_cards(lorder_cards, lorder_move)
            score = minmax_search(lc,
                                  farmer_cards,
                                  lorder_move,
                                  'farmer')
            # Current player is lorder. So, once MAX_SCORE, choose it!
            # Cut Branches! Ignore the rest lorder moves.
            if score == MAX_SCORE:
                break
        return score


@calc_time
def start_engine(lorder_cards=list(), farmer_cards=list(), farmer_move=list()):
    process_pool = []
    lorder_cards = format_input_cards(lorder_cards)
    farmer_cards = format_input_cards(farmer_cards)
    farmer_move = format_input_cards(farmer_move)

    all_lorder_moves = get_resp_moves(format_input_cards(lorder_cards), farmer_move)
    # a kind of optimization
    all_lorder_moves = sorted(all_lorder_moves, key=lambda x: len(x), reverse=True)
    print("All Moves: %s" % all_lorder_moves)

    for move in all_lorder_moves:
        record = {'move': move,
                  'farmer_win': 0,
                  'lorder_win': 0}
        mc_records.append(record)

        lc = get_rest_cards(lorder_cards, move)
        p = multiprocessing.Process(target=process_search,
                                    args=(lc, farmer_cards, move, 'farmer'))
        process_pool.append(p)

    for p in process_pool:
        p.start()
    for p in process_pool:
        p.join()
