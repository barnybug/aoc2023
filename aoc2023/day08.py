from itertools import cycle
import math
import re

from .utils import Answer


def solve(input: str):
    lookup = {}
    steps, network = input.split("\n\n")
    steps = [int(step == "R") for step in steps]

    for line in network.split("\n"):
        s, left, right = re.findall(r"([A-Z0-9]+)", line)
        lookup[s] = (left, right)

    finishes = {key for key in lookup if key.endswith("Z")}

    def walk(at: str) -> int:
        for i, step in enumerate(cycle(steps)):
            at = lookup[at][step]
            if at in finishes:
                return i + 1
        return 0

    part1 = walk("AAA") if "AAA" in lookup else 0
    starts = [key for key in lookup if key.endswith("A")]
    # assumption: start->end is the repeating cycle length (?)
    ends = [walk(start) for start in starts]
    part2 = math.lcm(*ends)

    return Answer(part1, part2)
