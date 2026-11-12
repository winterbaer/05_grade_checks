
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from grade_average import calculate_average


# Test valid inputs

def test_average_normal_marks():
    assert calculate_average(50, 60) == 55.0


def test_average_with_decimal_result():
    assert calculate_average(50, 51) == 50.5


def test_average_zero_marks():
    assert calculate_average(0, 0) == 0.0


def test_average_full_marks():
    assert calculate_average(100, 100) == 100.0


def test_average_different_marks():
    assert calculate_average(70, 80) == 75.0


# Test invalid input types

def test_invalid_first_mark_string():
    with pytest.raises(TypeError):
        calculate_average("50", 60)


def test_invalid_second_mark_string():
    with pytest.raises(TypeError):
        calculate_average(50, "60")


def test_invalid_first_mark_none():
    with pytest.raises(TypeError):
        calculate_average(None, 50)


def test_invalid_second_mark_none():
    with pytest.raises(TypeError):
        calculate_average(50, None)


def test_invalid_first_mark_boolean():
    with pytest.raises(TypeError):
        calculate_average(True, 50)


def test_invalid_second_mark_boolean():
    with pytest.raises(TypeError):
        calculate_average(50, False)


def test_invalid_first_mark_float():
    with pytest.raises(TypeError):
        calculate_average(50.5, 60)


# Test marks outside permitted range

def test_first_mark_below_range():
    with pytest.raises(ValueError):
        calculate_average(-1, 50)


def test_first_mark_above_range():
    with pytest.raises(ValueError):
        calculate_average(101, 50)


def test_second_mark_below_range():
    with pytest.raises(ValueError):
        calculate_average(50, -1)


def test_second_mark_above_range():
    with pytest.raises(ValueError):
        calculate_average(50, 101)


# Demo: Changes to test files trigger GitHub Actions.