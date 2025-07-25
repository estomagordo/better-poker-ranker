from itertools import combinations

from black_jack_ranker import BlackJackRanker
from card_rankings import card_rankings
from hand import Hand
from standard_ranker import StandardRanker


class Omajack:
    def __init__(self, hole_cards, flop, turn, river):
        self.hole_cards = hole_cards
        self.cards = hole_cards + flop + [turn] + [river]
        self.community_cards = flop + [turn] + [river]
        self.hand = []
        self.black_jack_possibilities = []

    def best_hand(self):
        if not self.hand:
            omaha_indices = [-1, -1]
            best_omaha = Hand(StandardRanker(), [])

            for c in combinations(range(len(self.hole_cards)), 2):
                playing = [self.hole_cards[i] for i in c]

                for d in combinations(self.community_cards, 3):
                    omaha = Hand(StandardRanker(), list(d) + playing)

                    if omaha > best_omaha:
                        best_omaha = omaha
                        omaha_indices = list(c)

            black_jack_indices = [i for i in range(len(self.hole_cards)) if i not in omaha_indices]
            black_jack_hand = Hand(BlackJackRanker(), [self.hole_cards[i] for i in black_jack_indices])

            self.hand = [best_omaha, black_jack_hand]

        return self.hand
    
    def rank_classify(self):
        return ''.join([card.raw_rank for card in sorted([card for card in self.hole_cards], key=lambda card: -card_rankings[card.raw_rank])])
    
    def nuanced_classify(self):
        reverse_ranked = sorted([card for card in self.hole_cards], key=lambda card: -card_rankings[card.raw_rank])
        suits_seen = {}
        out = []

        for card in reverse_ranked:
            if card.suit not in suits_seen:
                suits_seen[card.suit] = chr(ord('a')+len(suits_seen))
            out.append(f'{card.raw_rank}{suits_seen[card.suit]}')

        return ''.join(out)
    
    def all_black_jack_possibilities(self):
        if not self.black_jack_possibilities:
            poss = set()

            for c in combinations(self.hole_cards, 3):
                poss.add(Hand(BlackJackRanker(), c).hand_score())

            self.black_jack_possibilities = sorted(poss)

        return self.black_jack_possibilities
    
    def best_possible_black_jack(self):
        return self.all_black_jack_possibilities()[-1]
    
    def worst_possible_black_jack(self):
        return self.all_black_jack_possibilities()[0]