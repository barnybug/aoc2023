from aoc2023 import day06

testdata = open("tests/input06.txt").read()


def test_01():
    assert day06.solve(testdata).part1 == 288


def test_02():
    assert day06.solve(testdata).part2 == 71503
