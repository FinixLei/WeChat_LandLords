import copy
from common import get_rest_cards
from move_player import get_possible_moves

PARTY_A = "LandLord"
PARTY_B = "Farmer"


class Situation(object):
    
    def __init__(self, lord_cards=[], farmer_cards=[],
                 previous_move=[], player='farmer'):
        self.lord_cards = copy.deepcopy(lord_cards)
        self.farmer_cards = copy.deepcopy(farmer_cards)
        self.previous_move = copy.deepcopy(previous_move)
        self.player = player
