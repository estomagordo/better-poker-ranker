from itertools import product
from random import shuffle

import utils
from card import Card

class Deck:
    def __init__(self):
        self.cards = []

        for p in product(utils.ALL_RANKS, utils.ALL_SUITS):
            self.cards.append(Card(''.join(p)))

    def shuffle(self):
        shuffle(self.cards)