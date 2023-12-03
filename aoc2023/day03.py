from math import prod
from .utils import Answer, Point


class Grid:
    def __init__(self, input: str):
        self.lines = input.split("\n")

    def __iter__(self):
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                yield Point(x, y), c

    @property
    def width(self):
        return len(self.lines[0])


def solve(input: str):
    grid = Grid(input)
    symbols = {p for p, c in grid if c not in "0123456789."}
    gears = {p: [] for p, c in grid if c == "*"}

    numbers = []
    num = ""
    nearby = set()
    for p, c in grid:
        if c.isdigit():
            num += c
            nearby.update(symbols.intersection(p.around()))

        if num and (p.x + 1 == grid.width or not c.isdigit()):
            if nearby:
                numbers.append(int(num))
            for g in nearby:
                if g in gears:
                    gears[g].append(int(num))
            num = ""
            nearby = set()

    part1 = sum(numbers)
    part2 = sum(prod(nums) for nums in gears.values() if len(nums) == 2)

    return Answer(part1, part2)
