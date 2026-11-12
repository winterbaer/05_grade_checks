
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from grade_pass import has_passed


# Test valid inputs

def test_score_below_pass_mark():
    assert has_passed(49) is False


def test_score_at_pass_mark():
    assert has_passed(50) is True


def test_score_above_pass_mark():
    assert has_passed(51) is True


def test_score_zero():
    assert has_passed(0) is False


def test_score_full_marks():
    assert has_passed(100) is True


# Test invalid input types

def test_invalid_score_string():
    with pytest.raises(TypeError):
        has_passed("50")


def test_invalid_score_none():
    with pytest.raises(TypeError):
        has_passed(None)


def test_invalid_score_true():
    with pytest.raises(TypeError):
        has_passed(True)


def test_invalid_score_false():
    with pytest.raises(TypeError):
        has_passed(False)


def test_invalid_score_float():
    with pytest.raises(TypeError):
        has_passed(50.5)


# Test scores outside permitted range

def test_score_below_range():
    with pytest.raises(ValueError):
        has_passed(-1)


def test_score_above_range():
    with pytest.raises(ValueError):
        has_passed(101)
