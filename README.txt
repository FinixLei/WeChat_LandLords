欢乐斗地主之残局解答器

** Since the author is busy on work and learning recently, 
this project may be suspended for some time or be updated infrequently.
   因为工作和学习繁忙，作者将暂停或以较低频率更新本项目。
**
-- Finix 2018.03.05

--------------------------------------------------------------------------
# TODO:
1. 核心部分：蒙特卡洛树搜索

2. Refactor UIEngine with Position Expression.
   结合局面表达，重构UIEngine.
   有了局面自推演，这一部分目前不再重要，优先级降低

--------------------------------------------------------------------------
# Done

1. Test Framework
   See test.py

2. UIEngine
   The draft is done. Need refactoring after MC is done.

3. MoveGener (Move Generator)
   Generate all the 14 types of moves.
   
4. MoveClassifier (Move type classifier)
   Give a move, tell which type it belongs to.

5. get_possible_moves(cards, rival_move)
   Give all the possible moves per cards on hand and the rival's move

--------------------------------------------------------------------------

# MC Tree: 

S1 
S21, S22, ..., S2n2 
S31, S32, ..., S3n3
Sk1, Sk2, ..., Sknk

S1 + m1 = S21; S1+m2 = S22; ... S1 + mn = S2n
...
Sknx = [a is empty or b is empty] => a win or b win

--------------------------------------------------------------------------

# UI Design (need re-design)

可输入命令如下:
quit  - 退出程序
pass  - 过，不出牌
Y - 小王
Z - 大王

---------------------------------

请输入地主的最初牌型:
6 6 2

请输入农民的最初牌型:
3 3 Y

现在轮到农民出牌:
3 3

地主出牌:
6 6

---------------------------------

地主的牌：
2
    
农民的牌：
Y
    
现在轮到农民出牌:
Pass

---------------------------------

地主的牌：
2
    
农民的牌：
Y

地主出牌:
2

地主胜利！
