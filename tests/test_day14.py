from aoc2023 import day14

testdata = open("tests/input14.txt").read()


def test_01():
    assert day14.solve(testdata).part1 == 136


def test_02():
    assert day14.solve(testdata).part2 == 64
