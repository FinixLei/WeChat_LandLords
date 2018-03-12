from mc_engine_mp import start_mc


def main():
    # lorder_cards = ['A', 'A', 'K', 'J', 9, 9, 8, 6, 4]
    # farmer_cards = ['2', 'A', 'J', 10, 10, 7, 7, 6, 5, 5, 4, 3, 3]

    lorder_cards = [3, 4, 5, 6, 7, 8]
    farmer_cards = [4, 5, 6, 7, 8]
    start_mc(lorder_cards=lorder_cards, farmer_cards=farmer_cards)


if __name__ == '__main__':
    # freeze_support()
    main()
