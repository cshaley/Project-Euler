from __future__ import division
from collections import Counter
import numpy as np

poker_file = 'p054_poker.txt'


def compare_hands(h1, h2):
    h1_score = h1.getHandScore()
    h2_score = h2.getHandScore()
    # print h1_score
    # print h2_score
    if h1_score > h2_score:
        return True
    return False


class PokerHand(object):
    nums = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['H', 'C', 'S', 'D']
    cardnumdict = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
                   '8': '8', '9': '9', 'T': '10', 'J': 'Jack', 'Q': 'Queen',
                   'K': 'King'}
    cardsuitdict = {'C': 'Clubs', 'D': 'Diamonds', 'H': 'Hearts',
                    'S': 'Spades'}

    def __init__(self, cards):
        if not cards:
            raise
        if len(cards) < 5:
            raise

        self.cards = cards
        self.cardnums = [a[0] for a in cards]
        self.cardsuits = [a[1] for a in cards]
        self.cardnumcts = Counter(self.cardnums)
        self.cardnumset = set(self.cardnums)

    def __str__(self):
        return "{0}\n{1}".format(str(self.cards), self.getHandType())

    def getHandType(self):
        if self.isRoyalFlush():
            return "Royal Flush"
        if self.isStraightFlush():
            return "Straight Flush"
        if self.isFourOfAKind():
            return "Four of a Kind"
        if self.isFullHouse():
            return "Full House"
        if self.isFlush():
            return "Flush"
        if self.isStraight():
            return "Straight"
        if self.isThreeOfAKind():
            return "Three of a Kind"
        if self.isTwoPairs():
            return "Two Pairs"
        if self.isOnePair():
            return "One Pair"
        return "High Card"

    def getHandScore(self):
        a = 10**2
        b = 10**4
        c = 10**6
        d = 10**8
        e = 10**10

        if self.isRoyalFlush():
            return 10

        sf = self.isStraightFlush()
        if sf:
            return 9 + self.nums.index(sf)/a

        foak = self.isFourOfAKind()
        if foak:
            return 8 + self.nums.index(foak[0])/a + self.nums.index(foak[1])/b

        fh = self.isFullHouse()
        if fh:
            return 7 + self.nums.index(fh[0])/a + self.nums.index(fh[1])/b

        f = self.isFlush()
        if f:
            ghc = self.getHighestCards()
            return 6 + np.dot([1/a, 1/b, 1/c, 1/d, 1/e], ghc)

        s = self.isStraight()
        if s:
            return 5 + self.nums.index(s)/a

        toak = self.isThreeOfAKind()
        if toak:
            return 4 + self.nums.index(toak[0])/a + self.nums.index(toak[1][0])/b + self.nums.index(toak[1][1])/c

        tp = self.isTwoPairs()
        if tp:
            return 3 + self.nums.index(tp[0][0])/a + self.nums.index(tp[0][1])/b + self.nums.index(tp[1][0])/c

        op = self.isOnePair()
        if op:
            return 2 + self.nums.index(op[0])/a + self.nums.index(op[1][0])/b + self.nums.index(op[1][1])/c + self.nums.index(op[1][2])/d

        ghc = self.getHighestCards()
        return 1 + np.dot([1/a, 1/b, 1/c, 1/d, 1/e], ghc)

    def isRoyalFlush(self):
        return self.isStraightFlush() and self.getHighCard() == 'A'

    def isStraightFlush(self):
        if not (self.isStraight() and self.isFlush()):
            return False
        return self.getHighCard()

    def isFourOfAKind(self):
        if 4 not in self.cardnumcts.values():
            return False
        for key, value in self.cardnumcts.items():
            if value == 4:
                k1 = key
            else:
                k2 = key
        return (k1, k2)

    def isFullHouse(self):
        if not (3 in self.cardnumcts.values() and 2 in self.cardnumcts.values()):
            return False
        for key, value in self.cardnumcts.items():
            if value == 3:
                k1 = key
            elif value == 2:
                k2 = key
        return (k1, k2)

    def isFlush(self):
        if not len(set(self.cardsuits)) == 1:
            return False
        return self.getHighCard()

    def isStraight(self):
        if len(self.cardnumset) < 5:
            return False
        for i in range(len(self.nums)-5):
            if set(self.nums[i:i+5]) == self.cardnumset:
                return self.nums[i+5]
        return False

    def isThreeOfAKind(self):
        if 3 not in self.cardnumcts.values():
            return False
        for key, value in self.cardnumcts.items():
            if value == 3:
                k1 = key
        return (k1, self.getHighestCards([a for a in self.cardnums if a != k1]))

    def isTwoPairs(self):
        if not Counter(self.cardnumcts.values())[2] == 2:
            return False
        k1 = []
        for key, value in self.cardnumcts.items():
            if value == 2:
                k1.append(key)
        k1 = sorted(k1, reverse=True)
        return (k1, [a for a in self.cardnums if a not in k1])

    def isOnePair(self):
        if 2 not in self.cardnumcts.values():
            return False
        for key, value in self.cardnumcts.items():
            if value == 2:
                k1 = key
        return (k1, self.getHighestCards([a for a in self.cardnums if a != k1]))

    def getHighCard(self):
        maxidx = -1
        for cardnum in self.cardnums:
            idx = self.nums.index(cardnum)
            if maxidx < idx:
                maxidx = idx
        return maxidx

    def getHighestCards(self, remainingCards=None):
        if remainingCards is None:
            cardnums = [self.nums.index(a) for a in self.cardnums]
            return sorted(cardnums, reverse=True)
        else:
            return list(sorted(remainingCards, reverse=True))

    @classmethod
    def cardNumToString(cardnum):
        return self.cardnumdict[cardnum]

    @classmethod
    def cardSuitToString(cardsuit):
        return self.cardsuitdict[cardsuit]

arr = []
with open(poker_file, 'r') as f:
    for line in f.readlines():
        lst = line.split()
        p1h = lst[:5]
        p2h = lst[5:]
        # print p1h
        # print p2h
        p1_hand = PokerHand(p1h)
        p2_hand = PokerHand(p2h)
        res = compare_hands(p1_hand, p2_hand)
        arr.append(res)

print Counter(arr)
