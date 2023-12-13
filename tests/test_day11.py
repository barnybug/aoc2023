from aoc2023 import day11

testdata = open("tests/input11.txt").read()


def test_01():
    assert day11.distance(testdata, 1) == 374


def test_02():
    assert day11.distance(testdata, 9) == 1030
    assert day11.distance(testdata, 99) == 8410
