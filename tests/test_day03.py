from aoc2023 import day03

testdata = open("tests/input03.txt").read()
realdata = open("aoc2023/inputs/input03.txt").read()


def test_01():
    assert day03.solve(testdata).part1 == 4361


def test_02():
    assert day03.solve(testdata).part2 == 467835


def test_answer_01():
    assert day03.solve(realdata).part1 == 540131


def test_answer_02():
    assert day03.solve(realdata).part2 == 86879020
