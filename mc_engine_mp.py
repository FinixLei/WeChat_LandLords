import multiprocessing
import os
import re

from utils import format_input_cards, format_output_cards, \
    get_rest_cards, show_situation, calc_time
from move_gener import MovesGener
from move_player import get_resp_moves
from move_classifier import MoveClassifier

nodes_num = 0
mc_records = list()
m_class = MoveClassifier()


def clear_env():
    for file in os.listdir("."):
        if file.startswith("output_"):
            os.remove("./" + file)


def dump_mc_records(index, record):
    move = record.get('move', '')
    farmer_win = record.get('farmer_win', 0)
    lorder_win = record.get('lorder_win', 0)
    lorder_win_rate = float(lorder_win) / (lorder_win+farmer_win) if lorder_win else 0
    out_line = 'move=%s; lorder_win_rate=%.2f%s; lorder=%s; farmer=%s' \
               % (move, 100 * lorder_win_rate, '%', lorder_win, farmer_win)

    output_file = "./output_%s" % index
    with open(output_file, 'w') as OUT_FILE:
        OUT_FILE.write(out_line)

    results = list()
    for file in os.listdir('.'):
        if file.startswith('output_'):
            with open(file, 'r') as in_file:
                for line in in_file.readlines():
                    results.append(line)
                    break

    regex = re.compile(r'.+lorder_win_rate=(.+)%.+')
    result_dict = dict()
    for result in results:
        items = regex.search(result)
        if items:
            rate = items.group(1)
            result_dict[result] = float(rate)

    sorted_results = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
    for result in sorted_results:
        print(result[0])

    print("-" * 50)


def process_mc_search(index, record, lorder_cards, farmer_cards,
                      current_move, next_player):
    mc_search(index, record, lorder_cards, farmer_cards,
              current_move, next_player)
    print("------------- Start: Move No.%d --------------" % index)
    dump_mc_records(index, record)
    print("------------- End --------------")


def mc_search(index, record, lorder_cards, farmer_cards,
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
            if nodes_num % 1e5 == 0:
                dump_mc_records(index, record)
            return

    elif next_player == 'lorder':
        if len(farmer_cards) == 0:
            record['farmer_win'] += 1
            nodes_num += 1
            if nodes_num % 1e5 == 0:
                dump_mc_records(index, record)
            return

    if next_player == 'farmer':
        all_moves = get_resp_moves(farmer_cards, current_move)
        # a kind of optimization
        all_moves = sorted(all_moves, key=lambda x: len(x), reverse=True)
        for farmer_move in all_moves:
            fc = get_rest_cards(farmer_cards, farmer_move)
            mc_search(index, record,
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
            mc_search(index, record,
                      lc,
                      farmer_cards,
                      lorder_move,
                      'farmer')


@calc_time
def start_mc(lorder_cards=list(), farmer_cards=list(), farmer_move=list()):
    clear_env()

    process_pool = []
    lorder_cards = format_input_cards(lorder_cards)
    farmer_cards = format_input_cards(farmer_cards)
    farmer_move = format_input_cards(farmer_move)

    all_lorder_moves = get_resp_moves(format_input_cards(lorder_cards), farmer_move)
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
                                    args=(count, record, lc, farmer_cards, move, 'farmer'))
        process_pool.append(p)
        count += 1

    for p in process_pool:
        p.start()
    for p in process_pool:
        p.join()
