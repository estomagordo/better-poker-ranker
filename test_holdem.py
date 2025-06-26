from card import Card
from holdem import Holdem


def test_flush_over_flush():
    flop = [Card('7s'), Card('9s'), Card('Qd')]
    turn = Card('2c')
    river = Card('Ks')

    player_a = [Card('Ts'), Card('3s')]
    player_b = [Card('As'), Card('5s')]

    small_flush = Holdem(player_a, flop, turn, river)
    big_flush = Holdem(player_b, flop, turn, river)

    assert(big_flush > small_flush)


def test_royal_on_board():
    flop = [Card('Ad'), Card('Qd'), Card('Jd')]
    turn = Card('Kd')
    river = Card('Td')

    player_a = [Card('Ts'), Card('3s')]
    player_b = [Card('As'), Card('5s')]

    a = Holdem(player_a, flop, turn, river)
    b = Holdem(player_b, flop, turn, river)

    assert(a == b)


def test_one_liner():
    flop = [Card('7s'), Card('9s'), Card('Td')]
    turn = Card('Jc')
    river = Card('Ah')

    player_a = [Card('Ad'), Card('As')]
    player_b = [Card('2s'), Card('8c')]

    set = Holdem(player_a, flop, turn, river)
    straight = Holdem(player_b, flop, turn, river)

    assert(straight > set)