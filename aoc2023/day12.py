from itertools import combinations
from .utils import Answer


def arrangements(line: str):
    pattern, numbers = line.split(" ")
    pattern = pattern.strip(".").rstrip(".")
    blanks = [1 << i for i, c in enumerate(pattern) if c == "?"]
    numbers = [int(n) for n in numbers.split(",")]
    missing = sum(numbers) - pattern.count("#")
    existing = sum(1 << i for i, c in enumerate(pattern) if c == "#")
    count = 0

    for comb in combinations(blanks, missing):
        combined = sum(comb) + existing
        pos = 0
        while True:
            # shift out zeros
            while combined & 1 == 0:
                combined >>= 1
            n = 1
            combined >>= 1
            while combined & 1 == 1:
                combined >>= 1
                n += 1
            if n != numbers[pos]:
                break
            pos += 1
            if pos == len(numbers):
                count += 1
                break

    return count


def solve(input: str):
    part1 = sum(map(arrangements, input.split("\n")))
    return Answer(part1, 0)
