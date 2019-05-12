import copy
import move_classifier
import move_gener
import move_filter


def get_resp_moves(cards, rival_move):
    """
    :param cards, a list, current cards
    :param rival_move, a list, rival's move
    :return moves, a list of proper move list
    """
    mc = move_classifier.MoveClassifier()
    mg = move_gener.MovesGener(cards)
    mf = move_filter.MoveFilter()

    result = mc.get_move_type(rival_move)
    move_type = result.get('type')
    move_serial_num = result.get('serial_num', 1)
    moves = list()

    if move_type == move_classifier.TYPE_0_PASS:
        # generate a random move
        moves = mg.gen_moves()

    elif move_type == move_classifier.TYPE_1_SINGLE:
        all_moves = mg.gen_type_1_single()
        moves = mf.filter_type_1_single(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_2_PAIR:
        all_moves = mg.gen_type_2_pair()
        moves = mf.filter_type_2_pair(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_3_TRIPLE:
        all_moves = mg.gen_type_3_triple()
        moves = mf.filter_type_3_triple(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_4_BOMB:
        all_moves = mg.gen_type_4_bomb() \
                    + mg.gen_type_5_king_bomb()
        moves = mf.filter_type_4_bomb(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_5_KING_BOMB:
        moves = []

    elif move_type == move_classifier.TYPE_6_3_1:
        all_moves = mg.gen_type_6_3_1()
        moves = mf.filter_type_6_3_1(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_7_3_2:
        all_moves = mg.gen_type_7_3_2()
        moves = mf.filter_type_7_3_2(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_8_SERIAL_SINGLE:
        all_moves = mg.gen_type_8_serial_single(repeat_num=move_serial_num)
        moves = mf.filter_type_8_serial_single(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_9_SERIAL_PAIR:
        all_moves = mg.gen_type_9_serial_pair(repeat_num=move_serial_num)
        moves = mf.filter_type_9_serial_pair(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_10_SERIAL_TRIPLE:
        all_moves = mg.gen_type_10_serial_triple(repeat_num=move_serial_num)
        moves = mf.filter_type_10_serial_triple(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_11_SERIAL_3_1:
        all_moves = mg.gen_type_11_serial_3_1(repeat_num=move_serial_num)
        moves = mf.filter_type_11_serial_3_1(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_12_SERIAL_3_2:
        all_moves = mg.gen_type_12_serial_3_2(repeat_num=move_serial_num)
        moves = mf.filter_type_12_serial_3_2(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_13_4_2:
        all_moves = mg.gen_type_13_4_2()
        moves = mf.filter_type_13_4_2(all_moves, rival_move)

    elif move_type == move_classifier.TYPE_14_4_4:
        all_moves = mg.gen_type_14_4_4()
        moves = mf.filter_type_14_4_4(all_moves, rival_move)

    else:  # Unknown type
        raise Exception("Unknown Move Type! - %s" % rival_move)

    if move_type not in [move_classifier.TYPE_0_PASS,
                         move_classifier.TYPE_4_BOMB,
                         move_classifier.TYPE_5_KING_BOMB]:
        moves = moves + mg.gen_type_4_bomb() + mg.gen_type_5_king_bomb()

    if rival_move:  # rival_move is not 'pass'
        moves = moves + [[]]

    return moves


# Only for testing UIEngine
def do_a_move(lorder_cards=[], farmer_cards=[],
              previous_move=[], player='farmer'):
    lc = copy.deepcopy(lorder_cards)
    fc = copy.deepcopy(farmer_cards)
    pm = copy.deepcopy(previous_move)

    if player == 'farmer':
        all_moves = get_resp_moves(fc, pm)
    else:
        all_moves = get_resp_moves(lc, pm)

    if len(all_moves) == 0:
        move = []
    else:
        # move = all_moves[random.randint(0, len(all_moves)-1)]
        print("Debug: all moves: %s" % all_moves)
        move = all_moves[0]

    return move
