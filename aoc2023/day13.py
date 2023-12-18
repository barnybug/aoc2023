import numpy as np

from .utils import Answer


def reflects(pattern, target):
    for i in range(1, len(pattern)):
        mi = min(i, len(pattern) - i)
        diffs = (pattern[i : i + mi] != pattern[i - mi : i][::-1]).sum()
        if diffs == target:
            return i
    return 0


def part(patterns, target):
    total = 0
    for pattern in patterns:
        if horz := reflects(pattern, target):
            total += 100 * horz
        elif vert := reflects(pattern.T, target):
            total += vert
    return total


def solve(input: str):
    patterns = input.split("\n\n")
    patterns = [
        np.array([[c == "#" for c in line] for line in pattern.split()])
        for pattern in patterns
    ]
    part1 = part(patterns, 0)
    part2 = part(patterns, 1)
    return Answer(part1, part2)
