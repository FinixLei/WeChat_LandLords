# coding=utf-8

import copy
from common import s2v


class UIEngine(object):

    def declare_commands(self):
        print("可输入的命令及大小王牌型如下:")
        print("quit - 退出程序")
        print("pass - 过，不出牌")
        print("Y - 小王")
        print("Z - 大王")
        print("-" * 30)

    def format_cards(self, cards):
        new_cards = list()
        for i in cards:
            if i in s2v:
                new_cards.append(s2v[i])
            else:
                new_cards.append(i)
        return new_cards

    def valid_cards(self, cards):
        valid_range = s2v.values()
        for card in cards:
            if card not in valid_range:
                return False
        return True

    def check_quit_command(self, str_input):
        if str_input == 'quit':
            exit(0)

    def pass_move(self, str_input):
        return True if str_input.lower() == 'pass' else False

    def valid_move(self, current_move, current_cards):
        if not self.valid_cards(current_cards):
            return False

        rest_cards = copy.deepcopy(current_cards)
        c_move = copy.deepcopy(current_move)
        while len(c_move) > 0:
            if c_move[0] in rest_cards:
                rest_cards.remove(c_move[0])
                c_move.remove(c_move[0])
            else:
                return False
        return True

    def get_rest_cards(self, current_move, current_cards):
        rest_cards = copy.deepcopy(current_cards)
        c_move = copy.deepcopy(current_move)
        while len(c_move) > 0:
            rest_cards.remove(c_move[0])
            c_move.remove(c_move[0])
        return rest_cards

    def run(self):
        self.declare_commands()

        # Initial Cards of LandLord and Farmer

        print("请输入地主的最初牌型：")
        input_cards = raw_input('')
        self.check_quit_command(input_cards)
        lord_cards = self.format_cards(input_cards.split())

        if not self.valid_cards(lord_cards):
            while True:
                print("错误的输入，请重新输入: ")
                input_cards = raw_input('')
                self.check_quit_command(input_cards)
                lord_cards = self.format_cards(input_cards.split())
                if self.valid_cards(lord_cards):
                    break

        print("请输入农民的最初牌型：")
        input_cards = raw_input('')
        self.check_quit_command(input_cards)
        farmer_cards = self.format_cards(input_cards.split())

        if not self.valid_cards(farmer_cards):
            while True:
                print("错误的输入，请重新输入: ")
                input_cards = raw_input('')
                self.check_quit_command(input_cards)
                farmer_cards = self.format_cards(input_cards.split())
                if self.valid_cards(farmer_cards):
                    break

        # Start playing!

        current_player = 'Farmer'  # 'Farmer' or 'Lord'

        while True:  # Playing
            if current_player == 'Farmer':
                print('现在轮到农民出牌: ')
                input_move = raw_input('')
                self.check_quit_command(input_move)

                if self.pass_move(input_move):
                    current_move = []
                else:
                    current_move = self.format_cards(input_move.split())
                    if not self.valid_move(current_move, farmer_cards):
                        while True:
                            print("错误的出牌，请重新输入: ")
                            input_move = raw_input('')
                            self.check_quit_command(input_move)
                            if self.pass_move(input_move):
                                current_move = []
                            else:
                                current_move = self.format_cards(input_move.split())
                                if self.valid_move(current_move, farmer_cards):
                                    break

                farmer_cards = self.get_rest_cards(current_move, farmer_cards)
                if len(farmer_cards) == 0:
                    print("农民胜利!!!")
                    exit(0)
                else:
                    current_player = 'LandLord'

            else:  # Now it's turn to Landlord
                print('现在轮到地主出牌: ')
                input_move = raw_input('')
                self.check_quit_command(input_move)

                if self.pass_move(input_move):
                    current_move = []
                else:
                    current_move = self.format_cards(input_move.split())
                    if not self.valid_move(current_move, lord_cards):
                        while True:
                            print("错误的出牌，请重新输入: ")
                            input_move = raw_input('')
                            self.check_quit_command(input_move)
                            if self.pass_move(input_move):
                                current_move = []
                            else:
                                current_move = self.format_cards(input_move.split())
                                if self.valid_move(current_move, lord_cards):
                                    break

                lord_cards = self.get_rest_cards(current_move, lord_cards)
                if len(lord_cards) == 0:
                    print("地主胜利!!!")
                    exit(0)
                else:
                    current_player = 'Farmer'

