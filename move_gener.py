import copy
from utils import calc_time, GenAnyN, \
    MIN_SINGLE_CARDS, MIN_PAIRS, MIN_TRIPLES


class MovesGener(object):

    def __init__(self, cards_list=list()):
        self.cards_list = cards_list
        self.cards_dict = dict()
        
        for i in self.cards_list:
            if i in self.cards_dict:
                self.cards_dict[i] += 1
            else:
                self.cards_dict[i] = 1
                
        self.single_card_moves = list()
        self.pair_moves = list()
        self.triple_cards_moves = list()
        self.bomb_moves = list()
        self.final_bomb_moves = list()

    def _gen_serial_moves(self, cards, min_serial, repeat=1, repeat_num=0):
        """
        :param cards: A list of single cards, each may represent several same cards.
        :param min_serial: The required minimum sequence, e.g. for pairs, it's 3.
        :param repeat: 1 means single, 2 means pair, 3 means triple cards.
        :param repeat_num: How many sections in the sequence,
                            e.g. for 3,3,3,4,4,4, it is 2.
                            The default value 0 means no limitation
        :return: moves: serial moves, e.g. sequenced pairs, sequenced 3+1, etc.
        """
        if repeat_num < min_serial:  # at least repeat_num is min_serial
            repeat_num = 0

        single_cards = sorted(list(set(cards)))
        seq_records = list()
        moves = list()

        start = i = 0
        longest = 1
        while i < len(single_cards):
            if i+1 < len(single_cards) and single_cards[i+1] - single_cards[i] == 1:
                longest += 1
                i += 1
            else:
                seq_records.append((start, longest))
                i += 1
                start = i
                longest = 1

        for seq in seq_records:
            if seq[1] < min_serial:
                continue
            start, longest = seq[0], seq[1]
            longest_list = single_cards[start: start+longest]

            if repeat_num == 0:  # No limitation on how many sequences
                steps = min_serial
                while steps <= longest:
                    index = 0
                    while steps + index <= longest:
                        target_moves = sorted(longest_list[index: index+steps] * repeat)
                        moves.append(target_moves)
                        index += 1
                    steps += 1

            else:  # repeat_num > 0
                if longest < repeat_num:
                    continue
                index = 0
                while index + repeat_num <= longest:
                    target_moves = sorted(longest_list[index: index+repeat_num] * repeat)
                    moves.append(target_moves)
                    index += 1

        return moves

    def gen_type_1_single(self):
        if self.single_card_moves:
            return self.single_card_moves
            
        if len(self.cards_list) > 0:
            for i in set(self.cards_list):
                self.single_card_moves.append([i])
        return self.single_card_moves
        
    def gen_type_2_pair(self):
        if self.pair_moves:
            return self.pair_moves
        
        for k, v in self.cards_dict.items():
            if v >= 2:
                self.pair_moves.append([k, k])
        return self.pair_moves
        
    def gen_type_3_triple(self):
        if self.triple_cards_moves:
            return self.triple_cards_moves
        
        for k, v in self.cards_dict.items():
            if v >= 3:
                self.triple_cards_moves.append([k, k, k])
        return self.triple_cards_moves
        
    def gen_type_4_bomb(self):
        if self.bomb_moves:
            return self.bomb_moves
        
        for k, v in self.cards_dict.items():
            if v >= 4:
                self.bomb_moves.append([k, k, k, k])
        return self.bomb_moves
        
    def gen_type_5_king_bomb(self):
        if self.final_bomb_moves:
            return self.final_bomb_moves
        if 20 in self.cards_list and 30 in self.cards_list:
            self.final_bomb_moves.append([20, 30])
        return self.final_bomb_moves
        
    def gen_type_6_3_1(self):
        triple_cards = list()
        for k, v in self.cards_dict.items():
            if v >= 3:
                triple_cards.append(k)
                
        result = list()
        single_cards = list(set(self.cards_list))
        for t in triple_cards:
            for i in single_cards:
                if t != i:
                    result.append([t, t, t, i])
        return result
        
    def gen_type_7_3_2(self):
        triple_cards = list()
        two_more_cards = list()
        for k, v in self.cards_dict.items():
            if v >= 3:
                triple_cards.append(k)
            if v >= 2:
                two_more_cards.append(k)
                
        result = list()
        for t in triple_cards:
            for i in two_more_cards:
                if t != i:
                    result.append([t, t, t, i, i])
        return result
        
    def gen_type_8_serial_single(self, repeat_num=0):
        return self._gen_serial_moves(self.cards_list,
                                      MIN_SINGLE_CARDS,
                                      repeat=1,
                                      repeat_num=repeat_num)

    def gen_type_9_serial_pair(self, repeat_num=0):
        single_pairs = list()
        for k, v in self.cards_dict.items():
            if v >= 2:
                single_pairs.append(k)
                
        return self._gen_serial_moves(single_pairs,
                                      MIN_PAIRS,
                                      repeat=2,
                                      repeat_num=repeat_num)
        
    def gen_type_10_serial_triple(self, repeat_num=0):
        single_triples = list()
        for k, v in self.cards_dict.items():
            if v >= 3:
                single_triples.append(k)
                
        return self._gen_serial_moves(single_triples,
                                      MIN_TRIPLES,
                                      repeat=3,
                                      repeat_num=repeat_num)

    def gen_type_11_serial_3_1(self, repeat_num=0):
        serial_3_moves = self.gen_type_10_serial_triple(repeat_num=repeat_num)
        serial_3_1_moves = list()

        for s3 in serial_3_moves:  # s3 is like [3,3,3,4,4,4]
            cards = copy.deepcopy(self.cards_list)
            s3_set = set(s3)
            new_cards = [i for i in cards if i not in s3_set]

            # Get any s3_len items from cards
            gan = GenAnyN(new_cards, len(s3_set))
            any_n_lists = gan.gen_n_cards_lists()

            for i in any_n_lists:
                move = s3 + i  # like [3,3,3,4,4,4] + [5,6]
                serial_3_1_moves.append(move)

        return serial_3_1_moves

    def gen_type_12_serial_3_2(self, repeat_num=0):
        serial_3_moves = self.gen_type_10_serial_triple(repeat_num=repeat_num)
        serial_3_2_moves = list()
        pair_set = sorted([k for k, v in self.cards_dict.items() if v >= 2])

        for s3 in serial_3_moves:
            s3_set = set(s3)
            pair_candidates = copy.deepcopy(pair_set)
            pair_candidates = [i for i in pair_candidates if i not in s3_set]

            # Get any s3_len items from cards
            gan = GenAnyN(pair_candidates, len(s3_set))
            any_n_lists = gan.gen_n_cards_lists()
            for i in any_n_lists:
                move = sorted(s3 + i*2)  # like [3,3,3, 4,4,4] + [7,8]*2
                serial_3_2_moves.append(move)

        return serial_3_2_moves

    def gen_type_13_4_2(self):
        four_cards = list()
        for k, v in self.cards_dict.items():
            if v >= 4:
                four_cards.append(k)
        
        result = list()
        for fc in four_cards:
            cards_list = copy.deepcopy(self.cards_list)
            for _ in range(4):
                cards_list.remove(fc)
                
            i = 0
            while i < len(cards_list)-1: 
                j = i + 1
                while j < len(cards_list):
                    tmp_move = [fc, fc, fc, fc, cards_list[i], cards_list[j]]
                    result.append(tmp_move)
                    j += 1
                i += 1
        
        return result
    
    def gen_type_14_4_4(self):
        four_cards = list()
        for k, v in self.cards_dict.items():
            if v >= 4:
                four_cards.append(k)
        
        two_more_cards = list()
        for k, v in self.cards_dict.items():
            if v in [2, 3]:
                two_more_cards.append(k)
        
        result = list()
        if len(two_more_cards) < 2:
            return []
        
        for fc in four_cards:
            cards_list = copy.deepcopy(self.cards_list)
            for _ in range(4):
                cards_list.remove(fc)
                
            i = 0
            while i < len(two_more_cards)-1: 
                j = i + 1
                while j < len(two_more_cards):
                    tmp_move = [fc, fc, fc, fc, 
                                two_more_cards[i], two_more_cards[i], 
                                two_more_cards[j], two_more_cards[j]]
                    result.append(tmp_move)
                    j += 1
                i += 1
        
        return result
        
    # @calc_time
    def gen_moves(self):
        moves = list()
        moves.extend(self.gen_type_1_single())
        moves.extend(self.gen_type_2_pair())
        moves.extend(self.gen_type_3_triple())
        moves.extend(self.gen_type_4_bomb())
        moves.extend(self.gen_type_5_king_bomb())
        moves.extend(self.gen_type_6_3_1())
        moves.extend(self.gen_type_7_3_2())
        moves.extend(self.gen_type_8_serial_single())
        moves.extend(self.gen_type_9_serial_pair())
        moves.extend(self.gen_type_10_serial_triple())
        moves.extend(self.gen_type_11_serial_3_1())
        moves.extend(self.gen_type_12_serial_3_2())
        moves.extend(self.gen_type_13_4_2())
        moves.extend(self.gen_type_14_4_4())
        return moves
