from itertools import combinations

from card_rankings import card_rankings
from hand import Hand
from standard_ranker import StandardRanker


class Holdem:
    def __init__(self, hole_cards, flop, turn, river):
        self.hole_cards = hole_cards
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
    
    def classify(self):
        a, b = self.hole_cards

        if a.raw_rank == b.raw_rank:
            return a.raw_rank*2
        
        greater_rank = a.raw_rank
        smaller_rank = b.raw_rank

        if card_rankings[greater_rank] < card_rankings[smaller_rank]:
            greater_rank, smaller_rank = smaller_rank, greater_rank
        
        if a.suit == b.suit:
            return greater_rank + smaller_rank + 's'
        
        return greater_rank + smaller_rank + 'o'

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
