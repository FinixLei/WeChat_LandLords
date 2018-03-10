# coding=utf-8

from common import format_input_cards, format_output_cards, get_rest_cards
from move_player import get_resp_moves, do_a_move


class UIEngine(object):

    def declare_commands(self):
        print("可输入的命令及大小王牌型如下:")
        print("pass - 过，不出牌")
        print("Y - 小王")
        print("Z - 大王")
        print("-" * 30)

    @staticmethod
    def run(lorder_cards=[], farmer_cards=[]):
        lorder_cards = format_input_cards(lorder_cards)
        farmer_cards = format_input_cards(farmer_cards)
        player = 'farmer'

        print("初始状态: ")
        print("地主家的牌: %s" % format_output_cards(lorder_cards))
        print("农民家的牌: %s" % format_output_cards(farmer_cards))
        print("当前出牌者: %s" % "农民")
        print("-" * 20)

        # Farmer do the first move
        farmer_move = do_a_move(lorder_cards=lorder_cards,
                                farmer_cards=farmer_cards,
                                previous_move=[],
                                player=player)

        farmer_cards = get_rest_cards(farmer_cards, farmer_move)
        if len(farmer_cards) == 0:
            print("农民出牌: %s" % format_output_cards(farmer_move))
            print("农民胜利!")
            return

        # Lorder plays a move, and farmer plays a move, and so on.
        while True:
            # Print the Situation after Farmer play a move
            str_farmer_cards = format_output_cards(farmer_move) if farmer_move else 'Pass!'
            print("农民出牌: %s" % str_farmer_cards)
            print("地主家的牌: %s" % format_output_cards(lorder_cards))
            print("农民家的牌: %s" % format_output_cards(farmer_cards))
            print("-" * 20)

            # Lords play a move
            print("请帮地主出牌:")
            lorder_move = raw_input("")
            if (lorder_move in ['pass', 'Pass', 'PASS', '不要']) or \
               len(lorder_move.strip()) == 0:
                lorder_move = []
            else:
                lorder_move = format_input_cards(lorder_move.split())

            if not farmer_move:
                possible_moves = get_resp_moves(lorder_cards, farmer_move, can_be_pass=False)
            else:
                possible_moves = get_resp_moves(lorder_cards, farmer_move)
            while lorder_move not in possible_moves:
                print("错误的出牌！请重新帮地主出牌: ")
                lorder_move = raw_input("")
                if lorder_move in ['pass', 'Pass', 'PASS']:
                    lorder_move = []
                else:
                    lorder_move = format_input_cards(lorder_move.split())
                possible_moves = get_resp_moves(lorder_cards, farmer_move)

            lorder_cards = get_rest_cards(lorder_cards, lorder_move)
            if len(lorder_cards) == 0:
                print("地主出牌: %s" % format_output_cards(lorder_move))
                print("地主胜利！")
                return

            str_lorder_move = format_output_cards(lorder_move) if lorder_move else 'Pass!'
            print("地主出牌: %s" % str_lorder_move)
            print("地主家的牌: %s" % format_output_cards(lorder_cards))
            print("农民家的牌: %s" % format_output_cards(farmer_cards))
            print("-" * 20)

            # Farmer play a move
            can_be_pass = True if lorder_move else False
            farmer_move = do_a_move(lorder_cards=lorder_cards,
                                    farmer_cards=farmer_cards,
                                    previous_move=lorder_move,
                                    player="farmer",
                                    can_be_pass=can_be_pass)

            farmer_cards = get_rest_cards(farmer_cards, farmer_move)
            if len(farmer_cards) == 0:
                print("农民出牌: %s" % format_output_cards(farmer_move))
                print("农工胜利！")
                return
