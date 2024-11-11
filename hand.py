from card import Card
from ranking_schema import RankingSchema


class Hand:
    def __init__(self, ranking: RankingSchema, cards: list[Card]):
        self.ranking = ranking
        self.cards = sorted(cards, key=ranking.card_compare())
        self.score = []

    def hand_score(self):
        if not self.score:
            self.score = self.ranking.hand_score()(self.cards)

        return self.score

    def __lt__(self, other):
        return self.hand_score() < other.hand_score()

    def __le__(self, other):
        return self.hand_score() <= other.hand_score()

    def __gt__(self, other):
        return self.hand_score() > other.hand_score()

    def __ge__(self, other):
        return self.hand_score() >= other.hand_score()

    def __eq__(self, other):
        return self.hand_score() == other.hand_score()

    def __ne__(self, other):
        return self.hand_score() != other.hand_score()

    def __str__(self):
        return f'[{",".join(str(card) for card in self.cards)}]'

    def __repr__(self):
        return str(self)
