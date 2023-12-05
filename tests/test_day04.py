from aoc2023 import day04

testdata = open("tests/input04.txt").read()


def test_01():
    assert day04.solve(testdata).part1 == 13


def test_02():
    assert day04.solve(testdata).part2 == 30
