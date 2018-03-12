from mc_engine import start_mc


def main():
    lorder_cards = ['J', 8, 4]
    farmer_cards = ['2', 6, 4]
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
