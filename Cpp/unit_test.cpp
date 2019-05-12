#include "utils.hpp"
#include "MoveGener.hpp"
#include "MoveClassifier.hpp"
#include "MoveFilter.hpp"
#include "MovePlayer.hpp"
#include "MinMax.hpp"

int all_cases = 0;
int failed_cases = 0;
int success_cases = 0;

#define TEST_START {cout << "\n----- Test Start:  " << __FUNCTION__ << " ------\n"; all_cases ++;}
#define TEST_PASS  {cout << "Test Passed: " << __FUNCTION__ << endl; success_cases ++; }
#define TEST_FAIL  {cout << "Test Failed: " << __FUNCTION__ << endl; failed_cases ++; }
#define TEST_SUMMARY {cout << "Total test cases: " << all_cases << endl; \
                      cout << "Sucessful test cases: " << success_cases << endl; \
                      cout << "Failed test cases: " << failed_cases << endl; }

string c = "3 3 3 3 4 4 4 5 5 6 6 7 7 8 8 9 9 10 J Q K K A A A 大王 小王";

void test_s2v_v2s() 
{
    TEST_START
    for (auto i : s2v) {
        cout << i.first <<": " << i.second << endl;
    }
    cout << "----------\n";
    for (auto i : v2s) {
        cout << i.first <<": " << i.second << endl;
    }
    TEST_PASS 
}

void test_validate_cards()
{
    TEST_START
    string cards("3 4 5 6");
    bool result = validate_cards(cards);
    if (result) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_get_cards_from_input()
{
    TEST_START
    string input = "3 3 3 4 4 4 5 7 5 7 8 9 10 10 9 8 大王 小王";
    cout << input << endl;
    vector<string> cards = get_cards_from_input(input);
    for (auto c : cards) cout << c <<" "; cout << endl;
    TEST_PASS
}

void test_format_input_cards()
{
    TEST_START
    vector<string> cards({"3", "4", "5", "6", "7", "8", "9", "10", "10", "K"});
    vector<int> vec_cards = format_input_cards(cards);
    print_vector(vec_cards);
    TEST_PASS
}

void test_format_output_cards()
{
    TEST_START
    vector<int> cards({5, 4, 3, 2, 20, 30, 18});
    vector<string> vec_cards = format_output_cards(cards);
    print_vector(vec_cards);
    TEST_PASS
}

void test_remove_cards()
{
    TEST_START
    vector<int> cards({1, 3, 3, 4, 5, 5, 6, 7, 7});
    vector<int> move({3, 7, 5});
    print_vector(cards);
    remove_cards(cards, move);
    print_vector(cards);  // 1 3 4 5 6 7
    TEST_PASS
}

void test_get_n_of_m()
{
    TEST_START
    // vector<int> array({10, 20, 30, 40, 50});
    vector<int> array({3, 3, 5, 1, 5});
    sort(array.begin(), array.end());
    print_vector(array);
    
    GetAnyN gan(array, 2);
    vector<vector<int>> result = gan.get_any_n_cards();
    print_2d_vector(result);
    TEST_PASS
}

void test_gen_type_1_single(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_1_single();
    print_2d_vector(result);
    if (result.size() == 14) { 
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_2_pair(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_2_pair();
    print_2d_vector(result);
    if (result.size() == 9) { 
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_3_triple(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_3_triple();
    print_2d_vector(result);
    if (result.size() == 3) { 
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_4_bomb(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_4_bomb();
    print_2d_vector(result);
    if (result.size() == 1) { 
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_5_king_bomb(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_5_king_bomb();
    print_2d_vector(result);
    if (result.size() == 1) { 
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_6_3_1(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_6_3_1();
    print_2d_vector(result);
    if (result.size() == 39) { 
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_7_3_2(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_7_3_2();
    print_2d_vector(result);
    if (result.size() == 24) { 
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_8_serial_single(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_8_serial_single();
    print_2d_vector(result);
    if (result.size() == 36) { 
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_9_serial_pair(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_9_serial_pair();
    print_2d_vector(result);
    if (result.size() == 15) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_10_serial_triple(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_10_serial_triple();
    print_2d_vector(result);
    if (result.size() == 1) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_11_serial_3_1(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_11_serial_3_1();
    print_2d_vector(result);
    if (result.size() == 73) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_12_serial_3_2(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_12_serial_3_2();
    print_2d_vector(result);
    if (result.size() == 21) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_13_4_2(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_13_4_2();
    print_2d_vector(result);
    if (result.size() == 86) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_type_14_4_2_2(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> result = mg.gen_type_14_4_2_2();
    print_2d_vector(result);
    if (result.size() == 28) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_gen_all_moves(const vector<int>& input)
{
    TEST_START
    print_vector(input);
    MoveGener mg(input);
    vector<vector<int>> all_moves = mg.gen_all_moves();
    print_2d_vector(all_moves);
    if (all_moves.size() == 351) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_MoveClassifier()
{
    TEST_START
    vector<vector<int>> moves = {
        {},
        {20},
        {3, 3},
        {20, 30},
        {4, 4, 4},
        {5, 5, 5, 2},
        {3, 3, 3, 5},
        {6, 3, 4, 5},
        {6, 6, 6, 6},
        {7, 7, 7, 8, 8},
        {9, 9, 10, 10, 10},
        {3, 4, 5, 6, 7},
        {3, 4, 5, 6, 8},
        {2, 2, 4, 5, 6},
        {3, 4, 5, 6, 7, 8, 9},
        {3, 3, 3, 3, 5, 6},
        {3, 3, 3, 3, 5, 6, 7},
        {4, 4, 4, 4, 5, 5, 7, 7},
        {4, 4, 4, 4, 5, 5, 7, 6},
        {4, 4, 4, 4, 5, 5, 6, 6, 7, 7},
        {5, 5, 5, 6, 6, 6, 7, 8},
        {5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 10},
        {5, 5, 5, 6, 6, 6, 7, 7, 9, 9},
        {5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 10, 10, 13, 13},
        {5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 10, 10, 13, 13, 14}
    };

    int count = 0;
    for (auto move : moves) {
        count += 1;
        pair<int, int> move_type = get_move_type(move);
        cout << count << ": The type of ["; 
        for (auto card : move) cout << card << " ";
        cout << "] is " << MOVE_TYPES_STR[move_type.first] <<endl;
    }
    TEST_PASS
}

void test_filter_type_6_3_1()
{
    TEST_START
    vector<vector<int>> moves = {
        {3, 3, 3, 20},
        {4, 4, 4, 8},
        {5, 5, 5, 9},
        {6, 6, 6, 10}
    };
    vector<int> rival_move = {4, 4, 4, 3};

    vector<vector<int>> filtered_moves = filter_type_6_3_1(moves, rival_move);
    cout << "Filtered moves: \n"; 
    print_2d_vector(filtered_moves);
    if (filtered_moves.size() == 2) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_filter_type_7_3_2()
{
    TEST_START
    vector<vector<int>> moves = {
        {3, 3, 3, 7, 8},
        {4, 4, 4, 8, 8},
        {5, 5, 5, 9, 9},
        {6, 6, 6, 10, 10}
    };
    vector<int> rival_move = {4, 4, 4, 3, 3};

    vector<vector<int>> filtered_moves = filter_type_7_3_2(moves, rival_move);
    cout << "Filtered moves: \n"; 
    print_2d_vector(filtered_moves);
    if (filtered_moves.size() == 2) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_filter_type_8_serial_single()
{
    TEST_START
    vector<vector<int>> moves = {
        {3, 4, 5, 6, 7, 8},
        {4, 5, 6, 7, 8, 9},
        {5, 6, 7, 8, 9, 10}
    };
    vector<int> rival_move = {4, 5, 6, 7, 8, 9};

    vector<vector<int>> filtered_moves = filter_type_8_serial_single(moves, rival_move);
    cout << "Filtered moves: \n"; 
    print_2d_vector(filtered_moves);
    if (filtered_moves.size() == 1) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_filter_type_9_serial_pair()
{
    TEST_START
    vector<vector<int>> moves = {
        {3, 3, 4, 4, 5, 5},
        {4, 4, 5, 5, 6, 6},
        {7, 7, 8, 8, 9, 9}
    };
    vector<int> rival_move = {4, 4, 5, 5, 6, 6};

    vector<vector<int>> filtered_moves = filter_type_9_serial_pair(moves, rival_move);
    cout << "Filtered moves: \n"; 
    print_2d_vector(filtered_moves);
    if (filtered_moves.size() == 1) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_filter_type_10_serial_triple()
{
    TEST_START
    vector<vector<int>> moves = {
        {3, 3, 3, 4, 4, 4, 5, 5, 5},
        {4, 4, 4, 5, 5, 5, 6, 6, 6},
        {7, 7, 7, 8, 8, 8, 9, 9, 9}
    };
    vector<int> rival_move = {4, 4, 4, 5, 5, 5, 6, 6, 6};

    vector<vector<int>> filtered_moves = filter_type_10_serial_triple(moves, rival_move);
    cout << "Filtered moves: \n"; 
    print_2d_vector(filtered_moves);
    if (filtered_moves.size() == 1) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_filter_type_11_serial_3_1(){
    TEST_START
    vector<vector<int>> moves = {
        {3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8},
        {5, 5, 8, 9, 5, 6, 6, 6, 7, 7, 7, 10},
        {7, 7, 7, 3, 4, 5, 8, 8, 8, 9, 9, 9}
    };
    vector<int> rival_move = {6, 6, 6, 7, 7, 5, 7, 8, 8, 8, 3, 4};

    vector<vector<int>> filtered_moves = filter_type_11_serial_3_1(moves, rival_move);
    print_2d_vector(filtered_moves);
    if (filtered_moves.size() == 1) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_filter_type_12_serial_3_2(){
    TEST_START
    vector<vector<int>> moves = {
        {3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8},
        {5, 5, 8, 8, 9, 9, 5, 6, 6, 6, 7, 7, 7, 10, 10},
        {7, 7, 7, 3, 3, 4, 4, 5, 5, 8, 8, 8, 9, 9, 9}
    };
    vector<int> rival_move = {6, 6, 6, 7, 7, 5, 5, 7, 8, 8, 8, 3, 3, 4, 4};

    vector<vector<int>> filtered_moves = filter_type_12_serial_3_2(moves, rival_move);
    print_2d_vector(filtered_moves);
    if (filtered_moves.size() == 1) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_filter_type_13_4_2(){
    TEST_START
    vector<vector<int>> moves = {
        {3, 3, 3, 3, 7, 8},
        {5, 5, 5, 5, 10, 10},
        {9, 9, 9, 9, 3, 3}
    };
    vector<int> rival_move = {6, 6, 6, 6, 9, 10};

    vector<vector<int>> filtered_moves = filter_type_13_4_2(moves, rival_move);
    print_2d_vector(filtered_moves);
    if (filtered_moves.size() == 1) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_filter_type_14_4_2_2(){
    TEST_START
    vector<vector<int>> moves = {
        {3, 3, 3, 3, 7, 7, 8, 8},
        {5, 5, 5, 5, 10, 10, 11, 11},
        {9, 9, 9, 9, 3, 3, 4, 4}
    };
    vector<int> rival_move = {4, 4, 4, 4, 3, 3, 5, 5};

    vector<vector<int>> filtered_moves = filter_type_13_4_2(moves, rival_move);
    print_2d_vector(filtered_moves);
    if (filtered_moves.size() == 2) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_get_rest_cards()
{
    TEST_START
    vector<int> cards({3, 4, 4, 5, 5, 5, 6, 6});
    vector<int> move({4, 4, 5, 6, 6, 5});
    vector<int> rest = get_rest_cards(cards, move);
    print_vector(rest);
    TEST_PASS
}

void test_get_proper_moves()
{
    // TODO: Fix the bug here
    TEST_START
    vector<int> cards({3, 20});
    vector<int> rival_move({3});

    vector<vector<int>> proper_moves = get_proper_moves(cards, rival_move);
    print_2d_vector(proper_moves);
    if (proper_moves.size() == 2) {
        TEST_PASS
    }
    else {
        TEST_FAIL
    }
}

void test_min_max_search()
{
    TEST_START
    vector<int> lorder_cards({30, 20, 13, 10, 10, 7, 8, 8, 6, 6});
    vector<int> farmer_cards({18, 18, 14, 14, 14, 9, 9, 7, 6, 6, 3, 3});
    vector<int> last_move({});
    print_min_max_call(farmer_cards, lorder_cards, last_move, LORDER);
    long node_count = 0;
    returned_result result = min_max_search(farmer_cards, lorder_cards,
                                            last_move, LORDER, node_count);
    cout << "score = " << result.score << endl;
    cout << "move is: ";
    print_vector(result.best_move);
    TEST_PASS
}


int main()
{
    test_s2v_v2s();
    test_validate_cards();
    test_get_cards_from_input();
    test_format_input_cards();
    test_format_output_cards();
    test_remove_cards();
    test_get_n_of_m();

    vector<int> input = format_input_cards(get_cards_from_input(c));
    test_gen_type_1_single(input);
    test_gen_type_2_pair(input);
    test_gen_type_3_triple(input);
    test_gen_type_4_bomb(input);
    test_gen_type_5_king_bomb(input);
    test_gen_type_6_3_1(input);
    test_gen_type_7_3_2(input);
    test_gen_type_8_serial_single(input);
    test_gen_type_9_serial_pair(input);
    test_gen_type_10_serial_triple(input);
    test_gen_type_11_serial_3_1(input);
    test_gen_type_12_serial_3_2(input);
    test_gen_type_13_4_2(input);
    test_gen_type_14_4_2_2(input);
    test_gen_all_moves(input);
    
    test_MoveClassifier();
    test_filter_type_6_3_1();
    test_filter_type_7_3_2();
    test_filter_type_8_serial_single();
    test_filter_type_9_serial_pair();
    test_filter_type_10_serial_triple();
    test_filter_type_11_serial_3_1();
    test_filter_type_12_serial_3_2();
    test_filter_type_13_4_2();
    test_filter_type_14_4_2_2();

    test_get_rest_cards();
    test_get_proper_moves();

    test_min_max_search();

    TEST_SUMMARY 
    return 0;
}
