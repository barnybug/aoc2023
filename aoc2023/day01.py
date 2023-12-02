import re

from .utils import Answer


NUMBERS = "one|two|three|four|five|six|seven|eight|nine"
LOOKUP = {n: i + 1 for i, n in enumerate(NUMBERS.split("|"))} | {
    str(i): i for i in range(10)
}


def solution(lines, regex):
    matches = [regex.findall(line) for line in lines]
    return sum(LOOKUP[match[0]] * 10 + LOOKUP[match[-1]] for match in matches if match)


def solve(input: str):
    lines = input.split("\n")
    part1 = solution(lines, re.compile(r"(\d)"))
    part2 = solution(lines, re.compile(rf"(?:([0-9]|{NUMBERS}))"))
    return Answer(part1, part2)
