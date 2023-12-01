from aoc2023 import day01

testdata = open("tests/input01.txt").read()
testdata2 = open("tests/input01b.txt").read()


def test_01():
    assert day01.solve(testdata).part1 == 142


def test_02():
    assert day01.solve(testdata2).part2 == 281
