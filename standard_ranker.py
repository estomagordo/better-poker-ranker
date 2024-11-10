from collections.abc import Callable

from card import Card


class StandardRanker:
    def hand_size(self) -> int:
        return 5
    
    def score_compare(self) -> Callable[[Card], list[int]]:
        pass

    def sort_compare(self) -> Callable[[Card], int]:
        return lambda card: card.rank