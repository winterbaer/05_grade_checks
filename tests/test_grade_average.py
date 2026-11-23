
import pytest
from src.grade_average import calculate_average


# Test valid inputs

# Checks whether the function correctly calculates the average of two normal marks.
def test_average_normal_marks():
    assert calculate_average(50, 60) == 55.0

# Checks whether the function can return a decimal average instead of rounding it down.
def test_average_with_decimal_result():
    assert calculate_average(50, 51) == 50.5

# Checks whether the function can handle the minimum mark of 0.
def test_average_zero_marks():
    assert calculate_average(0, 0) == 0.0

# Checks whether the function can handle the maximum mark of 100.
def test_average_full_marks():
    assert calculate_average(100, 100) == 100.0

# Checks whether the function correctly calculates the average of two different marks.
def test_average_different_marks():
    assert calculate_average(70, 80) == 75.0


# Test invalid input types

# Checks whether a TypeError is raised when the first mark is a string.
def test_invalid_first_mark_string():
    with pytest.raises(TypeError):
        calculate_average("50", 60)

# Checks whether a TypeError is raised when the second mark is a string.
def test_invalid_second_mark_string():
    with pytest.raises(TypeError):
        calculate_average(50, "60")

# Checks whether a TypeError is raised when the first mark is None.
def test_invalid_first_mark_none():
    with pytest.raises(TypeError):
        calculate_average(None, 50)

# Checks whether a TypeError is raised when the second mark is None.
def test_invalid_second_mark_none():
    with pytest.raises(TypeError):
        calculate_average(50, None)

# Checks whether a TypeError is raised when the first mark is a Boolean value.
def test_invalid_first_mark_boolean():
    with pytest.raises(TypeError):
        calculate_average(True, 50)


# Checks whether a TypeError is raised when the second mark is a Boolean value.
def test_invalid_second_mark_boolean():
    with pytest.raises(TypeError):
        calculate_average(50, False)

# Checks whether a TypeError is raised when the first mark is a float.
def test_invalid_first_mark_float():
    with pytest.raises(TypeError):
        calculate_average(50.5, 60)


# Checks whether a TypeError is raised when the second mark is a float.
def test_invalid_second_mark_float():
    with pytest.raises(TypeError):
        calculate_average(50, 50.5)


# Test marks outside permitted range

# Checks whether a ValueError is raised when the first mark is below 0.
def test_first_mark_below_range():
    with pytest.raises(ValueError):
        calculate_average(-1, 50)


# Checks whether a ValueError is raised when the first mark is above 100.
def test_first_mark_above_range():
    with pytest.raises(ValueError):
        calculate_average(101, 50)

# Checks whether a ValueError is raised when the second mark is below 0.
def test_second_mark_below_range():
    with pytest.raises(ValueError):
        calculate_average(50, -1)

# Checks whether a ValueError is raised when the second mark is above 100.
def test_second_mark_above_range():
    with pytest.raises(ValueError):
        calculate_average(50, 101)
