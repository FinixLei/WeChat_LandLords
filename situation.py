import copy

PARTY_A = "LandOwner"
PARTY_B = "Farmer"


class PartOwner(object):
    def __init__(self, role, cards):
        self.role = role
        if isinstance(cards, list):
            self.cards = cards
        else:
            raise Exception("Failed to initiate PartOwner: "
                            "the 2nd parameter is not a list")


class Situation(object):
    
    def __init__(self, owner_a, owner_b):
        # owner_a is always the first mover
        self.a = owner_a
        self.b = owner_b
        
    def do_move(self, move):
        a = copy.deepcopy(self.a)
        b = copy.deepcopy(self.b)

        for i in move:
            a.cards.remove(i)

        if len(a.cards) == 0:
            # TODO: here may be changed in future
            msg = "%s: %s\n" % (a.role, move)
            msg += "%s Win!" % a.role
            return msg
        else:
            return Situation(b, a)
