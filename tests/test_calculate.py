import pytest
from calculate import calc

def test_calc_circle_area():
    assert calc('circle', 'area', [1]) == pytest.approx(3.14159, rel=1e-5)

def test_calc_circle_perimeter():
    assert calc('circle', 'perimeter', [1]) == pytest.approx(6.28318, rel=1e-5)

def test_calc_square_area():
    assert calc('square', 'area', [2]) == 4

def test_calc_square_perimeter():
    assert calc('square', 'perimeter', [2]) == 8

def test_invalid_figure():
    with pytest.raises(AssertionError):
        calc('invalid', 'area', [1])

def test_invalid_function():
    with pytest.raises(AssertionError):
        calc('circle', 'invalid', [1])

def test_invalid_size_for_circle():
    with pytest.raises(TypeError):
        calc('circle', 'area', [])

def test_invalid_size_for_square():
    with pytest.raises(TypeError):
        calc('square', 'area', [2, 2])
