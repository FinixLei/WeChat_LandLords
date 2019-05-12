#ifndef MINMAX_HPP
#define MINMAX_HPP

#include <pthread.h>
#include <ctime>

#include "utils.hpp"
#include "MoveGener.hpp"
#include "MoveFilter.hpp"
#include "MovePlayer.hpp"

extern pthread_mutex_t mutex;

struct thread_parameters {
    vector<int> farmer_cards;
    vector<int> lorder_cards;
    vector<int> last_move;
    int current_player;
};

bool find_best_move = false;
vector<int> best_move({});

const int MIN_SCORE = 0;
const int MAX_SCORE = 999;

// Players: FARMER is always the computer side. 
const int FARMER = 0;
const int LORDER = 1;

// returned item
struct returned_result {
    int score;
    vector<int> best_move;
};

static void print_min_max_call(const vector<int>& farmer_cards, 
                               const vector<int> lorder_cards, 
                               const vector<int>& last_move, 
                               int current_player) 
{
    #ifdef DEBUG

    cout << "Farmer Cards: ";
    print_vector(farmer_cards);
    cout << "Lorder Cards: ";
    print_vector(lorder_cards);


    if (current_player == LORDER) {
        cout << "Farmer plays: ";
    }
    else {
        cout << "Lorder plays: ";
    }
    
    if (last_move.size() == 0) {
        cout << "Pass\n";
    }
    else {
        print_vector(last_move);
    }
    cout << "-----------------------------\n";

    #endif
}

// Check how many nodes are calculated
// node_count - how many nodes are calculated
// last_check - whether this is the last time of checking 
void check_status (long& node_count, bool last_check=false)
{
    if (last_check) {  // this is the last time of checking
        cout << node_count << " nodes have been calculated...\n";
    }
    else {  // this is a normal checking
        if (node_count % 30000 == 0) {
            cout << node_count << " nodes have been calculated...\n";
        }
        pthread_mutex_lock(&mutex);
        if (find_best_move) {
            pthread_mutex_unlock(&mutex); // unlock before exit
            pthread_exit(NULL); 
        }
        pthread_mutex_unlock(&mutex);
    }
}

// Return - score
// If current_player is LORDER, MAX_SCORE is requrired. When MAX_SCORE is 
// found, then the search can be cut and return MAX_SCORE; 
// If all the moves cannot get MAX_SCORE, return MIN_SCORE;
// If current_player is FARMER, MIN_SCORE is required. When MIN_SCORE is found, 
// then the search can be cut and return MIN_SCORE;
// If all the moves cannot get MIN_SCORE, return MAX_SCORE;
// 
// farmer_cards   - In current position, cards on farmer's side;
// lorder_cards   - In current position, cards on lorder's side;
// last_move      - If current_player is LORDER, last_move is from FARMER; vice versa;
// current_player - The one will make the move right now
// node_count     - how many nodes are calculated
returned_result min_max_search(vector<int> farmer_cards, 
                               vector<int> lorder_cards,
                               vector<int> last_move, 
                               int current_player,
                               long& node_count)
{
    if (current_player == LORDER && farmer_cards.size() == 0) {
        ++ node_count;
        check_status(node_count);
        return {MIN_SCORE, {}};
    }
    if (current_player == FARMER && lorder_cards.size() == 0) {
        ++ node_count;
        check_status(node_count);
        return {MAX_SCORE, {}};
    }

    if (current_player == LORDER) {
        vector<vector<int>> proper_moves = get_proper_moves(lorder_cards, last_move);
        // cout << "Proper Moves for LORDER: \n";
        // print_2d_vector(proper_moves);
        // cout << "==========\n";

        for (auto move : proper_moves) {
            vector<int> lorder_current_cards = get_rest_cards(lorder_cards, move);
            print_min_max_call(farmer_cards, lorder_current_cards, move, FARMER);
            returned_result result = min_max_search(farmer_cards, 
                                                    lorder_current_cards,
                                                    move, 
                                                    FARMER, 
                                                    node_count);

            if (result.score == MAX_SCORE) {
                return {MAX_SCORE, move};
            }
        }
        return {MIN_SCORE, {}};
    }
    else { // current_player == FARMER
        vector<vector<int>> proper_moves = get_proper_moves(farmer_cards, last_move);
        for (auto move : proper_moves) {
            vector<int> farmer_current_cards = get_rest_cards(farmer_cards, move);
            print_min_max_call(farmer_current_cards, lorder_cards, move, LORDER);
            returned_result result = min_max_search(farmer_current_cards, 
                                                    lorder_cards,
                                                    move, LORDER, 
                                                    node_count);
            if (result.score == MIN_SCORE) {
                return {MIN_SCORE, move};
            }
        }
        return {MAX_SCORE, {}};
    }
}

// current_player - LORDER or FARMER
void* thread_func(void * args)
{
    thread_parameters *parameters = (thread_parameters *)(args);
    vector<int> farmer_cards = parameters->farmer_cards;
    vector<int> lorder_cards = parameters->lorder_cards;
    vector<int> last_move    = parameters->last_move;
    int current_player       = parameters->current_player;

    long node_count = 0;
    returned_result result = min_max_search(farmer_cards, 
                                            lorder_cards,
                                            last_move, 
                                            current_player, 
                                            node_count);
    bool last_check = true; 
    check_status(node_count, last_check);
    cout << "score = " << result.score << endl;
    cout << "calculated move is: "; print_vector(last_move);
    
    if (result.score == MAX_SCORE) {
        pthread_mutex_lock(&mutex);
        find_best_move = true;
        best_move = last_move;
        cout << "Best move is "; print_vector(best_move);
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

pair<int, vector<int>> start_engine(vector<int> farmer_cards, 
                                    vector<int> lorder_cards,
                                    vector<int> last_move,
                                    int current_player)
{
    clock_t start, end;
    start = clock();
    
    if (ENGINE_TYPE == MULTI_THREAD_ENGINE) {
        vector<pthread_t *> ptids;
        vector<vector<int>> proper_moves = get_proper_moves(lorder_cards, last_move);
        for (auto move : proper_moves) {
            vector<int> rest_lorder_cards =get_rest_cards(lorder_cards, move);
            struct thread_parameters thp({
                farmer_cards, rest_lorder_cards, move, FARMER
            });

            pthread_t *ptid = new pthread_t;
            ptids.push_back(ptid); // record in vector for future deletion
            pthread_create(ptid, NULL, thread_func, (void *)&thp);
            int result = pthread_join(*ptid, NULL);
            if (result != 0) {
                cout << "Failed to create thread for move "; 
                print_vector(move);
            }
        }

        for (auto ptid : ptids) delete ptid;
        
    }
    else {  // Single Thread Engine
        long node_count = 0;
        returned_result result = min_max_search(farmer_cards, 
                                                lorder_cards,
                                                last_move, 
                                                LORDER, 
                                                node_count);
        bool last_check = true; 
        check_status(node_count, last_check);
        cout << "score = " << result.score << endl;
        cout << "calculated move is: "; print_vector(result.best_move);
        
        if (result.score == MAX_SCORE) {
            find_best_move = true;
            best_move = result.best_move;
            cout << "Best move is "; print_vector(best_move);
        }
    }

    end = clock();
    double duration = (double)(end - start) / CLOCKS_PER_SEC;
    cout << "Time cost: " << duration << " seconds\n";
    cout << "---------------------------\n";
    
    if (find_best_move) { return {MAX_SCORE, best_move}; }
    else { return {MIN_SCORE, {}}; }
}


#endif