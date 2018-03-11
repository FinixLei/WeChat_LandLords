欢乐斗地主之残局解答器

**基本的蒙特卡洛搜索已经完成，但效率较低，还有很大的优化空间。**
**因为工作和学习繁忙，作者将暂停或以较低频率更新本项目。**
                          -- Finix 2018.03.11

--------------------------------------------------------------------------
# TODO:  
1. 进一步剪枝优化蒙特卡洛搜索(mc_engine)

2. 多线程/多进程实现mc_engine（虽然Python不支持真正的多线程，但可以试一下）

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