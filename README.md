欢乐斗地主之残局解答器

**基本的蒙特卡洛搜索已经完成，并辅以多进程（Python不真正支持多线程）搜索，目前基本功能已经完成。**
**使用方法是：直接编辑test_mc_engine_mp.py, 并运行它： python test_mc_engine_mp.py**
**ui_engine并没有实际的效用，不必使用这个文件。**

在test_mc_engine_mp.py中，给出了3个例子，计算机虽然模拟完了所有对局，但是得出了错误的结论。
因此，直接的蒙特卡洛方法是有缺陷的。这也是为什么很多围棋AI，包括第一版的Alpha Go(Alpha Go Lee)都有死活问题。

--------------------------------------------------------------------------
# TODO:  
思考蒙特卡洛算法的缺陷该如何补足，真正的暴力搜索是否可行。

--------------------------------------------------------------------------
# Done

1. Test Framework  
   See test.py

2. UIEngine  
   The draft is done.

3. MoveGener (Move Generator)  
   Generate all the 14 types of moves.
   
4. MoveClassifier (Move type classifier)  
   Give a move, tell which type it belongs to.

5. get_resp_moves(cards, rival_move)  
   Give all the possible moves per cards on hand and the rival's move

6. Basic Monte Carlo search
   Basic function is done.

7. Multi-Process do MC search.
