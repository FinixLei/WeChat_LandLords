import copy


class MoveFilter(object):
    def filter_type_1_single(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_2_pair(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_3_triple(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_4_bomb(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    # No need to filter for type_5_king_bomb

    def filter_type_6_3_1(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_7_3_2(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_8_serial_single(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_9_serial_pair(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_10_serial_triple(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_11_serial_3_1(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_12_serial_3_2(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_13_4_2(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves

    def filter_type_14_4_4(self, moves, rival_move):
        new_moves = copy.deepcopy(moves)
        return new_moves
