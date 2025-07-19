from deck import Deck
from omajack import Omajack

times = 10000
minplayers = 2
maxplayers = 4
showper = 20

results = []

for player_count in range(minplayers, maxplayers+1):
    results.append([player_count, {}, {}])

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
            players.append([x, hand.best_hand()[0], hand.best_hand()[1], hand.rank_classify(), hand.nuanced_classify()])

        best_omaha = max(player[1] for player in players)
        best_black_jack = max(player[2] for player in players)
        omaha_winners = sum(player[1] == best_omaha for player in players)
        black_jack_winners = sum(player[2] == best_black_jack for player in players)

        for x, omaha, black_jack, rank_class, nuanced_class in players:
            wins = 0.0

            if omaha == best_omaha:
                wins += 0.5/omaha_winners

            if black_jack == best_black_jack:
                wins += 0.5/black_jack_winners

            if rank_class not in results[player_count-minplayers][1]:
                results[player_count-minplayers][1][rank_class] = [0.0, 0.0, 0.0]

            if nuanced_class not in results[player_count-minplayers][2]:
                results[player_count-minplayers][2][nuanced_class] = [0.0, 0.0, 0.0]

            results[player_count-minplayers][1][rank_class][0] += wins
            results[player_count-minplayers][1][rank_class][1] += 1.0
            results[player_count-minplayers][1][rank_class][2] = results[player_count-minplayers][1][rank_class][0] / results[player_count-minplayers][1][rank_class][1]
            results[player_count-minplayers][2][nuanced_class][0] += wins
            results[player_count-minplayers][2][nuanced_class][1] += 1.0
            results[player_count-minplayers][2][nuanced_class][2] = results[player_count-minplayers][2][nuanced_class][0] / results[player_count-minplayers][2][nuanced_class][1]

for player_count in range(minplayers, maxplayers+1):
    _, rank_class_rankings, nuanced_class_rankings = results[player_count-minplayers]

    print(f'Player count: {player_count}')
    print('Best rank classified hands:')

    for classified, scores in sorted(rank_class_rankings.items(), key=lambda scores: -scores[2])[:showper]:
        print(classified, scores)

    print('Best nuanced classified hands:')

    for classified, scores in sorted(nuanced_class_rankings.items(), key=lambda scores: -scores[2])[:showper]:
        print(classified, scores)