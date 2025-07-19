from itertools import product

from card import Card
from card_rankings import black_jack_rankings

def score(cards: list[Card]) -> list[int]:
    LIMIT = 21

    best = 0

    for selection in product(*list([black_jack_rankings[card.raw_rank] for card in cards])):
        s = sum(selection)
        
        if s > LIMIT:
            s = 0

        best = max(best, s)

    return best