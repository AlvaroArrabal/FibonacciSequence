import pytest
from app.fibonacci import Fibonacci


@pytest.fixture
def fibonacci_sequence():
    return Fibonacci()


def test_sequence_initialization(fibonacci_sequence):
    assert fibonacci_sequence.get_iterations() == 0
    assert fibonacci_sequence.get_sequence() == []


@pytest.mark.parametrize("new_iterations, expected", [(2, 2), (5, 5), (10, 10)])
def test_iterations(fibonacci_sequence, new_iterations, expected):
    fibonacci_sequence.set_iterations(new_iterations)
    assert fibonacci_sequence.get_iterations() == expected


@pytest.mark.parametrize("iterations, expected", [(1, [0]), (2, [0, 1]), (5, [0, 1, 1, 2, 3])])
def test_sequence(fibonacci_sequence, iterations, expected):
    fibonacci_sequence.set_iterations(iterations)
    assert fibonacci_sequence.get_sequence() == expected


@pytest.mark.parametrize("iterations, position, expected", [
    (5, 0, 0),
    (5, 1, 1),
    (5, 4, 3)
])
def test_get_sequence_position(fibonacci_sequence, iterations, position, expected):
    fibonacci_sequence.set_iterations(iterations)
    assert fibonacci_sequence.get_sequence_position(position) == expected
