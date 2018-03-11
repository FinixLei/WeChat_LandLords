欢乐斗地主之残局解答器

**Since the author is busy on work and learning recently, this project may be suspended for some time or be updated infrequently.**   
**因为工作和学习繁忙，作者将暂停或以较低频率更新本项目。**  
-- Finix 2018.03.05

--------------------------------------------------------------------------
# TODO:  
1. 完善蒙特卡洛树搜索 （80%）

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

--------------------------------------------------------------------------

# MC Tree: 

S1 
S21, S22, ..., S2n2 
S31, S32, ..., S3n3
Sk1, Sk2, ..., Sknk

S1 + m1 = S21; S1+m2 = S22; ... S1 + mn = S2n
...
Sknx = [a is empty or b is empty] => a win or b win
