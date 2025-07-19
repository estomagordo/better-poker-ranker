from collections.abc import Callable

from card import Card
from high_scorer import score


class OmajackRanker:
    def hand_size(self) -> int:
        return 5 # Unclear if this should actually remain? Is it useful?
    
    def hand_score(self) -> Callable[[list[Card]], list[int]]:
        return score

    def card_compare(self) -> Callable[[Card], int]:
        return lambda card: -card.rank # Is this even needed?
