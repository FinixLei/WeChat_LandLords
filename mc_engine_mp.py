import multiprocessing

from utils import format_input_cards, format_output_cards, \
    get_rest_cards, show_situation, calc_time
from move_gener import MovesGener
from move_player import get_resp_moves
from move_classifier import MoveClassifier

nodes_num = 0
mc_records = list()
m_class = MoveClassifier()


def dump_mc_record(record):
    move = record.get('move', '')
    farmer_win = record.get('farmer_win', 0)
    lorder_win = record.get('lorder_win', 0)
    lorder_win_rate = float(lorder_win) / (lorder_win+farmer_win) if lorder_win else 0
    print('move: %s\n  lorder win rate: %.2f%s, lorder: %s, farmer: %s'
          % (move, 100*lorder_win_rate, '%', lorder_win, farmer_win))


def show_node_info(record):
    global nodes_num
    if nodes_num % 1e4 == 0:
        dump_mc_record(record)


def show_initial_state(lorder_cards=list(), farmer_cards=list(), player='lorder'):
    print("Initial State: ")
    print("lorder cards: %s" % format_output_cards(lorder_cards))
    print("farmer cards: %s" % format_output_cards(farmer_cards))
    print("Current player: %s" % player)
    print("-" * 20)


def process_mc_search(record, lorder_cards, farmer_cards,
                      current_move, next_player):
    mc_search(record, lorder_cards, farmer_cards,
              current_move, next_player)
    print("------------- Start --------------")
    dump_mc_record(record)
    print("------------- End --------------")


def mc_search(record, lorder_cards, farmer_cards,
              current_move, next_player):
    # show_situation(lorder_cards=lorder_cards, farmer_cards=farmer_cards,
    #                move=current_move, next_player=next_player)

    global m_class
    global nodes_num
    global mc_records

    if next_player == 'farmer':
        if len(lorder_cards) == 0:
            record['lorder_win'] += 1
            nodes_num += 1
            show_node_info(record)
            return

    elif next_player == 'lorder':
        if len(farmer_cards) == 0:
            record['farmer_win'] += 1
            nodes_num += 1
            show_node_info(record)
            return

    if next_player == 'farmer':
        all_moves = get_resp_moves(farmer_cards, current_move)
        # a kind of optimization
        all_moves = sorted(all_moves, key=lambda x: len(x), reverse=True)
        for farmer_move in all_moves:
            fc = get_rest_cards(farmer_cards, farmer_move)
            mc_search(record,
                      lorder_cards,
                      fc,
                      farmer_move,
                      'lorder')

    else:  # next_player is 'lorder'
        all_moves = get_resp_moves(lorder_cards, current_move)
        # a kind of optimization
        all_moves = sorted(all_moves, key=lambda x: len(x), reverse=True)
        for lorder_move in all_moves:
            lc = get_rest_cards(lorder_cards, lorder_move)
            mc_search(record,
                      lc,
                      farmer_cards,
                      lorder_move,
                      'farmer')


def start_mc(lorder_cards=list(), farmer_cards=list()):
    process_pool = []

    lorder_cards = format_input_cards(lorder_cards)
    farmer_cards = format_input_cards(farmer_cards)

    mg = MovesGener(format_input_cards(lorder_cards))
    all_lorder_moves = mg.gen_moves()
    # a kind of optimization
    all_lorder_moves = sorted(all_lorder_moves, key=lambda x: len(x), reverse=True)
    print("All Moves: %s" % all_lorder_moves)

    count = 0
    while count < len(all_lorder_moves):
        move = all_lorder_moves[count]
        record = {'move': move,
                  'farmer_win': 0,
                  'lorder_win': 0}
        mc_records.append(record)

        lc = get_rest_cards(lorder_cards, move)
        p = multiprocessing.Process(target=process_mc_search,
                                    args=(record, lc, farmer_cards, move, 'farmer'))
        process_pool.append(p)
        count += 1

    for p in process_pool:
        p.start()
    for p in process_pool:
        p.join()
