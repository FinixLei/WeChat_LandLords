#ifndef MOVE_GENER_H
#define MOVE_GENER_H

#include <set>
#include <vector>
#include <unordered_map>

#include "utils.hpp"


class MoveGener {
public:
    MoveGener(std::vector<int> cards);
    ~MoveGener(){}

    vector<vector<int>> gen_type_1_single();
    vector<vector<int>> gen_type_2_pair();
    vector<vector<int>> gen_type_3_triple();
    vector<vector<int>> gen_type_4_bomb();
    vector<vector<int>> gen_type_5_king_bomb();
    vector<vector<int>> gen_type_6_3_1();
    vector<vector<int>> gen_type_7_3_2();
    vector<vector<int>> gen_type_8_serial_single(int serial_num=0);
    vector<vector<int>> gen_type_9_serial_pair(int serial_num=0);
    vector<vector<int>> gen_type_10_serial_triple(int serial_num=0);
    vector<vector<int>> gen_type_11_serial_3_1(int serial_num=0);
    vector<vector<int>> gen_type_12_serial_3_2(int serial_num=0);
    vector<vector<int>> gen_type_13_4_2();
    vector<vector<int>> gen_type_14_4_2_2();
    vector<vector<int>> gen_all_moves();

private:
    MoveGener(const MoveGener&) = delete;
    MoveGener operator=(const MoveGener&) = delete;

    // Generate move like {3, 3, 3, 4, 4, 4}
    // candidate_cards - for serial single, it's just cards
    //                   for serial pair, it's like 33446688
    //                   for serial triple, it's like 333555666
    // min_serial - the minimum repeated number, e.g. for pairs, it is 3: 334455
    // type       - single, pair, or triple: TYPE_SINGLE, TYPE_PAIR, TYPE_TRIPLE
    // serial_num    - how many sets are repeated, e.g. for 333444, it is 2
    //              0 means no limitation
    // return - all the serail moves satisfied the requirement
    vector<vector<int>> _gen_serial_moves(vector<int> candidate_cards, 
                                          int min_serial, 
                                          int type=TYPE_SINGLE, 
                                          int serial_num=0);

private:
    std::vector<int> cards;
    std::set<int> cards_set;
    std::unordered_map<int, int> cards_dict; // <card, serial_num>
    
    // below store basic moves
    vector<vector<int>> single_moves;
    vector<vector<int>> pair_moves;
    vector<vector<int>> triple_moves;
    vector<vector<int>> bomb_moves;
    vector<vector<int>> king_bomb_moves;
    vector<vector<int>> serial_pair_moves;
    vector<vector<int>> serial_triple_moves;
};

MoveGener::MoveGener(std::vector<int> cards) : \
        cards(cards), cards_set(cards.begin(), cards.end()) 
{
    for (auto i : cards) {
        auto it = cards_dict.find(i);
        if (it == cards_dict.end()) {
            cards_dict[i] = 1;
        }
        else {
            cards_dict[i] ++;
        }
    }
}

vector<vector<int>> MoveGener::_gen_serial_moves(vector<int>candidate_cards, 
                                                int min_serial, 
                                                int type, 
                                                int serial_num)
{
    vector<vector<int>> moves;  // result
    if (serial_num < min_serial) serial_num = 0;  // just for robust

    set<int> candidate_cards_set(candidate_cards.begin(), candidate_cards.end());
    vector<int> single_cards(candidate_cards_set.begin(), candidate_cards_set.end());
    sort(single_cards.begin(), single_cards.end());

    vector<pair<int, int>> seq_records;
    int size_single = single_cards.size();
    int start=0, index=0, longest=1;

    while (index < size_single) {
        if (index+1 < size_single && single_cards[index+1]-single_cards[index]==1) {
            ++ longest;
            ++ index;
        }
        else {
            // seq_records is like: {{3,2},{4,3},{5,2}}
            seq_records.push_back(pair<int, int>({start, longest}));
            ++ index;
            start = index;
            longest = 1;
        }
    }

    for (auto seq : seq_records) {
        if (seq.second < min_serial) continue;
        int start = seq.first, longest = seq.second;
        if (longest < min_serial) continue; 

        // one longest_list is like: {3, 4, 5}, next longest_list is like {8,9}
        vector<int> longest_list({&single_cards[start], &single_cards[start+longest]}); 

        if (serial_num == 0) {  // no limitation
            if (longest_list.size() < min_serial) continue;

            for (int length = min_serial; length <= longest; ++length) {
                for (int start_pos = 0; start_pos+length <= longest; ++start_pos) {
                    vector<int> tmp_move(&longest_list[start_pos], &longest_list[start_pos+length]);
                    vector<int> one_move;
                    for (int i=0; i<type; ++i) {
                        one_move.insert(one_move.end(), tmp_move.begin(), tmp_move.end());
                    }
                    sort(one_move.begin(), one_move.end());
                    moves.push_back(one_move);
                }
            }
        }
        else {  // serial_num > 0, i.e. serial_num is a fixed number, e.g. 5, that means it must be 34567 or 45678
            for (int start_pos = 0; start_pos + serial_num <= longest; ++ start_pos) {
                vector<int> tmp_move(&longest_list[start_pos], &longest_list[start_pos+serial_num]);
                vector<int> one_move;
                for (int i=0; i<type; ++i) {
                    one_move.insert(one_move.end(), tmp_move.begin(), tmp_move.end());
                }
                sort(one_move.begin(), one_move.end());
                moves.push_back(one_move);
            }
        }
    }

    return moves;
}

vector<vector<int>> MoveGener::gen_type_1_single()
{
    if (single_moves.size() > 0) return single_moves;

    for (auto card : cards_set) {
        vector<int> tmp({card});
        single_moves.push_back(tmp);
    }
    return single_moves;
}

vector<vector<int>> MoveGener::gen_type_2_pair()
{
    if (pair_moves.size() > 0) return pair_moves;

    for (auto card : cards_dict) {
        if (card.second >= 2) {
            vector<int> tmp({card.first, card.first});
            pair_moves.push_back(tmp);
        }
    }
    return pair_moves;
}

vector<vector<int>> MoveGener::gen_type_3_triple()
{
    if (triple_moves.size() > 0) return triple_moves;

    for (auto card : cards_dict) {
        if (card.second >= 3) {
            vector<int> tmp({card.first, card.first, card.first});
            triple_moves.push_back(tmp);
        }
    }
    return triple_moves;
}

vector<vector<int>> MoveGener::gen_type_4_bomb()
{
    if (bomb_moves.size() > 0) return bomb_moves;

    for (auto card : cards_dict) {
        if (card.second >= 4) {
            vector<int> tmp({card.first, card.first, card.first, card.first});
            bomb_moves.push_back(tmp);
        }
    }
    return bomb_moves;
}

vector<vector<int>> MoveGener::gen_type_5_king_bomb()
{
    if (king_bomb_moves.size() > 0) return king_bomb_moves;

    if (cards_set.find(20) != cards_set.end() && cards_set.find(30) != cards_set.end()) {
        king_bomb_moves.push_back({20, 30});
    }
    return king_bomb_moves;
}

vector<vector<int>> MoveGener::gen_type_6_3_1()
{
    vector<vector<int>> result; 
    if (triple_moves.size() == 0) gen_type_3_triple();  // fill in triple_moves 
    
    for (auto t : triple_moves) {
        for (auto c : cards_set) {
            if (t[0] != c) {
                result.push_back({t[0], t[0], t[0], c});
            }
        }
    }
    return result;
}

vector<vector<int>> MoveGener::gen_type_7_3_2()
{
    vector<vector<int>> result;
    if (triple_moves.size() == 0) gen_type_3_triple(); 
    if (pair_moves.size() == 0) gen_type_2_pair();

    for (auto t : triple_moves) {
        for (auto p : pair_moves) {
            if (t[0] != p[0]) {
                result.push_back({t[0], t[0], t[0], p[0], p[0]});
            }
        }
    }
    return result;
}

vector<vector<int>> MoveGener::gen_type_8_serial_single(int serial_num)
{
    return _gen_serial_moves(cards, MIN_SINGLE, TYPE_SINGLE, serial_num);
}

vector<vector<int>> MoveGener::gen_type_9_serial_pair(int serial_num)
{
    if (serial_pair_moves.size() > 0) return serial_pair_moves;

    vector<int> single_pairs;
    for (auto card : cards_dict) {
        if (card.second >= 2) {
            single_pairs.push_back(card.first); 
        }
    }
    vector<vector<int>> serial_pair_moves = _gen_serial_moves(single_pairs, MIN_PAIRS, TYPE_PAIR, serial_num);
    return serial_pair_moves;
}

vector<vector<int>> MoveGener::gen_type_10_serial_triple(int serial_num)
{
    if (serial_triple_moves.size() > 0) return serial_triple_moves;

    vector<int> single_triples;
    for (auto card : cards_dict) {
        if (card.second >= 3) {
            single_triples.push_back(card.first); 
        }
    }
    serial_triple_moves = _gen_serial_moves(single_triples, MIN_TRIPLES, TYPE_TRIPLE, serial_num);
    return serial_triple_moves;
}

vector<vector<int>> MoveGener::gen_type_11_serial_3_1(int serial_num)
{
    vector<vector<int>> result;
    if (serial_triple_moves.size() == 0) gen_type_10_serial_triple();
    
    for (auto t : serial_triple_moves) {
        set<int> tmp_set(t.begin(), t.end());
        vector<int> rest_cards;
        for (auto card : cards) {
            if (tmp_set.find(card) == tmp_set.end()) {
                rest_cards.push_back(card);
            }
        }
        GetAnyN gan(rest_cards, tmp_set.size());
        vector<vector<int>> single_lists = gan.get_any_n_cards();
        
        for (auto single_cards : single_lists) {
            vector<int> one_result = t;
            one_result.insert(one_result.end(), single_cards.begin(), single_cards.end());
            result.push_back(one_result);
        }
    }
    return result;
}

vector<vector<int>> MoveGener::gen_type_12_serial_3_2(int serial_num)
{
    vector<vector<int>> result;
    if (serial_triple_moves.size() == 0) gen_type_10_serial_triple();
    if (pair_moves.size() == 0) gen_type_2_pair();
    set<int> pair_set;
    for (auto p : pair_moves) {
        pair_set.insert(p[0]);
    }
    for (auto s : serial_triple_moves) {
        set<int> triple_set(s.begin(), s.end());
        set<int> tmp_set = pair_set;
        for (auto card : s) {
            if (tmp_set.find(card) != tmp_set.end()) {
                tmp_set.erase(card);
            }
        }
        vector<int> single_pair_cards(tmp_set.begin(), tmp_set.end());
        GetAnyN gan(single_pair_cards, triple_set.size());
        vector<vector<int>> single_pair_lists = gan.get_any_n_cards();

        for (auto single_pair : single_pair_lists) {
            vector<int> one_result = s;
            for (int i=0; i<2; ++i) {
                one_result.insert(one_result.end(), single_pair.begin(), single_pair.end());
            }
            result.push_back(one_result);
        }
    }
    return result;
}

vector<vector<int>> MoveGener::gen_type_13_4_2()
{
    vector<vector<int>> result;
    if (bomb_moves.size() == 0) gen_type_4_bomb();
    
    vector<vector<int>> all_two_cards;
    if (cards.size() >= 1) {
        for (int i=0; i<cards.size()-1; ++i) {
            for (int j=i+1; j<cards.size(); ++j) {
                all_two_cards.push_back({cards[i], cards[j]});
            }
        }
    }
    
    set<int> duplicated;
    if (all_two_cards.size() >= 1) {
        for (int i=0; i<all_two_cards.size()-1; ++i) {
            for (int j=i+1; j<all_two_cards.size(); ++j) {
                if (all_two_cards[i][0] == all_two_cards[j][0] && \
                    all_two_cards[i][1] == all_two_cards[j][1]) {
                    duplicated.insert(j);
                }
            }
        }
    }
    vector<vector<int>> refined_two_cards;
    for (int i=0; i<all_two_cards.size(); ++i) {
        if (duplicated.find(i) == duplicated.end()) {
            refined_two_cards.push_back(all_two_cards[i]);
        }
    }

    for (auto bomb : bomb_moves) {
        for (auto two_cards : refined_two_cards) {
            if (bomb[0] != two_cards[0] && bomb[0] != two_cards[1]) {
                vector<int> one_result = bomb;
                one_result.insert(one_result.end(), two_cards.begin(), two_cards.end());
                result.push_back(one_result);
            }
        }
    }
    return result;
}

vector<vector<int>> MoveGener::gen_type_14_4_2_2()
{
    vector<vector<int>> result;
    if (bomb_moves.size() == 0) gen_type_4_bomb();
    
    vector<int> two_more_cards;
    for (auto card : cards_dict) {
        if (card.second == 2 || card.second == 3) two_more_cards.push_back(card.first);
    }
    if (two_more_cards.size() < 2) return result;

    GetAnyN gan(two_more_cards, 2);
    vector<vector<int>> two_pairs = gan.get_any_n_cards();

    for (auto bomb : bomb_moves) {
        for (auto two_pair : two_pairs) {
            if (bomb[0] != two_pair[0] && bomb[0] != two_pair[1]) {
                vector<int> one_result = bomb;
                vector<int> tmp({two_pair[0], two_pair[0], two_pair[1], two_pair[1]});
                one_result.insert(one_result.end(), tmp.begin(), tmp.end());
                result.push_back(one_result);
            }
        }
    }
    return result;
}

vector<vector<int>> MoveGener::gen_all_moves()
{
    vector<vector<int>> result;
    vector<vector<int>> tmp;
    tmp = gen_type_1_single();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_2_pair();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_3_triple();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_4_bomb();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_5_king_bomb();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_6_3_1();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_7_3_2();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_8_serial_single();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_9_serial_pair();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_10_serial_triple();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_11_serial_3_1();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_12_serial_3_2();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_13_4_2();
    result.insert(result.end(), tmp.begin(), tmp.end());
    tmp = gen_type_14_4_2_2();
    result.insert(result.end(), tmp.begin(), tmp.end());
    return result;
}

#endif