from card import Card
from ranking_schema import RankingSchema


class Hand:
    def __init__(self, ranking: RankingSchema, cards: list[Card]):
        self.ranking = ranking
        self.cards = sorted(cards, key=ranking.card_compare())

    def __lt__(self, other):
        return self.ranking.hand_score()(self.cards) < self.ranking.hand_score()(other.cards)
    
    def __le__(self, other):
        return self.ranking.hand_score()(self.cards) <= self.ranking.hand_score()(other.cards)
    
    def __gt__(self, other):
        return self.ranking.hand_score()(self.cards) > self.ranking.hand_score()(other.cards)
    
    def __ge__(self, other):
        return self.ranking.hand_score()(self.cards) >= self.ranking.hand_score()(other.cards)
    
    def __eq__(self, other):
        return self.ranking.hand_score()(self.cards) == self.ranking.hand_score()(other.cards)
    
    def __ne__(self, other):
        return self.ranking.hand_score()(self.cards) != self.ranking.hand_score()(other.cards)
    
    def __str__(self):
        return f'[{",".join(card for card in self.cards)}]'
    
    def __repr__(self):
        return str(self)