from aoc2023 import day15

testdata = open("tests/input15.txt").read()


def test_01():
    assert day15.solve(testdata).part1 == 1320


def test_02():
    assert day15.solve(testdata).part2 == 145
