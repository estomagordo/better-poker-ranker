import sample_hands

from high_scorer import score


def test_scoring_royal_flush():
    assert [8, 14, 13, 12, 11, 10] == score(sample_hands.royal_flush)