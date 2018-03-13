欢乐斗地主之残局解答器

这个项目终于完成了！
一共实现了2个引擎：蒙特卡洛引擎（分为单进程和多进程2个版本）和传统的Min-Max引擎（多进程版）。
实测中发现：
1. 蒙特卡洛引擎并不准确，某些题的正确答案所得到的概率并不是最高的。这大概也是很多围棋AI的死活有问题的根本原因。
2. Min-Max引擎非常之快，而且完全正确。当然，这是针对扑克牌变化相对较少而言（比如农民出对地主也只能出对和炸弹）。

最终的solution还是使用了Min-Max引擎。

--------------------------------------------------------------------------

TODO:
进一步完善UIEngine，更好的服务玩家。

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

8. Min-Max Engine.
   This is the final solution!
