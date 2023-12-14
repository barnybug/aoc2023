import pytest


from aoc2023 import day12


@pytest.mark.parametrize(
    ("line", "answer"),
    [
        ("???.### 1,1,3", 1),
        (".??..??...?##. 1,1,3", 4),
        ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        ("????.#...#... 4,1,1", 1),
        ("????.######..#####. 1,6,5", 4),
        ("?###???????? 3,2,1", 10),
    ],
)
def test_01(line, answer):
    assert day12.arrangements(line) == answer


def test_02():
    assert day12.solve(testdata).part2 == None
