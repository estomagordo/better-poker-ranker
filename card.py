from card_rankings import card_rankings


class Card:
    def __init__(self, compact: str):
        self.compact = compact
        self.rank = card_rankings[compact[0]]
        self.suit = compact[1]

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False

        return self.compact == other.compact

    def __str__(self):
        return self.compact

    def __repr__(self):
        return str(self)
