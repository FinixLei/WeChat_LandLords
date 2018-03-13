from minmax_engine import start_engine


def main():
    lorder_cards = [2, 2, 'A', 'K', 10, 7, 6, 6, 5, 5, 4, 3]
    farmer_cards = ['Z', 2, 'A', 'K', 'Q', 'J', 10, 5, 5, 4, 3]
    start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[])


if __name__ == '__main__':
    # freeze_support()
    main()
