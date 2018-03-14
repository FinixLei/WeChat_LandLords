from minmax_engine import start_engine


def main():
    # lorder_cards = [2, 2, 'A', 'K', 10, 7, 6, 6, 5, 5, 4, 3]
    # farmer_cards = ['Z', 2, 'A', 'K', 'Q', 'J', 10, 5, 5, 4, 3]
    # start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[])

    lorder_cards = ['Y', 2, 'J', 'J', 10, 8, 5, 5, 3]
    farmer_cards = ['A', 'A', 'K', 10, 10, 7, 6]
    best_move = start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[8, 8])
    print("Best Move is %s" % best_move)


if __name__ == '__main__':
    # freeze_support()
    main()
