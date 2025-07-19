from omajack import Omajack
from card import Card


def test_rank_classify():
    flop = [Card('Ah'), Card('Jh'), Card('7d')]
    turn = Card('9c')
    river = Card('9s')

    hole_cards = [Card('Th'), Card('8s'), Card('Jh'), Card('7h'), Card('Ad')]

    hand = Omajack(hole_cards, flop, turn, river)

    assert hand.rank_classify() == 'AJT87'


def test_nuanced_classify():
    flop = [Card('Ah'), Card('Jh'), Card('7d')]
    turn = Card('9c')
    river = Card('9s')

    three_one_one_hole_cards = [Card('Th'), Card('8s'), Card('Jh'), Card('7h'), Card('Ad')]
    three_two_hole_cards = [Card('Th'), Card('8d'), Card('Jh'), Card('7h'), Card('Ad')]
    four_one_hole_cards = [Card('Th'), Card('8h'), Card('Jh'), Card('7h'), Card('Ad')]
    two_one_one_one_hole_cards = [Card('Tc'), Card('8s'), Card('Jh'), Card('7h'), Card('Ad')]

    three_one_one_hole_hand = Omajack(three_one_one_hole_cards, flop, turn, river)
    three_two_hole_hand = Omajack(three_two_hole_cards, flop, turn, river)
    four_one_hole_hand = Omajack(four_one_hole_cards, flop, turn, river)
    two_one_one_one_hole_hand = Omajack(two_one_one_one_hole_cards, flop, turn, river)

    assert three_one_one_hole_hand.nuanced_classify() == 'AaJbTb8c7b'
    assert three_two_hole_hand.nuanced_classify() == 'AaJbTb8a7b'
    assert four_one_hole_hand.nuanced_classify() == 'AaJbTb8b7b'
    assert two_one_one_one_hole_hand.nuanced_classify() == 'AaJbTc8d7b'