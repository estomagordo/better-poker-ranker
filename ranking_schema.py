from collections.abc import Callable
from typing import Protocol

from card import Card


class RankingSchema(Protocol):
    def hand_size(self) -> int: ...
    def hand_score(self) -> Callable[[list[Card]], list[int]]: ...
    def card_compare(self) -> Callable[[Card], int]: ...
