#!/usr/bin/env python3
# https://adventofcode.com/2023/day/7
from collections import Counter
from enum import auto
from enum import Enum
from functools import cmp_to_key

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARDS_P2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


class Types(Enum):
    High = auto()
    OnePair = auto()
    TwoPair = auto()
    ThreeKind = auto()
    FullHouse = auto()
    FourKind = auto()
    FiveKind = auto()

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value


class Hand:
    def __init__(self, hand):
        cards, bid = hand.split()
        self.hand = cards
        self.bid = int(bid)
        self.cards = list(self.hand)
        self.get_type()  # Initial type assignment
        self.mut = False

    def __repr__(self) -> str:
        return "".join(self.cards) + ":" + str(self.type)

    def get_type(self):
        # Get hand type for current Hand
        ct = Counter(self.cards).most_common()
        match ct[0][1]:
            case 5:
                self.type = Types.FiveKind
            case 4:
                self.type = Types.FourKind
            case 3:
                if ct[1][1] == 2:
                    self.type = Types.FullHouse
                else:
                    self.type = Types.ThreeKind
            case 2:
                if ct[1][1] == 2:
                    self.type = Types.TwoPair
                else:
                    self.type = Types.OnePair
            case _:
                self.type = Types.High
        return self.type

    @staticmethod
    def cmp(first, other) -> int:
        # Compare relative value of two Hands
        if first.type > other.type:
            return 1
        elif first.type < other.type:
            return -1
        else:
            # Compare cards in hand
            # Create lists from original hand, in case of Joker mutation
            for c, o in zip(list(first.hand), list(other.hand), strict=True):
                if any([first.mut, other.mut]):
                    # Jokers have been mutated, use card ordering with Joker lowest
                    cv = CARDS_P2.index(c)
                    co = CARDS_P2.index(o)
                else:
                    cv = CARDS.index(c)
                    co = CARDS.index(o)
                if cv > co:
                    return 1
                elif cv < co:
                    return -1
            return 0

    def mutate_jokers(self):
        # Mutate cards, replacing Jokers with next highest value
        if "J" not in self.cards:
            return
        ct = Counter(self.cards).most_common()
        self.mut = True
        # Use 2nd most common element if Jokers are most common (and hand is not *all* Jokers), else use most common
        self.cards = list(self.hand.replace("J", ct[1][0] if ct[0][0] == "J" and len(ct) > 1 else ct[0][0]))
        self.type = self.get_type()  # Get new type


hands = [Hand(l) for l in lines]
hands.sort(key=cmp_to_key(Hand.cmp))

print(f"Part 1: {sum(h.bid * (i + 1) for i, h in enumerate(hands))}")

# Mutate Jokers and sort hand again
for h in hands:
    h.mutate_jokers()
hands.sort(key=cmp_to_key(Hand.cmp))

print(f"Part 2: {sum(h.bid * (i + 1) for i, h in enumerate(hands))}")
