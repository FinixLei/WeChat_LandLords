from utils import format_input_cards, format_output_cards, \
    get_rest_cards, show_situation
from move_gener import MovesGener
from move_player import get_resp_moves

farmer_win = 0
lorder_win = 0


def show_initial_state(lorder_cards=list(), farmer_cards=list(), player='lorder'):
    print("Initial State: ")
    print("lorder cards: %s" % format_output_cards(lorder_cards))
    print("farmer cards: %s" % format_output_cards(farmer_cards))
    print("Current player: %s" % player)
    print("-" * 20)


def mc_search(lorder_cards=list(), farmer_cards=list(), current_move=list(), next_player=''):
    global lorder_win
    global farmer_win

    show_situation(lorder_cards=lorder_cards, farmer_cards=farmer_cards,
                   move=current_move, next_player=next_player)

    if next_player == 'farmer' and len(lorder_cards) == 0:
        # TODO: record lorder win
        lorder_win += 1
        print("Lorder Win!")
        return
    elif next_player == 'lorder' and len(farmer_cards) == 0:
        # TODO: record farmer win
        farmer_win += 1
        print("Farmer Win!")
        return

    if next_player == 'farmer':
        all_moves = get_resp_moves(farmer_cards, current_move)
        for farmer_move in all_moves:
            fc = get_rest_cards(farmer_cards, farmer_move)
            mc_search(lorder_cards=lorder_cards,
                      farmer_cards=fc,
                      current_move=farmer_move,
                      next_player='lorder')

    else:  # next_player is 'lorder'
        all_moves = get_resp_moves(lorder_cards, current_move)
        for lorder_move in all_moves:
            lc = get_rest_cards(lorder_cards, lorder_move)
            mc_search(lorder_cards=lc,
                      farmer_cards=farmer_cards,
                      current_move=lorder_move,
                      next_player='farmer')


def start_mc(lorder_cards=list(), farmer_cards=list()):
    lorder_cards = format_input_cards(lorder_cards)
    farmer_cards = format_input_cards(farmer_cards)

    mg = MovesGener(format_input_cards(lorder_cards))
    all_lorder_moves = mg.gen_moves()

    for move in all_lorder_moves:
        if move:
            lc = get_rest_cards(lorder_cards, move)
            mc_search(lorder_cards=lc,
                      farmer_cards=farmer_cards,
                      current_move=move,
                      next_player='farmer')


def main():
    # start_mc(lorder_cards=[3, 7, 7, 10], farmer_cards=[3, 'J', 5, 5])
    start_mc(lorder_cards=[3, 4, 5], farmer_cards=[4, 5, 6])
    print("Farmer Win Number: %d" % farmer_win)
    print("Lorder Win Number: %d" % lorder_win)


main()
