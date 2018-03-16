# coding=utf-8


from ui_engine import UIEngine


def main():
    lorder_cards = ""
    farmer_cards = ""

    # lorder_cards = "3 4 5 大王"
    # farmer_cards = "3 4 5 小王"

    UIEngine.run(lorder_cards.split(), farmer_cards.split(), farmer_move=[])


if __name__ == '__main__':
    # freeze_support()
    main()
