from card import Card
from ranking_schema import RankingSchema


class Hand:
    def __init__(self, ranking: RankingSchema, cards: list[Card]):
        self.cards = sorted(cards, key=ranking.sort_compare())