from aoc2023 import day18

testdata = open("tests/input18.txt").read()


def test_01():
    assert day18.solve(testdata).part1 == 62


def test_02():
    assert day18.solve(testdata).part2 == 952408144115
