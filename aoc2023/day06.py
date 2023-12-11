from math import prod, sqrt, floor, ceil

from .utils import Answer


def quadratic(a, b, c):
    root = sqrt(b * b - 4 * a * c)
    return ((-b - root) / (2 * a), (-b + root) / (2 * a))


def race(time: int, record: int) -> int:
    # (time - x) * x > record
    # time * x - x^2 > record
    # x^2 - time * x + record < 0
    # x^2 - time * x + record + 1 <= 0
    x1, x2 = quadratic(1, -time, record + 1)
    wins = floor(x2) - ceil(x1) + 1
    return wins


def solve(input: str):
    times, distances = input.split("\n")[:2]
    times = map(int, times.split()[1:])
    distances = map(int, distances.split()[1:])

    part1 = prod(race(time, distance) for time, distance in zip(times, distances))

    times, distances = input.replace(" ", "").split("\n")[:2]
    times = map(int, times.split(":")[1:])
    distances = map(int, distances.split(":")[1:])

    part2 = prod(race(time, distance) for time, distance in zip(times, distances))
    return Answer(part1, part2)
