# coding=utf-8


from ui_engine import UIEngine


def main():
    lorder_cards = "小王 大王 K 10 10 7 8 8 6 6"
    farmer_cards = "2 2 A A A 9 9 7 6 6 3 3"

    # lorder_cards = "3 4 5 大王"
    # farmer_cards = "3 4 5 小王"

    UIEngine.run(lorder_cards.split(), farmer_cards.split(), farmer_move=[])


if __name__ == '__main__':
    # freeze_support()
    main()
