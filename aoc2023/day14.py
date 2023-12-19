import numpy as np


from .utils import Answer


def roll(arr):
    h = arr.shape[0]
    for x in range(arr.shape[1]):
        top = 0
        for y in range(h):
            if arr[y, x] == "#":
                top = y + 1
                continue
            elif arr[y, x] == "O":
                if top < y:
                    arr[top, x] = "O"
                    arr[y, x] = "."
                top += 1
    return arr


def cycle(arr):
    for _ in (0, 1, 2, 3):
        roll(arr)
        arr = np.rot90(arr, -1)


def load(arr):
    return sum((len(arr) - y) * sum(arr[y] == "O") for y in range(len(arr)))


def tostring(arr):
    return "\n".join("".join(row) for row in arr)


def solve(input: str):
    arr = np.array([list(line) for line in input.split("\n")])
    part1 = load(roll(arr))

    arr = np.array([list(line) for line in input.split("\n")])
    arrs = {tostring(arr): 0}
    loads = [load(arr)]
    target = 1_000_000_000
    part2 = 0
    for i in range(target):
        cycle(arr)
        s = tostring(arr)
        if s in arrs:
            start = arrs[s]
            length = i - start
            remain = (target - start) % length
            part2 = loads[remain + start]
            break
        arrs[s] = i
        loads.append(load(arr))

    return Answer(part1, part2)
