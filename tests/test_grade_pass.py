
import pytest
from src.grade_pass import has_passed


# Test valid inputs

# Checks whether a score below 50 is considered a fail.
def test_score_below_pass_mark():
    assert has_passed(49) is False

# Checks whether a score of exactly 50 is considered a pass.
def test_score_at_pass_mark():
    assert has_passed(50) is True

# Checks whether a score above 50 is considered a pass.
def test_score_above_pass_mark():
    assert has_passed(51) is True

# Checks whether the function can handle the minimum score of 0.
def test_score_zero():
    assert has_passed(0) is False

# Checks whether the function can handle the maximum score of 100.
def test_score_full_marks():
    assert has_passed(100) is True


# Test invalid input types

# Checks whether a TypeError is raised when the score is a string.
def test_invalid_score_string():
    with pytest.raises(TypeError):
        has_passed("50")

# Checks whether a TypeError is raised when the score is None.
def test_invalid_score_none():
    with pytest.raises(TypeError):
        has_passed(None)

# Checks whether a TypeError is raised when the score is True.
def test_invalid_score_true():
    with pytest.raises(TypeError):
        has_passed(True)

# Checks whether a TypeError is raised when the score is False.
def test_invalid_score_false():
    with pytest.raises(TypeError):
        has_passed(False)

# Checks whether a TypeError is raised when the score is a float.
def test_invalid_score_float():
    with pytest.raises(TypeError):
        has_passed(50.5)


# Test scores outside permitted range

# Checks whether a ValueError is raised when the score is below 0.
def test_score_below_range():
    with pytest.raises(ValueError):
        has_passed(-1)

# Checks whether a ValueError is raised when the score is above 100.
def test_score_above_range():
    with pytest.raises(ValueError):
        has_passed(101)
