#ifndef MOVEFILTER_HPP
#define MOVEFILTER_HPP

#include <vector>

static vector<vector<int>> _common_handle(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    vector<vector<int>> new_moves;
    for (auto move : moves) {
        if (move[0] > rival_move[0]) {
            new_moves.push_back(move);
        }
    }
    return new_moves;
}

vector<vector<int>> filter_type_1_single(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _common_handle(moves, rival_move);
}

vector<vector<int>> filter_type_2_pair(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _common_handle(moves, rival_move);
}

vector<vector<int>> filter_type_3_triple(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _common_handle(moves, rival_move);
}

vector<vector<int>> filter_type_4_bomb(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _common_handle(moves, rival_move);
}

// no need to filter for TYPE_5_KING_BOMB

vector<vector<int>> filter_type_6_3_1(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    vector<vector<int>> filtered_moves;
    int target_rival_card = 999;
    unordered_map<int, int> rival_dict;
    for (auto card : rival_move) {
        if (rival_dict.find(card) == rival_dict.end()) {
            rival_dict[card] = 1;
        }
        else {
            target_rival_card = card;
            break;
        }
    }
    
    for (auto move : moves) {
        unordered_map<int, int> move_dict;
        for (auto card : move) {
            if (move_dict.find(card) == move_dict.end()) {
                move_dict[card] = 1;
            }
            else {  // card exists in move_dict already
                if (card > target_rival_card) {
                    filtered_moves.push_back(move);
                }
                break;
            }
        }
    }
    return filtered_moves;
}

vector<vector<int>> filter_type_7_3_2(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    vector<vector<int>> filtered_moves;
    int target_rival_card = 999;
    unordered_map<int, int> rival_dict;
    for (auto card : rival_move) {
        if (rival_dict.find(card) == rival_dict.end()) {
            rival_dict[card] = 1;
        }
        else {
            rival_dict[card] ++;
            if (rival_dict[card] == 3) {
                target_rival_card = card;
                break;
            }
        }
    }
    
    for (auto move : moves) {
        unordered_map<int, int> move_dict;
        for (auto card : move) {
            if (move_dict.find(card) == move_dict.end()) {
                move_dict[card] = 1;
            }
            else {
                move_dict[card] ++;
                if (move_dict[card] == 3) {
                    if (card > target_rival_card) {
                        filtered_moves.push_back(move);
                    }
                    break;
                }
            }
        }
    }
    return filtered_moves;
}

vector<vector<int>> filter_type_8_serial_single(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _common_handle(moves, rival_move);
}

vector<vector<int>> filter_type_9_serial_pair(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _common_handle(moves, rival_move);
}

vector<vector<int>> filter_type_10_serial_triple(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _common_handle(moves, rival_move);
}

static vector<vector<int>> _filter_type_11_and_type_12(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    vector<vector<int>> filtered_moves;

    unordered_map<int, int> rival_move_dict;
    vector<int> rival_triples;
    for (auto card : rival_move) {
        if (rival_move_dict.find(card) == rival_move_dict.end()) {
            rival_move_dict[card] = 1;
        }
        else {
            rival_move_dict[card] ++;
            if (rival_move_dict[card] == 3) {
                rival_triples.push_back(card);
            }
        }
    }
    sort(rival_triples.begin(), rival_triples.end());

    for (auto move : moves) {
        vector<int> move_triples;
        unordered_map<int, int> move_dict;
        for (auto card : move) {
            if (move_dict.find(card) == move_dict.end()) {
                move_dict[card] = 1;
            }
            else {
                move_dict[card] ++;
                if (move_dict[card] == 3) {
                    move_triples.push_back(card);
                }
            }
        }
        sort(move_triples.begin(), move_triples.end());
        if (move_triples[0] > rival_triples[0]) {
            filtered_moves.push_back(move);
        }
    }
    return filtered_moves;
}

vector<vector<int>> filter_type_11_serial_3_1(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _filter_type_11_and_type_12(moves, rival_move);
}

vector<vector<int>> filter_type_12_serial_3_2(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _filter_type_11_and_type_12(moves, rival_move);
}

static vector<vector<int>> _filter_type_13_and_type_14(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    vector<vector<int>> filtered_moves;

    int target_rival_card = 999;
    unordered_map<int, int> rival_dict;
    for (auto card : rival_move) {
        if (rival_dict.find(card) == rival_dict.end()) {
            rival_dict[card] = 1;
        }
        else {
            rival_dict[card] ++;
            if (rival_dict[card] == 4) {
                target_rival_card = card; 
                break;
            }
        }
    }

    for (auto move : moves) {
        int bomb_card = -1;
        unordered_map<int, int> move_dict;
        for (auto card : move) {
            if (move_dict.find(card) == move_dict.end()) {
                move_dict[card] = 1;
            }
            else {
                move_dict[card] ++;
                if (move_dict[card] == 4) {
                    bomb_card = card;
                    break;
                }
            }
        }
        if (bomb_card > target_rival_card) {
            filtered_moves.push_back(move);
        }
    }
    return filtered_moves;
}

vector<vector<int>> filter_type_13_4_2(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _filter_type_13_and_type_14(moves, rival_move);
}

vector<vector<int>> filter_type_14_4_2_2(const vector<vector<int>>& moves, const vector<int>& rival_move)
{
    return _filter_type_13_and_type_14(moves, rival_move);
}

#endif