from itertools import combinations

from hand import Hand
from standard_ranker import StandardRanker


class Holdem:
    def __init__(self, hole_cards, flop, turn, river):
        self.cards = hole_cards + flop + [turn] + [river]

    def best_hand(self):
        if not self.hand:
            for c in combinations(self.cards, 5):
                hand = Hand(StandardRanker(), c)

                if not self.hand:
                    self.hand = hand
                else:
                    self.hand = max(self.hand, hand)