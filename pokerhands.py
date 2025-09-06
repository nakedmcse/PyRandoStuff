# project euler 54 Poker hand ranker
# https://projecteuler.net/problem=54
from enum import Enum

card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

class HandRanking(Enum):
    HighCard = 1
    OnePair = 2
    TwoPairs = 3
    ThreeOfAKind = 4
    Straight = 5
    Flush = 6
    FullHouse = 7
    FourOfAKind = 8
    StraightFlush = 9
    RoyalFlush = 10

class Rank:
    def __init__(self, rank: int, ranking_high_cards: list[int], high_card: int, cards: list[int]):
        self.rank = rank
        self.ranking_high_cards = ranking_high_cards
        self.high_card = high_card
        self.cards = cards

    def __repr__(self):
        return f"Rank({self.rank}, {self.ranking_high_cards}, {self.high_card}, {self.cards})"

    def __cmp__(self, other):
        # Compare base rank
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        # Compare rank high cards
        for rhci in range(len(self.ranking_high_cards)):
            if self.ranking_high_cards[rhci] > other.ranking_high_cards[rhci]: return 1
            if self.ranking_high_cards[rhci] < other.ranking_high_cards[rhci]: return -1

        # Compare remaining high card
        if self.high_card > other.high_card: return 1
        if self.high_card < other.high_card: return -1

        # Compare remaining cards
        s_remaining = sorted([c for c in self.cards if c not in self.ranking_high_cards and c != self.high_card], reverse=True)
        o_remaining = sorted([c for c in other.cards if c not in other.ranking_high_cards and c != other.high_card], reverse=True)
        for remi in range(len(s_remaining)):
            if s_remaining[remi] > o_remaining[remi]: return 1
            if s_remaining[remi] < o_remaining[remi]: return -1

        # Draw
        return 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

def rankHand(hand: list[str]) -> Rank:
    # Get high card, number of suits and counts of face cards
    cards = sorted([card_values.index(c[0]) for c in hand], reverse=True)
    high_card = max(cards)
    rankings = [HandRanking.HighCard.value]
    rank = Rank(HandRanking.HighCard.value, [high_card], high_card, cards)

    suits = set([c[1] for c in hand])
    faces = {}
    for c in hand:
        if c[0] in faces: faces[c[0]] += 1
        else: faces[c[0]] = 1

    # Check multi card rankings
    if any(v for v in faces.values() if v>1):
        if len([v for v in faces.values() if v == 2]) == 1:
            rankings.append(HandRanking.OnePair.value)
            rank.ranking_high_cards = [card_values.index(k) for k,v in faces.items() if v == 2]
        if len([v for v in faces.values() if v == 2]) == 2:
            rankings.append(HandRanking.TwoPairs.value)
            rank.ranking_high_cards = [card_values.index(k) for k,v in faces.items() if v == 2]
        if len([v for v in faces.values() if v == 3]) == 1:
            rankings.append(HandRanking.ThreeOfAKind.value)
            rank.ranking_high_cards = [card_values.index(k) for k,v in faces.items() if v == 3]
        if HandRanking.ThreeOfAKind.value in rankings and HandRanking.OnePair.value in rankings:
            rankings.append(HandRanking.FullHouse.value)
            rank.ranking_high_cards = [card_values.index(k) for k,v in faces.items() if v == 3]
            pair_val = [card_values.index(k) for k,v in faces.items() if v == 2]
            rank.ranking_high_cards.append(pair_val[0])
        if len([v for v in faces.values() if v == 4]) == 1:
            rankings.append(HandRanking.FourOfAKind.value)
            rank.ranking_high_cards = [card_values.index(k) for k,v in faces.items() if v == 4]
        if high_card in rank.ranking_high_cards and HandRanking.FullHouse.value not in rankings:
            high_card = max(c for c in cards if c not in rank.ranking_high_cards)

    # Check same suit rankings
    if len(suits) == 1:
        rank.ranking_high_cards = [high_card]
        if 'T' in faces and 'J' in faces and 'Q' in faces and 'K' in faces and 'A' in faces:
            rankings.append(HandRanking.RoyalFlush.value)
        elif cards[0]+1 == cards[1] and cards[1]+1 == cards[2] and cards[2]+1 == cards[3] and cards[3]+1 == cards[4] and cards[4]+1 == cards[5]:
            rankings.append(HandRanking.StraightFlush.value)
        else:
            rankings.append(HandRanking.Flush.value)

    # Check straight
    if cards[0]+1 == cards[1] and cards[1]+1 == cards[2] and cards[2]+1 == cards[3] and cards[3]+1 == cards[4] and cards[4]+1 == cards[5]:
        rank.ranking_high_cards = [high_card]
        rankings.append(HandRanking.Straight.value)

    rank.rank = max(rankings)
    return rank

player1rank = rankHand('5H 5C 6S 7S KD'.split(' '))
player2rank = rankHand('2C 3S 8S 8D TD'.split(' '))
print(f'{player1rank} vs {player2rank} - {'Player 1 Wins' if player1rank > player2rank else 'Player 2 Wins'}')

player1rank = rankHand('5D 8C 9S JS AC'.split(' '))
player2rank = rankHand('2C 5C 7D 8S QH'.split(' '))
print(f'{player1rank} vs {player2rank} - {'Player 1 Wins' if player1rank > player2rank else 'Player 2 Wins'}')

player1rank = rankHand('2D 9C AS AH AC'.split(' '))
player2rank = rankHand('3D 6D 7D TD QD'.split(' '))
print(f'{player1rank} vs {player2rank} - {'Player 1 Wins' if player1rank > player2rank else 'Player 2 Wins'}')

player1rank = rankHand('4D 6S 9H QH QC'.split(' '))
player2rank = rankHand('3D 6D 7H QD QS'.split(' '))
print(f'{player1rank} vs {player2rank} - {'Player 1 Wins' if player1rank > player2rank else 'Player 2 Wins'}')

player1rank = rankHand('2H 2D 4C 4D 4S'.split(' '))
player2rank = rankHand('3C 3D 3S 9S 9D'.split(' '))
print(f'{player1rank} vs {player2rank} - {'Player 1 Wins' if player1rank > player2rank else 'Player 2 Wins'}')
print()

player1wins = 0
with open('pokerhands.txt') as f:
    lines = f.read().splitlines()
    for l in lines:
        sl = l.split(' ')
        if rankHand(sl[0:5]) > rankHand(sl[5:10]): player1wins += 1
print(f'Player 1 Wins: {player1wins}')