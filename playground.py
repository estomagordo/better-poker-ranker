from deck import Deck
from omajack import Omajack

times = 100000
minplayers = 2
maxplayers = 4
showper = 20

results = []

for player_count in range(minplayers, maxplayers+1):
    results.append([player_count, {}, {}, {}, {}])

deck = Deck()

for i in range(times):
    if i % 1000 == 0:
        print(i, times, i/times)

    for player_count in range(minplayers, maxplayers+1):
        deck.shuffle()

        river = deck.cards[-1]
        turn = deck.cards[-2]
        flop = deck.cards[-5:-2]
        players = []

        for x in range(player_count):
            hole_cards = deck.cards[x*5:x*5+5]
            hand = Omajack(hole_cards, flop, turn, river)
            players.append([x, hand.best_hand()[1].hand_score(), hand.worst_possible_black_jack(), hand.best_possible_black_jack()])

        best_black_jack = max(player[1] for player in players)
        black_jack_winners = sum(player[1] == best_black_jack for player in players)

        if best_black_jack not in results[player_count-minplayers][1]:
            results[player_count-minplayers][1][best_black_jack] = 0

        results[player_count-minplayers][1][best_black_jack] += 1

        for x, black_jack_score, worst_bj, best_bj in players:
            wins = 0.0

            if black_jack_score == best_black_jack:
                wins += 1.0/black_jack_winners
                
            if black_jack_score not in results[player_count-minplayers][2]:
                results[player_count-minplayers][2][black_jack_score] = [0.0, 0.0]
            if worst_bj not in results[player_count-minplayers][3]:
                results[player_count-minplayers][3][worst_bj] = [0.0, 0.0]
            if best_bj not in results[player_count-minplayers][4]:
                results[player_count-minplayers][4][best_bj] = [0.0, 0.0]

            results[player_count-minplayers][2][black_jack_score][0] += wins
            results[player_count-minplayers][2][black_jack_score][1] += 1.0
            results[player_count-minplayers][3][worst_bj][0] += wins
            results[player_count-minplayers][3][worst_bj][1] += 1.0
            results[player_count-minplayers][4][best_bj][0] += wins
            results[player_count-minplayers][4][best_bj][1] += 1.0

for player_count in range(minplayers, maxplayers+1):
    _, winners, playing, worst, best = results[player_count-minplayers]

    print(f'Player count: {player_count}')
    
    print('Distribution for hand winners')
    for k in sorted(winners.keys()):
        print(k, winners[k])

    print('Best nuanced classified hands:')

    for classified, scores in sorted(nuanced_class_rankings.items(), key=lambda item: -item[1][2])[:showper]:
        print(classified, scores)