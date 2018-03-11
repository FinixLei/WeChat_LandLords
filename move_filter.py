class MoveFilter(object):
    def _common_handle(self, moves, rival_move):
        new_moves = list()
        for move in moves:
            if move[0] > rival_move[0]:
                new_moves.append(move)
        return new_moves

    def filter_type_1_single(self, moves, rival_move):
        return self._common_handle(moves, rival_move)

    def filter_type_2_pair(self, moves, rival_move):
        return self._common_handle(moves, rival_move)

    def filter_type_3_triple(self, moves, rival_move):
        return self._common_handle(moves, rival_move)

    def filter_type_4_bomb(self, moves, rival_move):
        return self._common_handle(moves, rival_move)

    # No need to filter for type_5_king_bomb

    def filter_type_6_3_1(self, moves, rival_move):
        rival_card_dict = dict()
        target_rival_card = -1
        for card in rival_move:
            if card not in rival_card_dict:
                rival_card_dict[card] = 1
            else:
                target_rival_card = card
                break

        new_moves = list()
        for move in moves:
            card_dict = dict()
            for card in move:
                if card not in card_dict:
                    card_dict[card] = 1
                else:
                    if card > target_rival_card:
                        new_moves.append(move)
                        break

        return new_moves

    def filter_type_7_3_2(self, moves, rival_move):
        rival_card_dict = dict()
        target_rival_card = -1
        for card in rival_move:
            if card not in rival_card_dict:
                rival_card_dict[card] = 1
            else:
                rival_card_dict[card] += 1
                if rival_card_dict[card] == 3:
                    target_rival_card = card
                    break

        new_moves = list()
        for move in moves:
            card_dict = dict()
            for card in move:
                if card not in card_dict:
                    card_dict[card] = 1
                else:
                    card_dict[card] += 1
                    if card_dict[card] == 3 and \
                            card > target_rival_card:
                        new_moves.append(move)
                        break

        return new_moves

    def filter_type_8_serial_single(self, moves, rival_move):
        return self._common_handle(moves, rival_move)

    def filter_type_9_serial_pair(self, moves, rival_move):
        return self._common_handle(moves, rival_move)

    def filter_type_10_serial_triple(self, moves, rival_move):
        return self._common_handle(moves, rival_move)

    def filter_type_11_serial_3_1(self, moves, rival_move):
        rival_triple_list = list()
        rival_dict = dict()
        for card in rival_move:
            if card not in rival_dict:
                rival_dict[card] = 1
            else:
                rival_dict[card] += 1
                if rival_dict[card] == 3:
                    rival_triple_list.append(card)
        rival_triple_list = sorted(rival_triple_list)

        new_moves = list()

        for move in moves:
            move_dict = dict()
            move_triple_list = list()
            for card in move:
                if card not in move_dict:
                    move_dict[card] = 1
                else:
                    move_dict[card] += 1
                    if move_dict[card] == 3:
                        move_triple_list.append(card)
            move_triple_list = sorted(move_triple_list)
            if move_triple_list[0] > rival_triple_list[0]:
                new_moves.append(move)

        return new_moves

    def filter_type_12_serial_3_2(self, moves, rival_move):
        rival_triple_list = list()
        rival_dict = dict()
        for card in rival_move:
            if card not in rival_dict:
                rival_dict[card] = 1
            else:
                rival_dict[card] += 1
                if rival_dict[card] == 3:
                    rival_triple_list.append(card)
        rival_triple_list = sorted(rival_triple_list)

        new_moves = list()

        for move in moves:
            move_dict = dict()
            move_triple_list = list()
            for card in move:
                if card not in move_dict:
                    move_dict[card] = 1
                else:
                    move_dict[card] += 1
                    if move_dict[card] == 3:
                        move_triple_list.append(card)
            move_triple_list = sorted(move_triple_list)
            if move_triple_list[0] > rival_triple_list[0]:
                new_moves.append(move)

        return new_moves

    def filter_type_13_4_2(self, moves, rival_move):
        rival_card_dict = dict()
        target_rival_card = -1
        for card in rival_move:
            if card not in rival_card_dict:
                rival_card_dict[card] = 1
            else:
                rival_card_dict[card] += 1
                if rival_card_dict[card] == 4:
                    target_rival_card = card
                    break

        new_moves = list()
        for move in moves:
            card_dict = dict()
            for card in move:
                if card not in card_dict:
                    card_dict[card] = 1
                else:
                    card_dict[card] += 1
                    if card_dict[card] == 4 and \
                            card > target_rival_card:
                        new_moves.append(move)
                        break

        return new_moves

    def filter_type_14_4_4(self, moves, rival_move):
        rival_card_dict = dict()
        target_rival_card = -1
        for card in rival_move:
            if card not in rival_card_dict:
                rival_card_dict[card] = 1
            else:
                rival_card_dict[card] += 1
                if rival_card_dict[card] == 4:
                    target_rival_card = card
                    break

        new_moves = list()
        for move in moves:
            card_dict = dict()
            for card in move:
                if card not in card_dict:
                    card_dict[card] = 1
                else:
                    card_dict[card] += 1
                    if card_dict[card] == 4 and \
                            card > target_rival_card:
                        new_moves.append(move)
                        break

        return new_moves
