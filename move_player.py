import copy
import random
import move_classifier
import move_gener


def get_possible_moves(cards, rival_move):
    """
    :param cards, a list, current cards
    :param rival_move, a list, rival's move
    :return moves, a list of proper move list
    """
    mc = move_classifier.MoveClassifier()
    mg = move_gener.MovesGener(cards)

    result = mc.get_move_type(rival_move)
    move_type = result.get('type')
    move_serial_num = result.get('serial_num', 1)
    moves = list()

    if move_type == move_classifier.TYPE_0_PASS:
        # generate a random move
        moves = mg.gen_moves()

    elif move_type == move_classifier.TYPE_1_SINGLE:
        moves = mg.gen_type_1_single()

    elif move_type == move_classifier.TYPE_2_PAIR:
        moves = mg.gen_type_2_pair()

    elif move_type == move_classifier.TYPE_3_TRIPLE:
        moves = mg.gen_type_3_triple()

    elif move_type == move_classifier.TYPE_4_BOMB:
        moves = mg.gen_type_4_bomb() \
                + mg.gen_type_5_king_bomb()

    elif move_type == move_classifier.TYPE_5_KING_BOMB:
        moves = []

    elif move_type == move_classifier.TYPE_6_3_1:
        moves = mg.gen_type_6_3_1()

    elif move_type == move_classifier.TYPE_7_3_2:
        moves = mg.gen_type_7_3_2()

    elif move_type == move_classifier.TYPE_8_SERIAL_SINGLE:
        moves = mg.gen_type_8_serial_single(repeat_num=move_serial_num)

    elif move_type == move_classifier.TYPE_9_SERIAL_PAIR:
        moves = mg.gen_type_9_serial_pair(repeat_num=move_serial_num)

    elif move_type == move_classifier.TYPE_10_SERIAL_TRIPLE:
        moves = mg.gen_type_10_serial_triple(repeat_num=move_serial_num)

    elif move_type == move_classifier.TYPE_11_SERIAL_3_1:
        moves = mg.gen_type_11_serial_3_1(repeat_num=move_serial_num)

    elif move_type == move_classifier.TYPE_12_SERIAL_3_2:
        moves = mg.gen_type_12_serial_3_2(repeat_num=move_serial_num)

    elif move_type == move_classifier.TYPE_13_4_2:
        moves = mg.gen_type_13_4_2()

    else:  # Unknown type
        raise Exception("Unknown Move Type!")

    if move_type not in [move_classifier.TYPE_0_PASS,
                         move_classifier.TYPE_4_BOMB,
                         move_classifier.TYPE_5_KING_BOMB]:
        moves = moves + mg.gen_type_4_bomb() + mg.gen_type_5_king_bomb()

    return moves


def do_a_move(lord_cards=[], farmer_cards=[],
              previous_move=[], player='farmer'):
    lc = copy.deepcopy(lord_cards)
    fc = copy.deepcopy(farmer_cards)
    pm = copy.deepcopy(previous_move)

    print("lord cards: %s" % lord_cards)
    print("farmer cards: %s" % farmer_cards)
    print("current player is %s" % player)
    print("previous move: %s" % previous_move)

    if player == 'farmer':
        all_moves = get_possible_moves(fc, pm)
    else:
        all_moves = get_possible_moves(lc, pm)

    if len(all_moves) == 0:
        move = []
    else:
        move = all_moves[random.randint(0, len(all_moves)-1)]

    print("current move: %s" % move)
    print("-" * 20)
    return move
