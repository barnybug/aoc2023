from aoc2023 import day08

testpart1 = open("tests/input08.txt").read()
testpart2 = open("tests/input08b.txt").read()


def test_01():
    assert day08.solve(testpart1).part1 == 6


def test_02():
    assert day08.solve(testpart2).part2 == 6
