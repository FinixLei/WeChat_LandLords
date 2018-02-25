from common import s2v, v2s, format_input
from move_gener import MovesGener
import move_classifier


def main():
    # Test MoveGener
    a = [3,3,3, 4,4,4, 6,7,8,9,10, 10, 'K']
    b = [6,7,8,9,10, 'J', 'J', 'Q', 'Q', 'Q', 'Y']
    c = [3,3,3,3, 4,4,4, 5,5, 6,6, 7,7, 8,8, 9,9, 10, 11, 12, 13, 13, 13, 14, 14, 14, 'Y', 'Z']

    print(format_input(c))
    mg = MovesGener(format_input(c))
    moves = mg.gen_moves()
    # print(moves)
    print(len(moves))

    # Test MoveClassifier 
    moves = [
        [], 
        [20],
        [3, 3],
        [20, 30],
        [4, 4, 4],
        [5, 5, 5, 2], 
        [2, 2, 2, 5],
        [2, 3, 4, 5],
        [6, 6, 6, 6], 
        [7, 7, 7, 8, 8], 
        [9, 9, 10, 10, 10], 
        [3, 4, 5, 6, 7], 
        [3, 4, 5, 6, 8], 
        [2, 2, 4, 5, 6]
    ]
    
    mc = move_classifier.MoveClassifier()
    count = 0
    for move in moves:
        count += 1
        move_type = mc.get_move_type(move)
        print("%d: The type of %s is %s" %
              (count,
               move,
               move_classifier.MOVE_TYPES_STR.get(move_type, "Wrong")))

    # Test Framework
    

main()
