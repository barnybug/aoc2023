from itertools import pairwise
from .utils import Answer, D_to_P, Point


def part(steps):
    pos = Point.Zero
    points = [pos]  # top left
    for (d, n), (d2, _) in pairwise(steps):
        pos += D_to_P[d] * n
        # Handle rounding on corners correctly
        # A turn D pushes the area out rightwards, A turn L pushes the area out downwards
        points.append(Point(pos.x + int("D" in (d, d2)), pos.y + int("L" in (d, d2))))

    # Shoelace algorithm
    s1 = sum(a.x * b.y for a, b in pairwise(points))
    s2 = sum(a.y * b.x for a, b in pairwise(points))
    return abs(s1 - s2) // 2


def solve(input: str):
    steps = [line.split() for line in input.split("\n")]
    steps = [(d, int(n)) for (d, n, _) in steps]
    part1 = part(steps)

    colours = [line[line.index("#") + 1 :][:6] for line in input.split("\n")]
    steps = [("RDLU"[int(c[-1])], int(c[:5], 16)) for c in colours]
    part2 = part(steps)

    return Answer(part1, part2)
