欢乐斗地主之残局解答器

每天利用一点业余时间来开发；
正在开发过程中，争取每天更新......


# TODO:
1. 完成gen_type_12_serial_3_2()
2. 给定招法，进行类型判断
3. 完成框架：即打印每轮双方的牌以及出招
4. 其他，如蒙特卡洛推演


# 1. 招法分类 + 应招判断

class MoveClassifier

type_1_single           <- self, type_4_bomb, type_5_king_bomb
type_2_pair             <- self, type_4_bomb, type_5_king_bomb
type_3_triple           <- self, type_4_bomb, type_5_king_bomb
type_4_bomb             <-       type_4_bomb, type_5_king_bomb
type_5_king_bomb        <- None
type_6_3_1              <- self, type_4_bomb, type_5_king_bomb
type_7_3_2              <- self, type_4_bomb, type_5_king_bomb
type_8_serial_single    <- self, type_4_bomb, type_5_king_bomb
type_9_serial_pair      <- self, type_4_bomb, type_5_king_bomb
type_10_serial_triple   <- self, type_4_bomb, type_5_king_bomb
type_11_serial_3_1      <- self, type_4_bomb, type_5_king_bomb
type_12_serial_3_2      <- self, type_4_bomb, type_5_king_bomb
type_13_4_2             <- self,              type_5_king_bomb
type_14_4_4             <- self,              type_5_king_bomb

# 2. 招法生成

class MoveGener

# 3. 局面表示

class Situation

-----------------------------------------------------------------------------

S1 
S21, S22, ..., S2n2 
S31, S32, ..., S3n3
Sk1, Sk2, ..., Sknk

S1 + m1 = S21; S1+m2 = S22; ... S1 + mn = S2n
...
Sknx = [a is empty or b is empty] => a win or b win

找出胜率最高的move
