欢乐斗地主之残局解答器

这个项目终于完成了！
最初实现了2个引擎（都是多进程）：蒙特卡洛引擎和传统的MinMax引擎。其实它们的代码极为类似，
但是因为蒙特卡洛引擎并不准确，概率最高的未必是绝杀的一条路，因此弃用蒙特卡洛引擎，而专注于MinMax引擎。
Min-Max引擎还有另外一个好处，就是非常快，因为可以剪枝；但对于牌类来说，就必须算到牌局终局。

使用方法：

    python solve_puzzle.py

--------------------------------------------------------------------------
# Code Introduction

1. Test Framework  
   See test.py

2. UIEngine

3. MoveGener (Move Generator)  
   Generate all the 14 types of moves.
   
4. MoveClassifier (Move type classifier)  
   Give a move, tell which type it belongs to.

5. get_resp_moves(cards, rival_move)  
   Give all the possible moves per cards on hand and the rival's move

6. Min-Max Engine
