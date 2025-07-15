from deck import Deck
from holdem import Holdem

times = 1000000
tie_count = 0
player_count = 18
outcomes = {}
deck = Deck()

for i in range(times):

    if i % 1000 == 0:
        print(i, times, i/times)

    deck.shuffle()

    river = deck.cards[-1]
    turn = deck.cards[-2]
    flop = deck.cards[-5:-2]
    players = []

    for x in range(player_count):
        hole_cards = deck.cards[x*2:x*2+2]
        players.append(Holdem(hole_cards, flop, turn, river))

    players.sort()

    if players[-2] == players[-1]:
        tie_count += 1
        continue

    for he in players:
        classified = he.classify()

        if classified not in outcomes:
            outcomes[classified] = [0, 0]

        outcomes[classified][1] += 1

    outcomes[players[-1].classify()][0] += 1

for k, v in sorted(outcomes.items(), key=lambda item: -item[1][0]/item[1][1]):
    print(k, v, f'{round(100.0 * v[0] / v[1], 2)}%')

print(tie_count)