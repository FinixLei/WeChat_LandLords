from minmax_engine import start_engine


def main():
    # lorder_cards = [3, 4, 5, 6, 7, 8]
    # farmer_cards = [4, 5, 6, 7, 8]
    # start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards)

    lorder_cards = ['A', 'A', 'K', 'J', 9, 9, 8, 6, 4]
    farmer_cards = ['2', 'A', 'J', 10, 10, 7, 7, 6, 5, 5, 4, 3, 3]
    start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[])
    # '6', 'J',

    # lorder_cards = ['A', 'A', 'K', 'J', 9, 9, 8, 4]
    # farmer_cards = ['2', 'A', 10, 10, 7, 7, 6, 5, 5, 4, 3, 3]
    # start_mc(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=['J'])
    # # 'K', 'A', pass, [3, 3]

    # lorder_cards = ['A', 'A', 'J', 9, 9, 8, 4]
    # farmer_cards = ['2', 10, 10, 7, 7, 6, 5, 5, 4]
    # start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[3, 3])
    # # [9, 9], [10, 10]

    # lorder_cards = ['A', 'A', 'J', 8, 4]
    # farmer_cards = ['2', 7, 7, 6, 5, 5, 4]
    # start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[10, 10])

    # lorder_cards = ['J', 8, 4]
    # farmer_cards = ['2', 7, 7, 6, 5, 5, 4]
    # start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[])
    # # Right Answer is 8 or 'J'. Figured it out!

    # lorder_cards = ['J', 4]
    # farmer_cards = [6]
    # start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[4])

    # lorder_cards = ['J', 8, 4]
    # farmer_cards = ['2', 6, 4]
    # start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards, farmer_move=[])


if __name__ == '__main__':
    # freeze_support()
    main()
