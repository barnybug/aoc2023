from aoc2023 import day17

testdata = open("tests/input17.txt").read()


def test_01():
    assert day17.part1(testdata) == 102


def test_02():
    assert day17.part2(testdata) == 94
