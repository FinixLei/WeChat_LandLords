import copy
from common import calc_time


class MovesGener(object):

    MIN_SINGLE_CARDS = 5
    MIN_PAIRS = 3
    MIN_TRIPLES = 2

    def __init__(self, cards_list=list()):
        self.cards_list = cards_list
        self.cards = dict()
        
        for i in self.cards_list:
            if i in self.cards:
                self.cards[i] += 1
            else:
                self.cards[i] = 1
                
        self.single_card_moves = list()
        self.pair_moves = list()
        self.triple_cards_moves = list()
        self.bomb_moves = list()
        self.final_bomb_moves = list()
        
    def _gen_serial_moves(self, cards, min_serial, repeat=1):
        single_cards = sorted(list(set(cards)))
        longest_lists = list()
        
        start = i = 0
        count = 1
        while i < len(single_cards):
            if i+1 < len(single_cards) and single_cards[i+1] - single_cards[i] == 1:
                count += 1
                i += 1
            else:
                if count >= min_serial:
                    long_list = single_cards[start: start+count]
                    step = min_serial
                    while step <= count:
                        index = 0
                        while index + step <= len(long_list):
                            target_moves = sorted(long_list[index: index+step] * repeat)
                            longest_lists.append(target_moves)
                            index += 1
                        step += 1
                    
                i += 1
                start = i
                count = 1
            
        return longest_lists

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
        
        for k,v in self.cards.items():
            if v >= 2:
                self.pair_moves.append([k, k])
        return self.pair_moves
        
    def gen_type_3_triple(self):
        if self.triple_cards_moves:
            return self.triple_cards_moves
        
        for k,v in self.cards.items():
            if v >= 3:
                self.triple_cards_moves.append([k, k, k])
        return self.triple_cards_moves
        
    def gen_type_4_bomb(self):
        if self.bomb_moves:
            return self.bomb_moves
        
        for k,v in self.cards.items():
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
        for k,v in self.cards.items():
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
        for k,v in self.cards.items():
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
        
    def gen_type_8_serial_single(self):
        return self._gen_serial_moves(self.cards_list, MovesGener.MIN_SINGLE_CARDS, repeat=1)
        
    def gen_type_9_serial_pair(self):
        single_pairs = list()
        for k,v in self.cards.items():
            if v >= 2:
                single_pairs.append(k)
                
        return self._gen_serial_moves(single_pairs, MovesGener.MIN_PAIRS, repeat=2)
        
    def gen_type_10_serial_triple(self):
        single_triples = list()
        for k,v in self.cards.items():
            if v >= 3:
                single_triples.append(k)
                
        return self._gen_serial_moves(single_triples, MovesGener.MIN_TRIPLES, repeat=3)
        
    # TODO: When generating serial moves,
    # we may need to assign an argument for specifying how many numbers of this "serial"
    
    def gen_type_13_4_2(self):
        four_cards = list()
        for k,v in self.cards.items():
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
        for k,v in self.cards.items():
            if v >= 4:
                four_cards.append(k)
        
        two_more_cards = list()
        for k,v in self.cards.items():
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
        
    @calc_time
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
        
        # moves.extend(self.gen_type_11_serial_3_1()) 
        # moves.extend(self.gen_type_12_serial_3_2()) 
        
        moves.extend(self.gen_type_13_4_2())
        moves.extend(self.gen_type_14_4_4())

        return moves
