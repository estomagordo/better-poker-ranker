from card import Card
from ranking_schema import RankingSchema


class Hand:
    def __init__(self, ranking: RankingSchema, cards: list[Card]):
        self.ranking = ranking
        self.cards = sorted(cards, key=ranking.card_compare())

    def __lt__(self, other):
        return self.ranking.card_compare(self.cards) < self.ranking.card_compare(other.cards)
    
    def __le__(self, other):
        return self.ranking.card_compare(self.cards) <= self.ranking.card_compare(other.cards)
    
    def __gt__(self, other):
        return self.ranking.card_compare(self.cards) > self.ranking.card_compare(other.cards)
    
    def __ge__(self, other):
        return self.ranking.card_compare(self.cards) >= self.ranking.card_compare(other.cards)
    
    def __eq__(self, other):
        return self.ranking.card_compare(self.cards) == self.ranking.card_compare(other.cards)
    
    def __ne__(self, other):
        return self.ranking.card_compare(self.cards) != self.ranking.card_compare(other.cards)