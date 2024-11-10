from card import Card
from hand import Hand
from standard_ranker import StandardRanker


def test_that_creating_a_hand_sorts_it_from_smallest_to_largest():
    cards = [
        Card('3c'),
        Card('9c'),
        Card('4s'),
        Card('Kd'),
        Card('Jd')
    ]

    expected_sorting = [
        Card('Kd'),
        Card('Jd'),
        Card('9c'),
        Card('4s'),
        Card('3c'),
        
    ]

    hand = Hand(StandardRanker(), cards)

    assert hand.cards == expected_sorting