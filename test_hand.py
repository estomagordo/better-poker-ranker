import sample_hands

from hand import Hand
from standard_ranker import StandardRanker


def test_straight_flush_beats_four_of_a_kind_with_standard_ranker():
    handA = Hand(StandardRanker, sample_hands.wheel_straight_flush)
    handB = Hand(StandardRanker, sample_hands.four_kings)

    assert handA > handB