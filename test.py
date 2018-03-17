import move_classifier
from utils import format_input_cards, GenAnyN, print_func_name
from move_gener import MovesGener
from move_player import get_resp_moves
from move_filter import MoveFilter
from minmax_engine import start_engine

a = [3, 3, 3, 4, 4, 4, 6, 7, 8, 9, 10, 10, 'K']
b = [6, 7, 8, 9, 10, 'J', 'J', 'Q', 'Q', 'Q', 'Y']
c = [3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 12, 13, 13, 13, 14, 14, 14, 'Y', 'Z']


@print_func_name
def test_MoveGener():
    print(format_input_cards(c))
    mg = MovesGener(format_input_cards(c))
    moves = mg.gen_moves()
    # print(moves)
    print(len(moves))


@print_func_name
def test_gen_type_8_serial_single():
    mg = MovesGener(format_input_cards(c))
    print(mg.gen_type_8_serial_single(repeat_num=7))


@print_func_name
def test_gen_type_9_serial_pair():
    mg = MovesGener(format_input_cards(c))
    print(mg.gen_type_9_serial_pair(repeat_num=5))


@print_func_name
def test_gen_type_10_serial_triple():
    mg = MovesGener(format_input_cards(c))
    print(mg.gen_type_10_serial_triple(repeat_num=2))


@print_func_name
def test_gen_type_11_serial_3_1():
    mg = MovesGener(format_input_cards(c))
    print(mg.gen_type_11_serial_3_1())


@print_func_name
def test_gen_type_12_serial_3_2():
    mg = MovesGener(format_input_cards(c))
    print(mg.gen_type_12_serial_3_2())


@print_func_name
def test_GenAnyN():
    gan = GenAnyN([1, 2, 3, 4, 5], 3)  # from this list, get any 3 numbers
    result = gan.gen_n_cards_lists()
    for cards in result:
        print(cards)
    print(len(result))


@print_func_name
def test_MoveClassifier():
    moves = [
        [],
        [20],
        [3, 3],
        [20, 30],
        [4, 4, 4],
        [5, 5, 5, 2],
        [3, 3, 3, 5],
        [6, 3, 4, 5],
        [6, 6, 6, 6],
        [7, 7, 7, 8, 8],
        [9, 9, 10, 10, 10],
        [3, 4, 5, 6, 7],
        [3, 4, 5, 6, 8],
        [2, 2, 4, 5, 6],
        [3, 4, 5, 6, 7, 8, 9],
        [3, 3, 3, 3, 5, 6],
        [3, 3, 3, 3, 5, 6, 7],
        [4, 4, 4, 4, 5, 5, 7, 7],
        [4, 4, 4, 4, 5, 5, 7, 6],
        [4, 4, 4, 4, 5, 5, 6, 6, 7, 7],
        [5, 5, 5, 6, 6, 6, 7, 8],
        [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 10],
        [5, 5, 5, 6, 6, 6, 7, 7, 9, 9],
        [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 10, 10, 13, 13],
        [5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 10, 10, 13, 13, 14],
    ]

    mc = move_classifier.MoveClassifier()
    count = 0
    for move in moves:
        count += 1
        move_type = mc.get_move_type(move).get('type')
        print("%d: The type of %s is %s" %
              (count,
               move,
               move_classifier.MOVE_TYPES_STR.get(move_type, "Wrong")))


@print_func_name
def test_get_resp_moves():
    rival_move = [3, 3, 4, 4, 5, 5]
    cards = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 20, 30]
    print("moves = %s" % get_resp_moves(cards, rival_move))

    rival_move = [5, 5, 5, 6, 6, 6, 7, 8]
    cards = [7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 11, 12, 20, 30]
    print("moves = %s" % get_resp_moves(cards, rival_move))


@print_func_name
def test_filter_type_6_3_1():
    moves = [
        [3, 3, 3, 20],
        [4, 4, 4, 8],
        [5, 5, 5, 9],
        [6, 6, 6, 10]
    ]
    rival_move = [4, 4, 4, 3]

    mf = MoveFilter()
    filtered_moves = mf.filter_type_6_3_1(moves, rival_move)
    print("Filtered moves = %s" % filtered_moves)


@print_func_name
def test_filter_type_7_3_2():
    moves = [
        [3, 3, 3, 7, 7],
        [4, 4, 4, 8, 8],
        [5, 5, 5, 9, 9],
        [6, 6, 6, 10, 10]
    ]
    rival_move = [4, 4, 4, 3, 3]

    mf = MoveFilter()
    filtered_moves = mf.filter_type_7_3_2(moves, rival_move)
    print("Filtered moves = %s" % filtered_moves)


@print_func_name
def test_filter_type_8_serial_single():
    moves = [
        [3, 4, 5, 6, 7, 8],
        [4, 5, 6, 7, 8, 9],
        [5, 6, 7, 8, 9, 10]
    ]
    rival_move = [4, 5, 6, 7, 8, 9]

    mf = MoveFilter()
    filtered_moves = mf.filter_type_8_serial_single(moves, rival_move)
    print("Filtered moves = %s" % filtered_moves)


@print_func_name
def test_filter_type_9_serial_pair():
    moves = [
        [3, 3, 4, 4, 5, 5],
        [4, 4, 5, 5, 6, 6],
        [7, 7, 8, 8, 9, 9]
    ]
    rival_move = [3, 3, 4, 4, 5, 5]

    mf = MoveFilter()
    filtered_moves = mf.filter_type_9_serial_pair(moves, rival_move)
    print("Filtered moves = %s" % filtered_moves)


@print_func_name
def test_filter_type_10_serial_triple():
    moves = [
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [5, 5, 5, 6, 6, 6, 7, 7, 7],
        [7, 7, 7, 8, 8, 8, 9, 9, 9]
    ]
    rival_move = [6, 6, 6, 7, 7, 7, 8, 8, 8]

    mf = MoveFilter()
    filtered_moves = mf.filter_type_10_serial_triple(moves, rival_move)
    print("Filtered moves = %s" % filtered_moves)


@print_func_name
def test_filter_type_11_serial_3_1():
    moves = [
        [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8],
        [5, 5, 8, 9, 5, 6, 6, 6, 7, 7, 7, 10],
        [7, 7, 7, 3, 4, 5, 8, 8, 8, 9, 9, 9]
    ]
    rival_move = [6, 6, 6, 7, 7, 5, 7, 8, 8, 8, 3, 4]

    mf = MoveFilter()
    filtered_moves = mf.filter_type_11_serial_3_1(moves, rival_move)
    print("Filtered moves = %s" % filtered_moves)


@print_func_name
def test_filter_type_12_serial_3_2():
    moves = [
        [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 7, 8],
        [5, 5, 8, 8, 9, 9, 5, 6, 6, 6, 7, 7, 7, 10, 10],
        [7, 7, 7, 3, 3, 4, 5, 4, 5, 8, 8, 8, 9, 9, 9]
    ]
    rival_move = [6, 6, 6, 7, 7, 5, 7, 8, 8, 8, 3, 3, 4, 5, 4]

    mf = MoveFilter()
    filtered_moves = mf.filter_type_12_serial_3_2(moves, rival_move)
    print("Filtered moves = %s" % filtered_moves)


@print_func_name
def test_filter_type_13_4_2():
    moves = [
        [3, 3, 3, 3, 4, 5],
        [5, 5, 5, 5, 8, 9],
        [7, 7, 7, 7, 3, 4]
    ]
    rival_move = [6, 6, 6, 6, 11, 12]

    mf = MoveFilter()
    filtered_moves = mf.filter_type_13_4_2(moves, rival_move)
    print("Filtered moves = %s" % filtered_moves)


@print_func_name
def test_filter_type_14_4_4():
    moves = [
        [3, 3, 3, 3, 4, 4, 5, 5],
        [5, 5, 5, 5, 8, 8, 9, 9],
        [7, 7, 7, 7, 3, 3, 4, 4]
    ]
    rival_move = [6, 6, 6, 6, 11, 11, 12, 12]

    mf = MoveFilter()
    filtered_moves = mf.filter_type_14_4_4(moves, rival_move)
    print("Filtered moves = %s" % filtered_moves)


@print_func_name
def test_minmax_engine():
    lorder_cards = "3 3 4 4 5 5 6 8"
    farmer_cards = "4 4 5 5 3 7"
    best_move = start_engine(lorder_cards=lorder_cards.split(), farmer_cards=farmer_cards.split(), farmer_move=[])
    print("Best Move is %s" % best_move)


def main():
    # Test MoveGener
    test_MoveGener()
    test_gen_type_8_serial_single()
    test_gen_type_9_serial_pair()
    test_gen_type_10_serial_triple()
    test_gen_type_11_serial_3_1()
    test_gen_type_12_serial_3_2()

    # Test MoveFilter
    test_filter_type_6_3_1()
    test_filter_type_7_3_2()
    test_filter_type_8_serial_single()
    test_filter_type_9_serial_pair()
    test_filter_type_10_serial_triple()
    test_filter_type_11_serial_3_1()
    test_filter_type_12_serial_3_2()
    test_filter_type_13_4_2()
    test_filter_type_14_4_4()

    # Test MoveClassifier
    test_MoveClassifier()

    # Test common
    test_GenAnyN()
    test_get_resp_moves()

    # Test MinMax Engine
    test_minmax_engine()


if __name__ == '__main__':
    # freeze_support()
    main()
