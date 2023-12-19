from aoc2023 import day16

testdata = open("tests/input16.txt").read()


def test_01():
    assert day16.solve(testdata).part1 == 46


def test_02():
    assert day16.solve(testdata).part2 == 51
