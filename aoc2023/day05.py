import re
from .utils import Answer
from typing import NamedTuple


class Seed(NamedTuple):
    start: int
    size: int

    @property
    def end(self):
        return self.start + self.size - 1


def run(seeds: list[Seed], maps):
    for ranges in maps:
        next_seeds = []
        # print(len(seeds), seeds)
        # breakpoint()
        for seed in seeds:
            for src, dest in ranges:
                if seed.start > src.end:
                    continue  # check next

                if seed.end < src.start:
                    next_seeds.append(seed)  # 1-1
                    break  # no more matches

                if seed.start < src.start:
                    prefix = Seed(seed.start, src.start - seed.start)  # 1-1
                    next_seeds.append(prefix)

                    overlap = Seed(
                        dest, src.size if seed.end > src.end else seed.end - src.start
                    )
                else:
                    overlap = Seed(
                        dest + seed.start - src.start,
                        src.end - seed.start if seed.end > src.end else seed.size,
                    )
                next_seeds.append(overlap)

                if seed.end > src.end:
                    suffix = Seed(src.end + 1, seed.end - src.end)
                    seeds.append(suffix)  # may be translated by later mappings

                break
            else:
                next_seeds.append(seed)  # 1-1

        seeds = next_seeds

    return min(s.start for s in seeds)


def solve(input: str):
    parts = input.split("\n\n")
    seeds = list(map(int, re.findall(r"\d+", parts[0])))

    maps = []
    for part in parts[1:]:
        ranges = [map(int, line.split()) for line in part.split("\n")[1:]]
        ranges = [(Seed(src, size), dest) for dest, src, size in ranges]
        ranges.sort()
        maps.append(ranges)

    part1_seeds = [Seed(s, 1) for s in seeds]
    part1 = run(part1_seeds, maps)

    part2_seeds = [Seed(a, b) for a, b in zip(seeds[::2], seeds[1::2])]
    part2 = run(part2_seeds, maps)

    return Answer(part1, part2)
