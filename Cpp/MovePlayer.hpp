#ifndef MOVEPLAYER_HPP
#define MOVEPLAYER_HPP

#include <vector>
#include <exception>
#include "utils.hpp"
#include "MoveGener.hpp"
#include "MoveFilter.hpp"
#include "MoveClassifier.hpp"


// cards      - current cards on hand
// rival_move - cards that rival played
// return:    - proper moves based on cards on hand
vector<vector<int>> get_proper_moves(vector<int>& cards, vector<int>& rival_move)
{
    vector<vector<int>> proper_moves;
    vector<vector<int>> all_moves;

    pair<MOVE_TYPE, SERIAL_NUM> move_type_pair = get_move_type(rival_move);
    int move_type = move_type_pair.first;
    int serial_num = move_type_pair.second;

    MoveGener mg(cards);

    if (move_type == TYPE_0_PASS) {
        proper_moves = mg.gen_all_moves();
    }
    else if (move_type == TYPE_1_SINGLE) {
        all_moves = mg.gen_type_1_single();
        proper_moves = filter_type_1_single(all_moves, rival_move);
    }
    else if (move_type == TYPE_2_PAIR) {
        all_moves = mg.gen_type_2_pair();
        proper_moves = filter_type_2_pair(all_moves, rival_move);
    }
    else if (move_type == TYPE_3_TRIPLE) {
        all_moves = mg.gen_type_3_triple();
        proper_moves = filter_type_3_triple(all_moves, rival_move);
    }
    else if (move_type == TYPE_4_BOMB) {
        all_moves = mg.gen_type_4_bomb();
        proper_moves = filter_type_4_bomb(all_moves,rival_move);
    }
    else if (move_type == TYPE_5_KING_BOMB) {
        proper_moves = {};
    }
    else if (move_type == TYPE_6_3_1) {
        all_moves = mg.gen_type_6_3_1();
        proper_moves = filter_type_6_3_1(all_moves, rival_move);
    }
    else if (move_type == TYPE_7_3_2) {
        all_moves = mg.gen_type_7_3_2();
        proper_moves = filter_type_7_3_2(all_moves, rival_move);
    }
    else if (move_type == TYPE_8_SERIAL_SINGLE) {
        all_moves = mg.gen_type_8_serial_single(serial_num);
        proper_moves = filter_type_8_serial_single(all_moves, rival_move);
    }
    else if (move_type == TYPE_9_SERIAL_PAIR) {
        all_moves = mg.gen_type_9_serial_pair(serial_num);
        proper_moves = filter_type_9_serial_pair(all_moves, rival_move);
    }
    else if (move_type == TYPE_10_SERIAL_TRIPLE) {
        all_moves = mg.gen_type_10_serial_triple(serial_num);
        proper_moves = filter_type_10_serial_triple(all_moves, rival_move);
    }
    else if (move_type == TYPE_11_SERIAL_3_1) {
        all_moves = mg.gen_type_11_serial_3_1(serial_num);
        proper_moves = filter_type_11_serial_3_1(all_moves, rival_move);
    }
    else if (move_type == TYPE_12_SERIAL_3_2) {
        all_moves = mg.gen_type_12_serial_3_2(serial_num);
        proper_moves = filter_type_12_serial_3_2(all_moves, rival_move);
    }
    else if (move_type == TYPE_13_4_2) {
        all_moves = mg.gen_type_13_4_2();
        proper_moves = filter_type_13_4_2(all_moves, rival_move);
    }
    else if (move_type == TYPE_14_4_2_2) {
        all_moves = mg.gen_type_14_4_2_2();
        proper_moves = filter_type_14_4_2_2(all_moves, rival_move);
    }
    else {
        throw "Invalid Move type!";
    }

    // Add bomb and king_bomb moves if needed
    if (move_type != TYPE_0_PASS && move_type != TYPE_4_BOMB && move_type != TYPE_5_KING_BOMB) {
        vector<vector<int>> bomb_moves = mg.gen_type_4_bomb();
        vector<vector<int>> king_bomb_moves = mg.gen_type_5_king_bomb();
        proper_moves.insert(proper_moves.end(), king_bomb_moves.begin(), king_bomb_moves.end());
        proper_moves.insert(proper_moves.end(), bomb_moves.begin(), bomb_moves.end());
    }

    // Add "pass" move
    if (rival_move.size() != 0) {
        proper_moves.push_back({});
    }

    // One kind of optimization, but need to be considered whether useful
    sort(proper_moves.begin(), proper_moves.end(), [&](const vector<int>&a, const vector<int>&b){return a.size()>b.size();});

    return proper_moves;
}

#endif
