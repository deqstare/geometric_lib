import square


def test_square_area():
    assert square.area(2) == 4


def test_square_perimeter():
    assert square.perimeter(2) == 8


def test_square_area_zero():
    assert square.area(0) == 0


def test_square_perimeter_zero():
    assert square.perimeter(0) == 0
