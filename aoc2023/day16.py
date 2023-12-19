from .utils import Answer, Point


def energized(grid, pos, vec):
    visited = set()
    beams = [(pos, vec)]
    while beams:
        beam = beams.pop()
        if beam in visited:
            continue
        visited.add(beam)
        pos, vec = beam
        c = grid[pos.y][pos.x]
        if c == "\\":
            vec = vec.turncw if vec.y == 0 else vec.turnccw
        elif c == "/":
            vec = vec.turncw if vec.x == 0 else vec.turnccw
        elif c == "|" and vec.y == 0:
            if pos.y > 0:
                beams.append((pos + Point.U, Point.U))
            vec = Point.D
        elif c == "-" and vec.x == 0:
            if pos.x > 0:
                beams.append((pos + Point.L, Point.L))
            vec = Point.R
        pos += vec
        if 0 <= pos.x < len(grid[0]) and 0 <= pos.y < len(grid):
            beams.append((pos, vec))

    return len({pos for pos, vec in visited})


def solve(input: str):
    grid = list(input.split("\n"))
    part1 = energized(grid, Point.Zero, Point.R)
    h = len(grid)
    w = len(grid[0])
    part2 = max(
        max(energized(grid, Point(0, i), Point.R) for i in range(h)),
        max(energized(grid, Point(w - 1, i), Point.L) for i in range(h)),
        max(energized(grid, Point(i, 0), Point.D) for i in range(w)),
        max(energized(grid, Point(i, h - 1), Point.U) for i in range(w)),
    )
    return Answer(part1, part2)
