import sys
import heapq

from .utils import Answer, Point


def solution(input: str, min_blocks, max_blocks):
    grid = [[int(c) for c in line] for line in input.split("\n")]
    shortest = {Point.Zero: 0}
    # A heap is the most efficient structure to use here - so we explore the tree lowest loss first
    heap = []
    h = len(grid) - 1
    w = len(grid[0]) - 1
    finish = Point(w, h)
    answer = sys.maxsize

    def step(pos, loss, vec):
        nonlocal answer
        for i in range(1, max_blocks + 1):
            pos += vec
            if pos.y < 0 or pos.y > h or pos.x < 0 or pos.x > w:
                return
            loss += int(grid[pos.y][pos.x])
            if i < min_blocks:
                continue

            key = (pos, vec)
            if loss >= shortest.get(key, sys.maxsize):
                continue

            shortest[key] = loss
            if pos == finish:
                answer = min(answer, loss)
                return
            heapq.heappush(heap, (loss, pos, vec))

    step(Point.Zero, 0, Point.R)
    step(Point.Zero, 0, Point.D)

    while heap:
        (loss, pos, vec) = heapq.heappop(heap)
        step(pos, loss, vec.turnccw)
        step(pos, loss, vec.turncw)

    return answer


def part1(input: str):
    return solution(input, 1, 3)


def part2(input: str):
    return solution(input, 4, 10)


def solve(input: str):
    return Answer(part1(input), part2(input))
