from common import MIN_SINGLE_CARDS, MIN_PAIRS, MIN_TRIPLES


TYPE_0_PASS = 0
TYPE_1_SINGLE = 1
TYPE_2_PAIR = 2
TYPE_3_TRIPLE = 3
TYPE_4_BOMB = 4
TYPE_5_KING_BOMB = 5
TYPE_6_3_1 = 6
TYPE_7_3_2 = 7 
TYPE_8_SERIAL_SINGLE = 8
TYPE_9_SERIAL_PAIR = 9
TYPE_10_SERIAL_TRIPLE = 10
TYPE_11_SERIAL_3_1 = 11
TYPE_12_SERIAL_3_2 = 12
TYPE_13_4_2 = 13
TYPE_14_4_4 = 14
TYPE_99_WRONG = 99


# For Debug
MOVE_TYPES_STR = {
    TYPE_0_PASS: "Pass", 
    TYPE_1_SINGLE: "Single", 
    TYPE_2_PAIR: "Pair", 
    TYPE_3_TRIPLE: "Triple", 
    TYPE_4_BOMB: "Bomb!", 
    TYPE_5_KING_BOMB: "King Bomb!!!", 
    TYPE_6_3_1: "3 + 1", 
    TYPE_7_3_2: "3 + 2", 
    TYPE_8_SERIAL_SINGLE: "Serial Single", 
    TYPE_9_SERIAL_PAIR: "Serial Pair", 
    TYPE_10_SERIAL_TRIPLE: "Serial Triple", 
    TYPE_11_SERIAL_3_1: "Serial 3 + 1", 
    TYPE_12_SERIAL_3_2: "Serial 3 + 2", 
    TYPE_13_4_2: "4 + 2", 
    TYPE_14_4_4: "4 + 2 Pairs", 
    TYPE_99_WRONG: "Wrong Type!"
}


def is_increased_seq_by_one(move):
    """
        move is a sorted list
    """
    result = True

    i = 0
    while i < len(move)-1:
        j = i + 1
        if move[j] - move[i] != 1:
            result = False
            break
        i += 1
    return result


class MoveClassifier(object):

    def get_move_type(self, move):
        # move must be a sorted list
        
        if move is None:
            return TYPE_0_PASS
        if not isinstance(move, list):
            return TYPE_99_WRONG
            
        len_move = len(move)
        len_set_move = len(set(move))
        
        if len_move == 0:
            return TYPE_0_PASS
            
        if len_move == 1:
            return TYPE_1_SINGLE
            
        if len_move == 2:
            if move[0] == move[1]:
                return TYPE_2_PAIR
            elif move == [20, 30]:  # Kings
                return TYPE_5_KING_BOMB
            else:
                return TYPE_99_WRONG
                
        if len_move == 3:
            if len_set_move == 1:
                return TYPE_3_TRIPLE
            else:
                return TYPE_99_WRONG
                
        if len_move == 4:
            if len_set_move == 1:
                return TYPE_4_BOMB
            elif len_set_move == 2:
                if move[0] == move[1] == move[2] or\
                   move[1] == move[2] == move[3]:
                    return TYPE_6_3_1
                else: 
                    return TYPE_99_WRONG
            else:
                return TYPE_99_WRONG
                
        if len_move == 5:
            if len_set_move in [1, 3, 4]:
                return TYPE_99_WRONG
            elif len_set_move == 2:
                return TYPE_7_3_2
            else:  # len_set_move == 5
                if move[0] + 1 == move[1] and \
                   move[1] + 1 == move[2] and \
                   move[2] + 1 == move[3] and \
                   move[3] + 1 == move[4]:
                    return TYPE_8_SERIAL_SINGLE
                else:
                    return TYPE_99_WRONG

        # Simple classifying is done. Let's do harder work.

        cards = dict()
        for i in move:
            if i in cards:
                cards[i] += 1
            else:
                cards[i] = 1

        card_types = len(cards.keys())
        count_dict = dict()
        for _, v in cards.items():
            if v in count_dict:
                count_dict[v] += 1
            else:
                count_dict[v] = 1

        if len(move) == 6:
            if card_types == 3 and \
               count_dict.get(4) == 1 and \
               count_dict.get(1) == 2:
                return TYPE_13_4_2

            elif card_types == 3 and count_dict.get(2) == 3:
                return TYPE_9_SERIAL_PAIR, 3  # 3 serial pairs

            elif card_types == 6 and count_dict.get(1) == 6:
                if is_increased_seq_by_one(move):
                    return TYPE_8_SERIAL_SINGLE, 6
                else:
                    return TYPE_99_WRONG

            else:
                return TYPE_99_WRONG

        if len(move) == 8 and \
           card_types == 3 and \
           count_dict.get(4) == 1 and \
           count_dict.get(2) == 2:
            return TYPE_14_4_4

        if card_types == count_dict.get(1) and \
           card_types >= MIN_SINGLE_CARDS and \
           is_increased_seq_by_one(move):
            return TYPE_8_SERIAL_SINGLE

        if card_types == count_dict.get(2) and \
           card_types >= MIN_PAIRS and \
           is_increased_seq_by_one(sorted(list(set(move)))):
            return TYPE_9_SERIAL_PAIR

        if card_types == count_dict.get(3) and \
           card_types >= MIN_TRIPLES and \
           is_increased_seq_by_one(sorted(list(set(move)))):
            return TYPE_10_SERIAL_TRIPLE

        # Check Type 11 and Type 12
        if count_dict.get(3) >= MIN_TRIPLES:
            serial_3 = list()
            single = list()
            pair = list()

            for k, v in cards.items():
                if v == 3:
                    serial_3.append(k)
                elif v == 1:
                    single.append(k)
                elif v == 2:
                    pair.append(k)
                else:  # no other possibilities
                    return TYPE_99_WRONG

            if is_increased_seq_by_one(sorted(serial_3)):
                if len(serial_3) == len(single) and card_types == len(serial_3)*2:
                    return TYPE_11_SERIAL_3_1
                if len(serial_3) == len(pair) and card_types == len(serial_3)*2:
                    return TYPE_12_SERIAL_3_2

            return TYPE_99_WRONG

        return TYPE_99_WRONG
