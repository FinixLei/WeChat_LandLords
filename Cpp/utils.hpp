#ifndef UTILS_HPP_
#define UTILS_HPP_

#include <unistd.h>
#include <pthread.h>

#include <unordered_map>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;


pthread_mutex_t mutex;

const int SINGLE_THREAD_ENGINE = 1;
const int MULTI_THREAD_ENGINE = 9;
int ENGINE_TYPE = MULTI_THREAD_ENGINE;

const int MIN_SINGLE = 5;
const int MIN_PAIRS = 3;
const int MIN_TRIPLES = 2;

const int TYPE_SINGLE = 1;
const int TYPE_PAIR = 2;
const int TYPE_TRIPLE = 3;

template<typename T>
void print_vector(vector<T> vec) {
    for (auto i : vec) {
        std::cout << i << " "; 
    }
    std::cout << std::endl;
}

template<typename T>
void print_2d_vector(vector<vector<T>> vec2d)
{
    for (auto vec : vec2d) {
        print_vector(vec);
    }
    cout << "Total number: " << vec2d.size() << endl;
}

unordered_map<std::string, int> s2v({
    {"3", 3}, {"4", 4}, {"5", 5}, {"6", 6}, {"7", 7}, {"8", 8}, {"9", 9}, {"10", 10}, 
    {"J", 11}, {"j", 11}, {"Q", 12}, {"q", 12}, {"K", 13}, {"k", 13}, 
    {"A", 14}, {"a", 14}, {"2", 18},
    {"Y", 20}, {"y", 20}, {"小王", 20}, 
    {"Z", 30}, {"z", 30}, {"大王", 30}
});

unordered_map<int, std::string> v2s({
    {3, "3"}, {4, "4"}, {5, "5"}, {6, "6"}, {7, "7"}, {8, "8"}, {9, "9"}, {10, "10"}, 
    {11, "J"}, {12, "Q"}, {13, "K"}, {14, "A"}, {18, "2"}, 
    {20, "小王"}, {30, "大王"}
});

vector<int> get_rest_cards(vector<int>& cards, vector<int> move)
{
    list<int> cards_list(cards.begin(), cards.end());
    for (auto card : move) {
        bool findit = false;
        for (auto it = cards_list.begin(); it != cards_list.end(); ++it) {
            if (card == *it) {
                cards_list.erase(it);
                findit = true;
                break;
            }
        }
        if (!findit) throw "move is not subset of cards";
    }
    vector<int> result(cards_list.begin(), cards_list.end());
    return result;
}

vector<string> get_cards_from_input(string& input) 
{
    stringstream ssinput(input);
    string card;
    vector<string> cards;
    while (ssinput >> card) {
        cards.push_back(card);
    }
    return cards;
}

vector<int> format_input_cards(const vector<string>& cards)
{
    const int size = cards.size();
    vector<int> vec_cards(size);
    for (int i=0; i<size; ++i) {
        vec_cards[i] = s2v[cards[i]];
    }
    sort(vec_cards.begin(), vec_cards.end());
    return vec_cards;
}

vector<string> format_output_cards(const vector<int>& cards)
{
    const int size = cards.size();
    vector<string> vec_cards(size);
    for (int i=0; i<size; ++i) {
        vec_cards[i] = v2s[cards[i]];
    }
    sort(vec_cards.begin(), vec_cards.end());
    return vec_cards;
}

bool validate_cards(string& input)
{
    vector<string> cards = get_cards_from_input(input);
    for (auto card : cards) {
        if (s2v.find(card) == s2v.end()) return false;
    }
    return true;
}

void remove_cards(vector<int>& cards, vector<int>& move)
{
    sort(cards.begin(), cards.end());
    sort(move.begin(), move.end());
    auto cit = cards.begin();
    auto mit = move.begin();
    while (cit != cards.end()) {
        if (*cit == *mit) {
            cit = cards.erase(cit);
            mit++;
        }
        else {
            cit ++;
        }
    }
}


class GetAnyN {
public:
    GetAnyN(const vector<int>& array, int n) : array(array), n(n) { m = array.size(); }
    ~GetAnyN(){}
    vector<vector<int>> get_any_n_cards();  // Get any n cards from m cards
    
private:
    GetAnyN(const GetAnyN&) = delete;
    GetAnyN operator=(const GetAnyN&) = delete;
    
    void _list_all_n_of_m(int m, int n, vector<int>& tmp);
    void _remove_duplicated();
    
private: 
    vector<int> array;
    int m;  // m >= n
    int n;
    vector<vector<int>> all_lists;
    vector<vector<int>> final_result;
};


void GetAnyN::_list_all_n_of_m(int m, int n, vector<int>& result)
{
    for (int i=m; i>=n; i--)
    {
        result.push_back(this->array[i-1]);
        if (n > 1)
        {
            _list_all_n_of_m(i-1, n-1, result);
        }
        else
        {
            this->all_lists.push_back(result);
        }
        result.pop_back();
    }
}

void GetAnyN::_remove_duplicated()
{
    vector<int> duplicated; 
    int size = all_lists.size();
    for (int i=0; i<size-1; i++) {
        for (int j=i+1; j<size; j++) {
            bool equal = true;
            for (int k=0; k<n; k++) {
                if (all_lists[i][k] != all_lists[j][k]) {
                    equal = false;
                    break;
                }
            }
            if (equal) duplicated.push_back(j);
        }
    }
    
    vector<int> good_index; 
    for (int i=0; i<size; i++) {
        bool good = true;
        for (auto bad : duplicated) {
            if (i == bad) {
                good = false;
                break;
            }
        }
        if (good) good_index.push_back(i);
    }
    
    for (auto i : good_index) {
        final_result.push_back(all_lists[i]);
    }
}

vector<vector<int>> GetAnyN::get_any_n_cards()
{
    vector<int> tmp;
    _list_all_n_of_m(m, n, tmp);
    _remove_duplicated();
    return final_result;
}

#endif