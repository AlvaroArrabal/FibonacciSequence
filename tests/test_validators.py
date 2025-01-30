import pytest
from app.modules.utils import validate_position, validate_iterations


@pytest.mark.parametrize("position, iterations", [(0, 5), (2, 5), (4, 5)])
def test_validate_position_valid(position, iterations):
    try:
        validate_position(position, iterations)
    except ValueError:
        pytest.fail(f"ValueError was raised for valid position {position} with {iterations} iterations")


@pytest.mark.parametrize("position, iterations", [(-1, 5), (5, 5), (6, 5)])
def test_validate_position(position, iterations):
    with pytest.raises(ValueError):
        validate_position(position, iterations)


@pytest.mark.parametrize("iterations", [0, 1, 10, 100])
def test_validate_iterations_non_negative(iterations):
    try:
        validate_iterations(iterations)
    except ValueError:
        pytest.fail(f"ValueError was raised for valid iterations {iterations}")


@pytest.mark.parametrize("iterations", [-1, -10, -100])
def test_validate_iterations_negative(iterations):
    with pytest.raises(ValueError):
        validate_iterations(iterations)
