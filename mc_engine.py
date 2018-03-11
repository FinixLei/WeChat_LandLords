from utils import format_input_cards, format_output_cards, \
    get_rest_cards, show_situation, calc_time
from move_gener import MovesGener
from move_player import get_resp_moves
from move_classifier import MoveClassifier

nodes_num = 0
m_class = MoveClassifier()


def show_initial_state(lorder_cards=list(), farmer_cards=list(), player='lorder'):
    print("Initial State: ")
    print("lorder cards: %s" % format_output_cards(lorder_cards))
    print("farmer cards: %s" % format_output_cards(farmer_cards))
    print("Current player: %s" % player)
    print("-" * 20)


def mc_search(lorder_cards=list(), farmer_cards=list(),
              current_move=list(), next_player='',
              record=dict()):
    # show_situation(lorder_cards=lorder_cards, farmer_cards=farmer_cards,
    #                move=current_move, next_player=next_player)

    global nodes_num
    global m_class

    if next_player == 'farmer':
        if len(lorder_cards) == 0:
            record['lorder_win'] += 1
            nodes_num += 1
            if nodes_num % 10000 == 0:
                print("Calculated %s nodes" % nodes_num)
            return

    elif next_player == 'lorder':
        if len(farmer_cards) == 0:
            record['farmer_win'] += 1
            nodes_num += 1
            if nodes_num % 10000 == 0:
                print("Calculated %s nodes" % nodes_num)
            return

    if next_player == 'farmer':
        all_moves = get_resp_moves(farmer_cards, current_move)
        for farmer_move in all_moves:
            fc = get_rest_cards(farmer_cards, farmer_move)
            mc_search(lorder_cards=lorder_cards,
                      farmer_cards=fc,
                      current_move=farmer_move,
                      next_player='lorder',
                      record=record)

    else:  # next_player is 'lorder'
        all_moves = get_resp_moves(lorder_cards, current_move)
        for lorder_move in all_moves:
            lc = get_rest_cards(lorder_cards, lorder_move)
            mc_search(lorder_cards=lc,
                      farmer_cards=farmer_cards,
                      current_move=lorder_move,
                      next_player='farmer',
                      record=record)


@calc_time
def start_mc(lorder_cards=list(), farmer_cards=list()):
    lorder_cards = format_input_cards(lorder_cards)
    farmer_cards = format_input_cards(farmer_cards)

    mg = MovesGener(format_input_cards(lorder_cards))
    all_lorder_moves = mg.gen_moves()

    mc_records = list()
    for i in range(len(all_lorder_moves)):
        mc_records.append({'farmer_win': 0, 'lorder_win': 0})

    count = 0
    for move in all_lorder_moves:
        lc = get_rest_cards(lorder_cards, move)
        mc_search(lorder_cards=lc,
                  farmer_cards=farmer_cards,
                  current_move=move,
                  next_player='farmer',
                  record=mc_records[count])
        count += 1

    return all_lorder_moves, mc_records


def main():
    global nodes_num

    # lorder_cards = ['A', 'A', 'K', 'J', 9, 9, 8, 6, 4]
    # farmer_cards = ['2', 'A', 'J', 10, 10, 7, 7, 6, 5, 5, 4, 3, 3]

    lorder_cards = [3, 4, 5, 6, 7]
    farmer_cards = [4, 5, 6, 7, 8]
    all_moves, records = start_mc(lorder_cards=lorder_cards, farmer_cards=farmer_cards)

    for i in range(len(all_moves)):
        f_win_num = records[i]['farmer_win']
        l_win_num = records[i]['lorder_win']
        print("%d. %s:\n   lorder_win: %.2f%s:\t lorder=%d, farmer=%d, "
              % (i+1, all_moves[i],
                 100 * float(l_win_num) / (l_win_num + f_win_num), '%',
                 l_win_num, f_win_num))

    print("Calculated %s node" % nodes_num)


main()
