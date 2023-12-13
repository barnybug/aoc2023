from itertools import accumulate, combinations

from .utils import Answer


def distance(input: str, multiplier: int) -> int:
    lines = input.split("\n")
    y_empty = [int("#" not in line) for line in lines]
    y_expand = list(accumulate(y_empty))
    width = len(lines[0])
    x_empty = [int(all(line[i] != "#" for line in lines)) for i in range(width)]
    x_expand = list(accumulate(x_empty))

    galaxies = [
        (x + x_expand[x] * multiplier, y + y_expand[y] * multiplier)
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
        if c == "#"
    ]
    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in combinations(galaxies, 2))


def solve(input: str):
    part1 = distance(input, 1)
    part2 = distance(input, 999999)
    return Answer(part1, part2)
