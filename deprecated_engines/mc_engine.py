from utils import format_input_cards, format_output_cards, \
    get_rest_cards, show_situation, calc_time
from move_gener import MovesGener
from move_player import get_resp_moves
from move_classifier import MoveClassifier

nodes_num = 0
m_class = MoveClassifier()
mc_records = list()


def dump_mc_records():
    global mc_records
    for record in mc_records:
        move = record.get('move', '')
        farmer_win = record.get('farmer_win', 0)
        lorder_win = record.get('lorder_win', 0)
        lorder_win_rate = float(lorder_win) / (lorder_win+farmer_win) if lorder_win else 0
        print('move: %s\n  lorder win rate: %.2f%s, lorder: %s, farmer: %s'
              % (move, 100*lorder_win_rate, '%', lorder_win, farmer_win))


def show_node_info():
    if nodes_num % 1e4 == 0:
        print("Calculated %s nodes" % nodes_num)
    if nodes_num % 1e5 == 0:
        dump_mc_records()


def show_initial_state(lorder_cards=list(), farmer_cards=list(), player='lorder'):
    print("Initial State: ")
    print("lorder cards: %s" % format_output_cards(lorder_cards))
    print("farmer cards: %s" % format_output_cards(farmer_cards))
    print("Current player: %s" % player)
    print("-" * 20)


def mc_search(lorder_cards=list(), farmer_cards=list(),
              current_move=list(), next_player='',
              record=dict(), debug=False):
    if debug:
        show_situation(lorder_cards=lorder_cards, farmer_cards=farmer_cards,
                       move=current_move, next_player=next_player)

    global nodes_num
    global m_class

    if next_player == 'farmer':
        if len(lorder_cards) == 0:
            record['lorder_win'] += 1
            nodes_num += 1
            show_node_info()
            return

    elif next_player == 'lorder':
        if len(farmer_cards) == 0:
            record['farmer_win'] += 1
            nodes_num += 1
            show_node_info()
            return

    if next_player == 'farmer':
        all_moves = get_resp_moves(farmer_cards, current_move)
        # a kind of optimization
        all_moves = sorted(all_moves, key=lambda x: len(x), reverse=True)
        for farmer_move in all_moves:
            fc = get_rest_cards(farmer_cards, farmer_move)
            mc_search(lorder_cards=lorder_cards,
                      farmer_cards=fc,
                      current_move=farmer_move,
                      next_player='lorder',
                      record=record,
                      debug=debug)

    else:  # next_player is 'lorder'
        all_moves = get_resp_moves(lorder_cards, current_move)
        # a kind of optimization
        all_moves = sorted(all_moves, key=lambda x: len(x), reverse=True)
        for lorder_move in all_moves:
            lc = get_rest_cards(lorder_cards, lorder_move)
            mc_search(lorder_cards=lc,
                      farmer_cards=farmer_cards,
                      current_move=lorder_move,
                      next_player='farmer',
                      record=record,
                      debug=debug)


@calc_time
def start_mc(lorder_cards=list(), farmer_cards=list(), farmer_move=list()):
    global mc_records

    lorder_cards = format_input_cards(lorder_cards)
    farmer_cards = format_input_cards(farmer_cards)
    farmer_move = format_input_cards(farmer_move)

    all_lorder_moves = get_resp_moves(format_input_cards(lorder_cards), farmer_move)
    # a kind of optimization
    all_lorder_moves = sorted(all_lorder_moves, key=lambda x: len(x), reverse=True)

    for i in range(len(all_lorder_moves)):
        mc_records.append({'move': all_lorder_moves[i],
                           'farmer_win': 0,
                           'lorder_win': 0})

    count = 0
    for move in all_lorder_moves:
        lc = get_rest_cards(lorder_cards, move)
        debug = False
        mc_search(lorder_cards=lc,
                  farmer_cards=farmer_cards,
                  current_move=move,
                  next_player='farmer',
                  record=mc_records[count],
                  debug=debug)
        count += 1

    return all_lorder_moves, mc_records, nodes_num
