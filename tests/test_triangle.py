import triangle


def test_triangle_area():
    assert triangle.area(3, 4, 5) == 6


def test_triangle_perimeter():
    assert triangle.perimeter(3, 4, 5) == 12


def test_triangle_area_zero():
    assert triangle.area(0, 0, 0) == 0


def test_triangle_perimeter_zero():
    assert triangle.perimeter(0, 0, 0) == 0
