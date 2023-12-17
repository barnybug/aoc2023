from functools import cache
from .utils import Answer


@cache
def count(numbers: tuple, dots: int, sets: int, length: int) -> int:
    ret = 0
    n = numbers[0]
    remain = length - sum(numbers) - len(numbers) + 1
    bits = (1 << n) - 1
    for i in range(remain + 1):
        if sets & (1 << i) - 1 or dots & bits or sets & (1 << i + n):
            bits <<= 1
            continue

        shift = n + i + 1
        if len(numbers) == 1:
            if not sets >> shift:
                ret += 1
        else:
            ret += count(numbers[1:], dots >> shift, sets >> shift, length - shift)

        bits <<= 1

    return ret


def arrangements(pattern: str, numbers: list[int]) -> int:
    pattern = pattern.strip(".").rstrip(".")
    dots = sum(1 << i for i, c in enumerate(pattern) if c == ".")
    sets = sum(1 << i for i, c in enumerate(pattern) if c == "#")

    return count(tuple(numbers), dots, sets, len(pattern))


def part1(line: str):
    pattern, numbers = parse(line)
    return arrangements(pattern, numbers)


def part2(line: str):
    pattern, numbers = parse(line)
    pattern = "?".join([pattern] * 5)
    numbers = numbers * 5
    return arrangements(pattern, numbers)


def parse(line: str):
    pattern, numbers = line.split(" ")
    numbers = [int(n) for n in numbers.split(",")]
    return pattern, numbers


def solve(input: str):
    lines = input.split("\n")
    p1 = sum(part1(line) for line in lines)
    p2 = sum(part2(line) for line in lines)
    return Answer(p1, p2)
