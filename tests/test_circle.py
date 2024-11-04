import pytest
import circle


def test_circle_area():
    assert circle.area(1) == pytest.approx(3.14159, rel=1e-5)


def test_circle_perimeter():
    assert circle.perimeter(1) == pytest.approx(6.28318, rel=1e-5)


def test_circle_area_zero():
    assert circle.area(0) == 0


def test_circle_perimeter_zero():
    assert circle.perimeter(0) == 0
