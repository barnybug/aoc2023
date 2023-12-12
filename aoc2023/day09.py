from .utils import Answer


def predict(seq, forward):
    if seq.count(0) == len(seq):
        return 0
    diffs = [b - a for a, b in zip(seq, seq[1:])]
    if forward:
        return seq[-1] + predict(diffs, forward)
    else:
        return seq[0] - predict(diffs, forward)


def solve(input: str):
    numbers = [[int(i) for i in line.split()] for line in input.split("\n")]
    part1 = sum(predict(row, True) for row in numbers)
    part2 = sum(predict(row, False) for row in numbers)
    return Answer(part1, part2)
