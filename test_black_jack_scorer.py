from black_jack_scorer import score
from card import Card

DEUCE = Card('2s')
FIVE = Card('5s')
NINE = Card('9s')
TEN = Card('Ts')
KING = Card('Ks')
ACE = Card('As')


def test_scoring_simple():
    assert score([DEUCE, DEUCE]) == 4
    assert score([DEUCE, NINE]) == 11
    assert score([FIVE, NINE]) == 14
    assert score([NINE, FIVE]) == 14
    assert score([FIVE, KING]) == 15