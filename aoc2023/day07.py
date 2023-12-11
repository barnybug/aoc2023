from collections import Counter

from .utils import Answer

VALUES = {str(i): i for i in range(2, 10)} | {c: i + 10 for i, c in enumerate("TJQKA")}
VALUES2 = VALUES | {"J": 1}


class Hand:
    def __init__(self, line):
        self.cards, bid = line.split(" ")
        self.bid = int(bid)


def card_values(hand, most, second, values):
    handtype = most * 3 + second
    return [handtype] + [values[c] for c in hand.cards]


def key(hand: Hand):
    c = Counter(hand.cards)
    counts = [c for _, c in c.most_common()]
    most = counts[0]
    second = counts[1] if len(counts) > 1 else 0
    return card_values(hand, most, second, VALUES)


def key2(hand: Hand):
    jokers = len([c for c in hand.cards if c == "J"])
    without_jokers = hand.cards.replace("J", "")
    c = Counter(without_jokers)
    counts = [c for _, c in c.most_common()]
    most = (counts[0] if counts else 0) + jokers
    second = counts[1] if len(counts) > 1 else 0
    return card_values(hand, most, second, VALUES2)


def solve(input: str):
    hands = [Hand(line) for line in input.split("\n")]
    part1 = sum((i + 1) * hand.bid for i, hand in enumerate(sorted(hands, key=key)))
    part2 = sum((i + 1) * hand.bid for i, hand in enumerate(sorted(hands, key=key2)))
    return Answer(part1, part2)
