from ui_engine import UIEngine


def main():
    lorder_cards = ""
    farmer_cards = ""

    # lorder_cards = "2 2 A K 10 7 6 6 5 5 4 3"
    # farmer_cards = "Z 2 A K Q J 10 5 5 4 3"

    UIEngine.run(lorder_cards.split(), farmer_cards.split())


if __name__ == '__main__':
    # freeze_support()
    main()
