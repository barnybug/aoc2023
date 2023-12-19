from .utils import Answer


def hash(s):
    value = 0
    for c in s:
        value = (value + ord(c)) * 17 % 256
    return value


def solve(input: str):
    steps = input.split(",")
    part1 = sum(hash(step) for step in steps)

    boxes = [{} for _ in range(256)]
    for step in steps:
        if step[-1] == "-":
            n = hash(step[:-1])
            boxes[n].pop(step[:-1], None)
        else:
            key = step[:-2]
            n = hash(key)
            boxes[n][key] = step[-1]

    part2 = sum(
        (i + 1) * sum((j + 1) * int(fl) for j, fl in enumerate(box.values()))
        for i, box in enumerate(boxes)
    )

    return Answer(part1, part2)
