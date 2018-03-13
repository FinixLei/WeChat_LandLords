欢乐斗地主之残局解答器

**蒙特卡洛搜索已经完成，并辅以多进程（Python不真正支持多线程）搜索，目前基本功能已经完成。多进程确实加速了几倍的速度。**
**使用方法：直接编辑test_mc_engine_mp.py, 并运行它： python test_mc_engine_mp.py**

(ui_engine并没有实际的效用，不必使用这个文件。)

在test_mc_engine_mp.py中，给出了3个例子，计算机虽然模拟完了所有对局，但是得出了错误的结论。
因此，直接的蒙特卡洛方法是有缺陷的。这也是为什么很多围棋AI，包括第一版的Alpha Go(Alpha Go Lee)都有死活问题。

--------------------------------------------------------------------------
# TODO:  
普通的蒙特卡洛搜索是有一定的问题。解决方法大致有2种：
1. 优化蒙特卡洛搜索（但是这只能在一定程度上缓解问题，并不能根治问题）
2. MIN-MAX纯暴力搜索（这能从根本上解决问题，但是一般不能在可接受的时间内解决）

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
