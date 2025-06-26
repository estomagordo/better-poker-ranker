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