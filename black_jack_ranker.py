from collections.abc import Callable

from card import Card
from black_jack_scorer import score


class BlackJackRanker:
    def hand_size(self) -> int:
        return 5
    
    def hand_score(self) -> Callable[[list[Card]], list[int]]:
        return score

    def card_compare(self) -> Callable[[Card], int]:
        return lambda card: -card.rank
