from collections import Counter

import hand_rankings

from card import Card


def score(cards: list[Card]) -> list[int]:
    rank_counts = Counter(card.rank for card in cards)

    rank_span = cards[0].rank - cards[-1].rank == 4
    wheel = [card.rank for card in cards] == [14, 5, 4, 3, 2]

    straight = wheel or (len(rank_counts) == 5 and rank_span)
    flush = len(set(card.suit for card in cards)) == 1
    four_of_a_kind = rank_counts.most_common(1)[0][1] == 4
    full_house = [count[1] for count in rank_counts.most_common(2)] == [3, 2]
    three_of_a_kind = len(rank_counts) == 3 and rank_counts.most_common(1)[0][1] == 3
    two_pair = len(rank_counts) == 3 and rank_counts.most_common(1)[1][1] == 2
    one_pair = len(rank_counts) == 4

    if straight and flush:
        return [hand_rankings.STRAIGHT_FLUSH] + ([] if wheel else [card.rank for card in cards])
    if four_of_a_kind:
        return [hand_rankings.FOUR_OF_A_KIND] + [count[0] for count in rank_counts.most_common(2)]
    if full_house:
        return [hand_rankings.FULL_HOUSE] + [count[0] for count in rank_counts.most_common(2)]
    if flush:
        return [hand_rankings.FLUSH] + [card.rank for card in cards]
    if straight:
        return [hand_rankings.STRAIGHT] + ([] if wheel else [card.rank for card in cards])
    if three_of_a_kind:
        trip_rank = rank_counts.most_common(1)[0][0]
        kickers = sorted([card.rank for card in cards if card.rank != trip_rank], reverse=True)

        return [hand_rankings.THREE_OF_A_KIND] + kickers
    if two_pair:
        kicker_rank = rank_counts.most_common(3)[2][0]
        pairs = sorted([card.rank for card in cards if card.rank != kicker_rank], reverse=True)

        return [hand_rankings.TWO_PAIR] + pairs + [kicker_rank]
    if one_pair:
        pair_rank = rank_counts.most_common(1)[0][0]
        kickers = sorted([card.rank for card in cards if card.rank != pair_rank], reverse=True)

        return [hand_rankings.ONE_PAIR] + [pair_rank] + kickers
    return [hand_rankings.HIGH_CARD] + [card.rank for card in cards]