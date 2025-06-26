from itertools import combinations

from hand import Hand
from standard_ranker import StandardRanker


class Holdem:
    def __init__(self, hole_cards, flop, turn, river):
        self.cards = hole_cards + flop + [turn] + [river]
        self.hand = []

    def best_hand(self):
        if not self.hand:
            for c in combinations(self.cards, 5):
                hand = Hand(StandardRanker(), c)

                if not self.hand:
                    self.hand = hand
                else:
                    self.hand = max(self.hand, hand)

        return self.hand

    def __lt__(self, other):
        return self.best_hand().hand_score() < other.best_hand().hand_score()

    def __le__(self, other):
        return self.best_hand().hand_score() <= other.best_hand().hand_score()

    def __gt__(self, other):
        return self.best_hand().hand_score() > other.best_hand().hand_score()

    def __ge__(self, other):
        return self.best_hand().hand_score() >= other.best_hand().hand_score()

    def __eq__(self, other):
        return self.best_hand().hand_score() == other.best_hand().hand_score()

    def __ne__(self, other):
        return self.best_hand().hand_score() != other.best_hand().hand_score()
