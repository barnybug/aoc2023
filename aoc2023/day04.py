from .utils import Answer


def score(line: str) -> int:
    left, right = line.split("|")
    winning = {int(n) for n in left.split()[2:]}
    numbers = [int(n) for n in right.split()]
    overlap = winning.intersection(numbers)
    return len(overlap)


def solve(input: str):
    scores = [score(line) for line in input.split("\n")]
    points = [2 ** (s - 1) if s > 0 else 0 for s in scores]
    part1 = sum(points)

    cards = [1] * len(scores)
    for i, no in enumerate(cards):
        for j in range(scores[i]):
            cards[i + j + 1] += no
    part2 = sum(cards)

    return Answer(part1, part2)
