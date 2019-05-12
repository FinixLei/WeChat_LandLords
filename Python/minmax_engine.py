import multiprocessing

from utils import format_input_cards, format_output_cards, get_rest_cards, calc_time
from move_player import get_resp_moves
from move_classifier import MoveClassifier

MAX_SCORE = 100
MIN_SCORE = 0

nodes_num = 0
mc_records = list()
m_class = MoveClassifier()


@calc_time
def process_search(index, result_dict,
                   lorder_cards, farmer_cards, current_move, next_player):
    score = minmax_search(result_dict, lorder_cards, farmer_cards, current_move, next_player)
    print("Move: %s; Score: %d; calculated %s nodes "
          % (format_output_cards(current_move), score, nodes_num))
    result_dict[index] = {'move': current_move, 'score': score}


def minmax_search(result_dict, lorder_cards, farmer_cards, current_move, next_player):
    global m_class
    global nodes_num

    def _get_best_move():
        best = False
        for _, item in result_dict.items():
            if item['score'] == MAX_SCORE:
                best = True
                break
        return best

    if next_player == 'farmer':
        if len(lorder_cards) == 0:
            # If any other process gets the best move, exit myself
            if nodes_num % 1e4 == 0 and _get_best_move():
                exit(0)
            nodes_num += 1
            return MAX_SCORE  # lorder win, return MAX_SCORE

    elif next_player == 'lorder':
        if len(farmer_cards) == 0:
            # If any other process gets the best move, exit myself
            if nodes_num % 1e4 == 0 and _get_best_move():
                exit(0)
            nodes_num += 1
            return MIN_SCORE  # farmer win, return MIN_SCORE

    if next_player == 'farmer':  # the parameter next_player is current player
        score = MAX_SCORE  # For farmer, the default score is MAX_SCORE
        all_moves = get_resp_moves(farmer_cards, current_move)
        # a kind of optimization
        all_moves = sorted(all_moves, key=lambda x: len(x), reverse=True)
        for farmer_move in all_moves:
            fc = get_rest_cards(farmer_cards, farmer_move)
            score = minmax_search(result_dict,
                                  lorder_cards,
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
            score = minmax_search(result_dict,
                                  lc,
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
    """
    :return: the best move which can win, otherwise None
    """
    manager = multiprocessing.Manager()
    result_dict = manager.dict()

    process_pool = []
    lorder_cards = format_input_cards(lorder_cards)
    farmer_cards = format_input_cards(farmer_cards)
    farmer_move = format_input_cards(farmer_move)

    all_lorder_moves = get_resp_moves(format_input_cards(lorder_cards), farmer_move)
    # a kind of optimization
    all_lorder_moves = sorted(all_lorder_moves, key=lambda x: len(x), reverse=True)
    formatted_all_lorder_moves = [format_output_cards(move) for move in all_lorder_moves]
    print("%d Moves totally: %s" % (len(formatted_all_lorder_moves), formatted_all_lorder_moves))

    if len(all_lorder_moves) == 1:  # Pass
        return all_lorder_moves[0]

    count = 0
    for move in all_lorder_moves:
        record = {'move': move,
                  'farmer_win': 0,
                  'lorder_win': 0}
        mc_records.append(record)

        lc = get_rest_cards(lorder_cards, move)
        p = multiprocessing.Process(target=process_search,
                                    args=(count, result_dict,
                                          lc, farmer_cards, move, 'farmer'))
        process_pool.append(p)
        count += 1

    for p in process_pool:
        p.start()
    for p in process_pool:
        p.join()

    for _, item in result_dict.items():
        if item['score'] == MAX_SCORE:
            return item['move']
