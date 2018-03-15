# coding=utf-8

from six.moves import input
from utils import format_input_cards, format_output_cards, get_rest_cards
from move_player import get_resp_moves
from minmax_engine import start_engine


class UIEngine(object):
    @staticmethod
    def declare():
        print("可输入的命令及大小王牌型如下:")
        print("pass - 过，不出牌")
        print("Y - 小王")
        print("Z - 大王")
        print("-" * 30)

    @staticmethod
    def run(lorder_cards=[], farmer_cards=[], farmer_move=[]):
        UIEngine.declare()

        if not lorder_cards and not farmer_cards:
            print("请输入地主的牌: ")
            lorder_cards = input().split()
            print("请输入农民的牌: ")
            farmer_cards = input().split()

        lorder_cards = format_input_cards(lorder_cards)
        farmer_cards = format_input_cards(farmer_cards)

        print("初始状态: ")
        print("地主家的牌: %s" % format_output_cards(lorder_cards))
        print("农民家的牌: %s" % format_output_cards(farmer_cards))
        print("当前出牌者: %s" % "地主")
        print("-" * 20)

        # LandLorder do the first move
        lorder_move = start_engine(lorder_cards=lorder_cards,
                                   farmer_cards=farmer_cards,
                                   farmer_move=farmer_move)

        if lorder_move is None:
            print("地主必败！")
            return

        lorder_cards = get_rest_cards(lorder_cards, lorder_move)
        if len(lorder_cards) == 0:
            print("地主出牌: %s" % format_output_cards(lorder_move))
            print("地主胜利!")
            return

        # Farmer and LandLorder play one by one
        while True:
            # Print the Situation after Lorder play a move
            str_lorder_move = format_output_cards(lorder_move) if lorder_move else 'Pass!'
            print("地主家的牌: %s" % format_output_cards(lorder_cards))
            print("地主已出牌: %s" % str_lorder_move)
            print("农民家的牌: %s" % format_output_cards(farmer_cards))
            print("-" * 20)

            # Farmer plays a move
            print("请帮农民出牌:")
            farmer_move = input("")
            if (farmer_move in ['pass', 'Pass', 'PASS', '不要']) or \
               len(farmer_move.strip()) == 0:
                farmer_move = []
            else:
                farmer_move = format_input_cards(farmer_move.split())

            possible_moves = get_resp_moves(farmer_cards, lorder_move)
            # must sort, for 'not in' check.
            possible_moves = [sorted(move) for move in possible_moves]
            while farmer_move not in possible_moves:
                print("错误的出牌！请重新帮农民出牌: ")
                farmer_move = input("")
                if farmer_move in ['pass', 'Pass', 'PASS']:
                    farmer_move = []
                else:
                    farmer_move = format_input_cards(farmer_move.split())
                possible_moves = get_resp_moves(farmer_cards, lorder_move)
                # must sort, for 'not in' check.
                possible_moves = [sorted(move) for move in possible_moves]

            farmer_cards = get_rest_cards(farmer_cards, farmer_move)
            if len(farmer_cards) == 0:
                print("农民出牌: %s" % format_output_cards(farmer_move))
                print("农民胜利！")
                return

            str_farmer_move = format_output_cards(farmer_move) if farmer_move else 'Pass!'
            print("地主家的牌: %s" % format_output_cards(lorder_cards))
            print("农民家的牌: %s" % format_output_cards(farmer_cards))
            print("农民已出牌: %s" % str_farmer_move)
            print("-" * 20)

            # LandLorder plays a move
            lorder_move = start_engine(lorder_cards=lorder_cards, farmer_cards=farmer_cards,
                                       farmer_move=farmer_move)

            if lorder_move is None:
                print("地主必败！")
                return

            lorder_cards = get_rest_cards(lorder_cards, lorder_move)
            if len(lorder_cards) == 0:
                print("地主出牌: %s" % format_output_cards(lorder_move))
                print("地主胜利！")
                return
