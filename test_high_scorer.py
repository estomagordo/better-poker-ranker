import sample_hands

from high_scorer import score


def test_scoring_royal_flush():
    assert [8, 14, 13, 12, 11, 10] == score(sample_hands.royal_flush)


def test_straight_flush_beats_four_of_a_kind():
    assert score(sample_hands.wheel_straight_flush) > score(sample_hands.four_fives)


def test_four_of_a_kind_beats_full_house():
    assert score(sample_hands.four_kings) > score(sample_hands.full_house_eights_over_deuces)


def test_full_house_beats_flush():
    assert score(sample_hands.full_house_eights_over_deuces) > score(sample_hands.jack_high_flush)


def test_flush_beats_straight():
    assert score(sample_hands.jack_high_flush) > score(sample_hands.nine_high_straight)


def test_straight_beats_three_of_a_kind():
    assert score(sample_hands.nine_high_straight) > score(sample_hands.three_queens)


def test_three_of_a_kind_beats_two_pair():
    assert score(sample_hands.three_queens) > score(sample_hands.two_pair_aces_and_fours)


def test_two_pair_beats_one_pair():
    assert score(sample_hands.two_pair_aces_and_fours) > score(sample_hands.pair_of_fives)


def test_one_pair_beats_high_card():
    assert score(sample_hands.pair_of_fives) > score(sample_hands.high_card_hand)


def test_hand_equals_itself():
    assert score(sample_hands.jack_high_flush) == score(sample_hands.jack_high_flush)