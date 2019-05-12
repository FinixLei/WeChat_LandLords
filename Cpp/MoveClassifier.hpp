#ifndef MOVECLASSIFIER_H
#define MOVECLASSIFIER_H

#include <unordered_map>
#include <string>

#include "utils.hpp"

const int TYPE_0_PASS           = 0;
const int TYPE_1_SINGLE         = 1;
const int TYPE_2_PAIR           = 2;
const int TYPE_3_TRIPLE         = 3;
const int TYPE_4_BOMB           = 4;
const int TYPE_5_KING_BOMB      = 5;
const int TYPE_6_3_1            = 6;
const int TYPE_7_3_2            = 7;
const int TYPE_8_SERIAL_SINGLE  = 8;
const int TYPE_9_SERIAL_PAIR    = 9;
const int TYPE_10_SERIAL_TRIPLE = 10;
const int TYPE_11_SERIAL_3_1    = 11;
const int TYPE_12_SERIAL_3_2    = 12;
const int TYPE_13_4_2           = 13;
const int TYPE_14_4_2_2         = 14;
const int TYPE_99_WRONG         = 99;

// For Debug
unordered_map<int, string> MOVE_TYPES_STR ({
    {TYPE_0_PASS,           "Pass"},
    {TYPE_1_SINGLE,         "Single"},
    {TYPE_2_PAIR,           "Pair"},
    {TYPE_3_TRIPLE,         "Triple"},
    {TYPE_4_BOMB,           "Bomb!"},
    {TYPE_5_KING_BOMB,      "King Bomb!!!"},
    {TYPE_6_3_1,            "3 + 1"},
    {TYPE_7_3_2,            "3 + 2"},
    {TYPE_8_SERIAL_SINGLE,  "Serial Single"},
    {TYPE_9_SERIAL_PAIR,    "Serial Pair"},
    {TYPE_10_SERIAL_TRIPLE, "Serial Triple"},
    {TYPE_11_SERIAL_3_1,    "Serial 3 + 1"},
    {TYPE_12_SERIAL_3_2,    "Serial 3 + 2"},
    {TYPE_13_4_2,           "4 + 2"},
    {TYPE_14_4_2_2,         "4 + 2 Pairs"},
    {TYPE_99_WRONG,         "Wrong Type!"}
});

static bool is_increased_by_one(const vector<int>& seq)
{
    int size = seq.size();
    for (int i=0; i<size-1; ++i) {
        if (seq[i+1] - seq[i] != 1) return false;
    }
    return true;
}

typedef int MOVE_TYPE;
typedef int SERIAL_NUM;
pair<MOVE_TYPE, SERIAL_NUM> get_move_type(const vector<int>& move)
{
    int size = move.size();
    set<int> move_set(move.begin(), move.end());
    int set_size = move_set.size();

    if (size == 0) return {TYPE_0_PASS, -1};

    if (size == 1) return {TYPE_1_SINGLE, -1};

    if (size == 2) {
        if (set_size == 1) {
            return {TYPE_2_PAIR, -1};
        }
        else if(set_size == 2 && ((move[0]==20 && move[1]==30) || (move[0]==30 && move[1]==20))) {
            return {TYPE_5_KING_BOMB, -1};
        }
        else {
            return {TYPE_99_WRONG, -1};
        }
    }

    if (size == 3) {
        if (set_size == 1) return {TYPE_3_TRIPLE, -1};
        else return {TYPE_99_WRONG, -1};
    }

    if (size == 4) {
        if (set_size == 1) {
            return {TYPE_4_BOMB, -1};
        }
        else if (set_size == 2 && ((move[0]==move[1] && move[1]==move[2]) 
                                   || (move[1]==move[2] && move[2]==move[3]))
                ) {
            return {TYPE_6_3_1, -1};
        }
        else {
            return {TYPE_99_WRONG, -1};
        }
    }

    if (size == 5) {
        if (set_size == 2) {
            return {TYPE_7_3_2, -1}; 
        }
        else if (set_size == 5 && is_increased_by_one(move)) {
            return {TYPE_8_SERIAL_SINGLE, 5};
        }
        else {
            return {TYPE_99_WRONG, -1};
        }
    }

    // Lazy Computing: Do something complicated from now on 

    unordered_map<int, int> move_dict;
    for (auto card : move) {
        if (move_dict.find(card) == move_dict.end()) {
            move_dict[card] = 1;
        }
        else {
            move_dict[card] ++;
        }
    }

    // Key: a number which stands for how many cards of one or more specific card type(s)
    // Value: how many card types owns the same number 
    // Example: 33 44 55 66, then it is {2, 4} - key=2, value=4
    unordered_map<int, int> count_dict;
    for (auto move_item : move_dict) {
        if (count_dict.find(move_item.second) == count_dict.end()) {
            count_dict[move_item.second] = 1;
        }
        else {
            count_dict[move_item.second] ++; 
        }
    }

    if (size == 6) {
        if (set_size == 2) {
            if (count_dict[4] == 1 && count_dict[2] == 1) return {TYPE_13_4_2, -1};
            else return {TYPE_99_WRONG, -1};
        }
        else if (set_size == 3) {
            if (count_dict[4] == 1 && count_dict[1] == 2) return {TYPE_13_4_2, -1};
            else if (count_dict[2] == 3) {
                vector<int> tmp(move_set.begin(), move_set.end());
                sort(tmp.begin(), tmp.end());
                if (is_increased_by_one(tmp)) return {TYPE_9_SERIAL_PAIR, 3};
                else return {TYPE_99_WRONG, -1};
            }
            else {
                return {TYPE_99_WRONG, -1};
            }
        }
        else if (set_size == 6) {
            if (count_dict[1] == 6 && is_increased_by_one(move)) return {TYPE_8_SERIAL_SINGLE, 6};
            else return {TYPE_99_WRONG, -1};
        }
        else {
            return {TYPE_99_WRONG, -1};
        }
    }

    // Only for checking TYPE_14_4_2_2
    if (size==8 && set_size==3 && count_dict[4]==1 && count_dict[2]==2) {
        return {TYPE_14_4_2_2, -1};
    }

    // Check for TYPE_8_SERIAL_SINGLE
    if (set_size == count_dict[1] && set_size >= MIN_SINGLE && is_increased_by_one(move)) {
        return {TYPE_8_SERIAL_SINGLE, set_size};
    }

    // Check for TYPE_9_SERIAL_PAIR
    if (set_size == count_dict[2] && set_size >= MIN_PAIRS) {
        vector<int> tmp(move_set.begin(), move_set.end());
        sort(tmp.begin(), tmp.end());
        if (is_increased_by_one(tmp)) {
            return {TYPE_9_SERIAL_PAIR, set_size};
        }
    }

    // Check for TYPE_10_SERIAL_TRIPLE
    if (set_size == count_dict[3] && set_size >= MIN_TRIPLES) {
        vector<int> tmp(move_set.begin(), move_set.end());
        sort(tmp.begin(), tmp.end());
        if (is_increased_by_one(tmp)) {
            return {TYPE_10_SERIAL_TRIPLE, set_size};
        }
    }

    // Check for TYPE_11_SERIAL_3_1 and TYPE_12_SERIAL_3_2
    // This is the last checking. So, if it is not type_11 or type_12, 
    // it is a wrong type. 
    if (count_dict[3] >= MIN_TRIPLES) {
        vector<int> triples; 
        vector<int> singles;
        vector<int> pairs;
        for (auto card_item : move_dict) {
            if (card_item.second == 3) {
                triples.push_back(card_item.first);
            }
            else if (card_item.second == 2) {
                pairs.push_back(card_item.first);
            }
            else if (card_item.second == 1) {
                singles.push_back(card_item.first);
            }
            else {
                return {TYPE_99_WRONG, -1};
            }
        }

        sort(triples.begin(), triples.end());
        if (is_increased_by_one(triples)) {
            if (triples.size() == singles.size() && set_size == triples.size() + singles.size()) {
                return {TYPE_11_SERIAL_3_1, triples.size()};
            }
            if (triples.size() == pairs.size() && set_size == triples.size() + pairs.size()) {
                return {TYPE_12_SERIAL_3_2, triples.size()};
            }
        }
    }

    // For all other cases
    return {TYPE_99_WRONG, -1};
}

#endif