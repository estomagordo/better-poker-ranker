from collections.abc import Callable
from typing import Protocol

from card import Card


class RankingSchema(Protocol):
    def hand_size(self) -> int: ...
    def score_compare(self) -> Callable[[Card], list[int]]: ...
    def sort_compare(self) -> Callable[[Card], int]: ...