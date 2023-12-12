from aoc2023 import day10

testdata = open("tests/input10.txt").read()
testdatab = open("tests/input10b.txt").read()
testdatac = open("tests/input10c.txt").read()
testdatad = open("tests/input10d.txt").read()
testdatae = open("tests/input10e.txt").read()
testdataf = open("tests/input10f.txt").read()


def test_01():
    assert day10.solve(testdata).part1 == 4
    assert day10.solve(testdatab).part1 == 8


def test_02():
    assert day10.solve(testdata).part2 == 1
    assert day10.solve(testdatab).part2 == 1
    assert day10.solve(testdatac).part2 == 4
    assert day10.solve(testdatad).part2 == 4
    assert day10.solve(testdatae).part2 == 8
    assert day10.solve(testdataf).part2 == 10
