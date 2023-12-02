from .utils import Answer
from collections import defaultdict
from math import prod

limits = {"red": 12, "green": 13, "blue": 14}


def max_draw(draws: str):
    maximum = defaultdict(int)
    for draw in draws.split(";"):
        for balls in draw.split(","):
            no, colour = balls.split()
            maximum[colour] = max(int(no), maximum[colour])
    return maximum


def solve(input: str):
    part1 = part2 = 0
    for line in input.split("\n"):
        game, draws = line.split(":")
        if all(no <= limits[colour] for colour, no in max_draw(draws).items()):
            part1 += int(game[5:])
        part2 += prod(max_draw(draws).values())

    return Answer(part1, part2)
