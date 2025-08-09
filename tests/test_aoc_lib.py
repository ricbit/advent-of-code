import pytest
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
import aoc


def test_integer_compositions_basic():
    result = list(aoc.integer_compositions(3))
    assert result == [[3], [2, 1], [1, 2], [1, 1, 1]]


def test_integer_compositions_negative():
    with pytest.raises(ValueError):
        list(aoc.integer_compositions(-1))


def test_to_binary_basic():
    assert aoc.to_binary(5, 4) == "0101"


def test_to_binary_negative():
    with pytest.raises(ValueError):
        aoc.to_binary(-5, 4)


def test_bounds():
    b = aoc.bounds([(0, 0), (2, 3), (-1, 4)])
    assert (b.ymin, b.ymax, b.xmin, b.xmax) == (-1, 2, 0, 4)

