# https://www.hackerrank.com/contests/projecteuler/challenges/euler054/problem
import collections

CARD_VALUES = '23456789TJQKA'

def evaluate_poker_hand(cards):
    def is_flush(cards):
        return len(set(card[-1] for card in cards)) == 1

    def is_straight(values):
        return max(values) - min(values) == 4 and len(set(values)) == 5

    card_suits = [card[-1] for card in cards]
    same_suit = len(set(card_suits)) == 1

    card_ranks = [CARD_VALUES.index(card[0]) for card in cards]
    card_ranks.sort(reverse=True)

    if card_ranks == [12, 3, 2, 1, 0]:
        if same_suit:
            return (8, 3)
        else:
            return (4, 3)

    differences = [card_ranks[i] - card_ranks[i+1] for i in range(4)]
    differences.append(-1)

    groups = []
    start = 0
    for i in range(1, len(differences)):
        if differences[i] != differences[i-1]:
            groups.append((differences[i-1], i - start))
            start = i

    consecutive_values = (1, 4) in groups

    values_same = [rank[0] for rank in collections.Counter(card_ranks).most_common()]

    if same_suit and consecutive_values:
        return (8, max(card_ranks))
    elif (0, 3) in groups:
        return (7, *values_same)
    elif (0, 1) in groups and (0, 2) in groups:
        return (6, *values_same)
    elif same_suit:
        return (5, *card_ranks)
    elif consecutive_values:
        return (4, max(card_ranks))
    elif (0, 2) in groups:
        return (3, *values_same)
    elif groups.count((0, 1)) == 2:
        return (2, *values_same)
    elif (0, 1) in groups:
        return (1, *values_same)
    else:
        return (0, *card_ranks)

def determine_winner(player1, player2):
    size = min(len(player1), len(player2))
    for i in range(size):
        if player1[i] > player2[i]:
            return 'Player 1'
        elif player1[i] < player2[i]:
            return 'Player 2'

if __name__ == "__main__":
    num_cases = int(input())
    for _ in range(num_cases):
        cards = input().split()

        player1 = cards[:5]
        player2 = cards[5:]

        poker_hand1 = evaluate_poker_hand(player1)
        poker_hand2 = evaluate_poker_hand(player2)

        winner = determine_winner(poker_hand1, poker_hand2)
        print(winner)
