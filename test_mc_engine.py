from mc_engine import start_mc


def main():
    # lorder_cards = ['A', 'A', 'K', 'J', 9, 9, 8, 6, 4]
    # farmer_cards = ['2', 'A', 'J', 10, 10, 7, 7, 6, 5, 5, 4, 3, 3]

    lorder_cards = [3, 4, 5, 6, 7,8 ]
    farmer_cards = [4, 5, 6, 7, 8]
    all_moves, records, nodes_num = start_mc(lorder_cards=lorder_cards, farmer_cards=farmer_cards)

    for i in range(len(all_moves)):
        f_win_num = records[i]['farmer_win']
        l_win_num = records[i]['lorder_win']
        print("%d. %s:\n   lorder_win: %.2f%s:\t lorder=%d, farmer=%d, "
              % (i+1, all_moves[i],
                 100 * float(l_win_num)/(l_win_num+f_win_num), '%',
                 l_win_num, f_win_num))

    print("There are %s nodes totally." % nodes_num)


main()
