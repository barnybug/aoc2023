from .utils import Answer, Point


MOVES = {
    (Point.D, "|"): Point.D,
    (Point.U, "|"): Point.U,
    (Point.R, "-"): Point.R,
    (Point.L, "-"): Point.L,
    (Point.D, "L"): Point.R,
    (Point.L, "L"): Point.U,
    (Point.R, "J"): Point.U,
    (Point.D, "J"): Point.L,
    (Point.R, "7"): Point.D,
    (Point.U, "7"): Point.L,
    (Point.L, "F"): Point.D,
    (Point.U, "F"): Point.R,
}


class Grid:
    def __init__(self, input) -> None:
        self.lines = input.split("\n")

    def __iter__(self):
        yield from (
            (Point(x, y), c)
            for y, row in enumerate(self.lines)
            for x, c in enumerate(row)
        )

    def __getitem__(self, p: Point):
        if p.y < 0 or p.y >= len(self.lines) or p.x < 0 or p.x >= len(self.lines[0]):
            return None
        return self.lines[p.y][p.x]


def solve(input: str):
    grid = Grid(input)
    start = pos = next(p for p, c in grid if c == "S")
    vec = next(d for d in Point.Dirs if (d, grid[pos + d]) in MOVES)
    path = []
    vecs = []

    # Work out path round the pipe
    while True:
        path.append(pos)
        vecs.append(vec)
        pos += vec
        if pos == start:
            break
        vec = MOVES[(vec, grid[pos])]

    # Furthest point is halfway around
    part1 = len(path) // 2
    pieces = set(path)

    def try_fill(path, vecs):
        # Fill in the path assuming CW loop
        filled = set()

        def fill(p):
            # Flood fill
            q = [p]
            while q:
                p = q.pop()
                if grid[p] is None:  # out of bounds
                    raise ValueError("out of bounds")
                if p in filled or p in pieces:
                    continue
                filled.add(p)
                q.extend([p + d for d in Point.Dirs])

        for pos, a, b in zip(path, vecs[-1:] + vecs, vecs):
            # a is the entry vector, b the exit vector
            if a == b:
                # straight piece - inside is clockwise turn
                fill(pos + a.turncw)
            elif a.turnccw == b:
                # ->J, etc - fill 'below' and to the 'right' (corner covered by flood)
                fill(pos + a)
                fill(pos + a.turncw)
            # ->7, etc - nothing to do - corner covered by others

        return len(filled)

    try:
        # Try to fill assuming going CW first
        part2 = try_fill(path, vecs)
    except ValueError:
        # Filled outside path => must have been traversing CCW, so reverse direction
        rpath = path[:1] + path[:0:-1]  # start stays as is, then last, last but 1, etc.
        rvecs = [v.turncw.turncw for v in vecs[::-1]]  # reverse vectors
        part2 = try_fill(rpath, rvecs)

    return Answer(part1, part2)
