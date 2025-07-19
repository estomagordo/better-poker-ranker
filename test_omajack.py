from omajack import Omajack
from card import Card


def test_rank_classify():
    flop = [Card('Ah'), Card('Jh'), Card('7d')]
    turn = Card('9c')
    river = Card('9s')

    hole_cards = [Card('Ad'), Card('Jh'), Card('Th'), Card('8s'), Card('7h')]

    hand = Omajack(hole_cards, flop, turn, river)

    assert hand.rank_classify() == 'AJT87'


