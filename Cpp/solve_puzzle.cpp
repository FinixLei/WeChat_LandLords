#include "utils.hpp"
#include "MoveGener.hpp"
#include "MoveClassifier.hpp"
#include "MoveFilter.hpp"
#include "MovePlayer.hpp"
#include "MinMax.hpp"

extern pthread_mutex_t mutex;

void declare()
{
    cout << "---------------------------\n"; 
    cout << "可输入的命令：" << endl; 
    cout << "pass - 过" << endl;
    cout << "quit - 退出程序" << endl;
    cout << "---------------------------\n"; 
}

void choose_engine()
{
    cout << "请选择计算引擎：（默认使用多线程引擎)" << endl;
    cout << "多线程引擎(输入M) v.s. 单线程引擎(输入S)" << endl;
    cout << "请选择（M or S): "; 

    const int buf_size = 10;
    char screen_buf[buf_size];
    cin.getline(screen_buf, buf_size);
    string answer = string(screen_buf);
    if (answer[0] == 'S' || answer[0] == 's') {
        ENGINE_TYPE = SINGLE_THREAD_ENGINE;
    }
    else {
        ENGINE_TYPE = MULTI_THREAD_ENGINE;
    }
    string engine = (ENGINE_TYPE==MULTI_THREAD_ENGINE)?string("多线程引擎"):string("单线程引擎") ;
    cout << "引擎类型: " << engine << endl;
    cout << "---------------------------\n";
    cin.clear();
}

int main()
{
    declare();
    choose_engine();

    const int buf_size = 1000;
    char screen_buf[buf_size];
    pthread_mutex_init (&mutex,NULL);

    // Quick Test Case
    // string str_lorder_cards = "2 K 9 8 7 7 6 6 5 4";
    // string str_farmer_cards = "大王 2 A Q J J 9 6 4";

    // Slow Test Case
    // string str_lorder_cards = "小王 大王 K 10 10 7 8 8 6 6";
    // string str_farmer_cards = "2 2 A A A 9 9 7 6 6 3 3";

    // Standard Case
    string str_lorder_cards = "";
    string str_farmer_cards = "";

    if (str_lorder_cards == "" && str_farmer_cards == "") {
        cout << "请输入地主的牌：(以空格间隔)" << endl;
        cin.getline(screen_buf, buf_size);
        str_lorder_cards = string(screen_buf);
        bool valid_cards = validate_cards(str_lorder_cards);
        while (!valid_cards) {
            cout << "输入错误，请重新输入地主的牌：(以空格间隔)" << endl;
            cin.getline(screen_buf, buf_size);
            str_lorder_cards = string(screen_buf);
            valid_cards = validate_cards(str_lorder_cards);
        }

        cout << "请输入农民的牌：(以空格间隔)" << endl;
        cin.getline(screen_buf, buf_size);
        str_farmer_cards = string(screen_buf);
        valid_cards = validate_cards(str_farmer_cards);
        while (!valid_cards) {
            cout << "输入错误，请重新输入农民的牌：(以空格间隔)" << endl;
            cin.getline(screen_buf, buf_size);
            str_farmer_cards = string(screen_buf);
            valid_cards = validate_cards(str_farmer_cards);
        }
    }

    vector<int> lorder_cards = format_input_cards(get_cards_from_input(str_lorder_cards));
    vector<int> farmer_cards = format_input_cards(get_cards_from_input(str_farmer_cards));
    vector<int> last_move({});  

    cout << "初始状态: "  << endl;
    cout << "地主家的牌:"; print_vector(format_output_cards(lorder_cards)); 
    cout << "农民家的牌:"; print_vector(format_output_cards(farmer_cards));
    cout << "当前出牌者:" << "地主" << endl;
    cout << "---------------------------" << endl;
    
    vector<int> lorder_move, farmer_move;
    int score = 0;
    pair<int, vector<int>> result = start_engine(farmer_cards, lorder_cards, last_move, LORDER);
    score = result.first;
    lorder_move = result.second;

    if (score == MIN_SCORE) {
        cout << "地主必败" << endl;
        return 0;
    }

    lorder_cards = get_rest_cards(lorder_cards, lorder_move);
    if (lorder_cards.size() == 0) {
        cout << "地主出牌: "; print_vector(format_output_cards(lorder_move));
        cout << "地主胜利!" << endl;
        return 0;
    }

    // Farmer and LandLorder play one by one
    vector<string> str_lorder_move, str_farmer_move;
    vector<vector<int>> proper_moves;

    while (true) {
        // Print the Situation after Lorder play a move
        if (lorder_move.size() > 0) {
            str_lorder_move = format_output_cards(lorder_move);
        }
        else {
            str_lorder_move = {string("Pass!")};
        }

        cout << "地主家的牌: "; print_vector(format_output_cards(lorder_cards));
        cout << "农民家的牌: "; print_vector(format_output_cards(farmer_cards));
        cout << "地主已出牌: "; print_vector(str_lorder_move);
        cout << "---------------------------" << endl;

        // Farmer plays a move
        cout << "请帮农民出牌:" << endl;
        cin.getline(screen_buf, buf_size);
        string input_farmer_move = string(screen_buf);

        str_farmer_move = get_cards_from_input(input_farmer_move); 
        if (str_farmer_move.size() == 0 || 
            str_farmer_move[0] == "pass" || str_farmer_move[0] == "Pass" ) {
            farmer_move = {};
        }
        else if (str_farmer_move[0] == "quit") {
            exit(0);
        }
        else {
            farmer_move = format_input_cards(str_farmer_move);
        }

        proper_moves = get_proper_moves(farmer_cards, lorder_move);

        // check if farmer_move exists in proper_moves
        bool farmer_move_exists = false;
        if (farmer_move.size() == 0) {  // pass move
            farmer_move_exists = true;
        }
        else {
            sort(farmer_move.begin(), farmer_move.end());
            for (auto move : proper_moves) {
                if (move.size() != farmer_move.size()) continue;
                sort(move.begin(), move.end());
                bool all_same = true;
                for (int i=0; i<move.size(); ++i) {
                    if (farmer_move[i] != move[i]) {
                        all_same = false;
                        break;
                    }
                }
                if (all_same == true) farmer_move_exists = true;
            }
        }

        while (farmer_move_exists == false) {
            cout << "出牌错误。请重新帮农民出牌:" << endl;
            cin.getline(screen_buf, buf_size);
            input_farmer_move = string(screen_buf);
            str_farmer_move = get_cards_from_input(input_farmer_move); 
            if (str_farmer_move.size() == 0 || 
                str_farmer_move[0] == "pass" || str_farmer_move[0] == "Pass") {
                farmer_move = {};
            }
            else if (str_farmer_move[0] == "quit") {
                exit(0);
            }
            else {
                farmer_move = format_input_cards(str_farmer_move);
            }

            proper_moves = get_proper_moves(farmer_cards, lorder_move);

            // check if farmer_move exists in proper_moves
            farmer_move_exists = false;
            if (farmer_move.size() == 0) {  // pass move
                farmer_move_exists = true;
            }
            else {
                sort(farmer_move.begin(), farmer_move.end());
                for (auto move : proper_moves) {
                    if (move.size() != farmer_move.size()) continue;
                    sort(move.begin(), move.end());
                    bool all_same = true;
                    for (int i=0; i<move.size(); ++i) {
                        if (farmer_move[i] != move[i]) {
                            all_same = false;
                            break;
                        }
                    }
                    if (all_same) farmer_move_exists = true;
                }
            }
        }

        farmer_cards = get_rest_cards(farmer_cards, farmer_move);
        if (farmer_cards.size() == 0) {
            cout << "农民出牌: "; print_vector(format_output_cards(farmer_move));
            cout << "农民胜利！" << endl;
            return 0;
        }

        if (farmer_move.size() > 0) {
            str_farmer_move = format_output_cards(farmer_move);
        }
        else {
            str_farmer_move = {"Pass!"};
        }
        cout << "地主家的牌: "; print_vector(format_output_cards(lorder_cards));
        cout << "农民家的牌: "; print_vector(format_output_cards(farmer_cards));
        cout << "农民已出牌: "; print_vector(str_farmer_move);
        cout << "---------------------------" << endl;

        // LandLorder plays a move
        find_best_move = false;  // recovery this global variable
        best_move = {};
        result = start_engine(farmer_cards, lorder_cards, farmer_move, LORDER);
        score = result.first;
        lorder_move = result.second;

        if (score == MIN_SCORE) {
            cout << "地主必败！" << endl;
            return 0;
        }

        lorder_cards = get_rest_cards(lorder_cards, lorder_move);
        if (lorder_cards.size() == 0) {
            cout << "地主出牌: "; print_vector(format_output_cards(lorder_move));
            cout << "地主胜利！" << endl;
            return 0;
        }
    }

    return 0;
}
