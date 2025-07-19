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


def test_scoring_aces():
    assert score([ACE, DEUCE]) == 13
    assert score([ACE, NINE]) == 20
    assert score([ACE, TEN]) == 21
    assert score([ACE, KING]) == 21
    assert score([ACE, ACE, ACE, ACE, FIVE]) == 19
    assert score([ACE, ACE, KING]) == 12


def test_scoring_bust():
    assert score([ACE, ACE, KING, KING]) == 0
    assert score([DEUCE] * 11) == 0
    assert score([NINE, NINE, FIVE]) == 0